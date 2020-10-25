#!/usr/bin/env python3

import unittest
import subprocess
import os

from test_common import run, Valgrind, lines


class CardsTests (unittest.TestCase):
  def setUp (self):
    if not os.path.isfile("./cards"): self.skipTest("Program doesn't exist")
    self.rc,self.r = run("./cards")
    self.r = lines(self.r)
    self.assertGreater(self.rc, -1, "Program crashed!")
    self.assertEqual(self.rc, 0, "Program returned nonzero")
    #if len(self.r) != 52: self.skipTest("Wrong number of cards")

  def test_contains_proper_deck (self):
    cards = [x.lower().split(" of ") for x in self.r]

    rankname = lambda r: {1:"ace",11:"jack",12:"queen",13:"king"}.get(r,str(r))
    ac = [(rankname(r),s) for s in "hearts spades diamonds clubs".split()
                            for r in range(1,14)]

    counts = {c:0 for c in ac}

    for c in cards:
      self.assertTrue(len(c) == 2, "Improperly formatted line")

      c = tuple(c)
      self.assertIn(c, ac, "%s of %s is not a valid card" % c)

      counts[c] += 1

    missing = {c for c,n in counts.items() if n == 0}
    multiple = {c for c,n in counts.items() if n > 1}

    if multiple: self.fail("Duplicated cards: %s" % (multiple,))
    if missing: self.fail("Missing cards: %s" % (missing,))


class CardsRandomizationTests (unittest.TestCase):
  def _test_suits_seem_random (self, num):
    if not os.path.isfile("./cards"): self.skipTest("Program doesn't exist")
    self.ok = False
    srand = "call srand(%s)" % (num,)
    self.rc,self.r = run(*["gdb","./cards","-ex","break main","-ex","r","-ex",
                           srand,"-ex","c","-ex","q"])
    self.r = self.r.split("\nContinuing.\n",1)[1]
    self.r = self.r.rsplit("[",1)[0].strip()
    self.r = lines(self.r)
    self.assertGreater(self.rc, -1, "Program crashed!")
    self.assertEqual(self.rc, 0, "Program returned nonzero")

    cards = [x.lower().split(" of ") for x in self.r]

    rankname = lambda r: {1:"ace",11:"jack",12:"queen",13:"king"}.get(r,str(r))
    ac = [(rankname(r),s) for s in "hearts spades diamonds clubs".split()
                            for r in range(1,14)]

    counts = {c:0 for c in ac}

    for c in cards:
      if len(c) != 2: self.skipTest("Bad deck")

      c = tuple(c)
      if c not in ac: self.skipTest("Bad deck")

      counts[c] += 1

    missing = {c for c,n in counts.items() if n == 0}
    multiple = {c for c,n in counts.items() if n > 1}

    if multiple or missing: self.skipTest("Bad deck")

    last_suit = None
    suit_switches = 0
    for c in cards:
      _,suit = c
      if last_suit is None:
        last_suit = suit
        continue
      if last_suit != suit:
        suit_switches += 1
      last_suit = suit

    self.ok = True
    self.assertGreater(suit_switches, 30)

  def test_suits_seem_random (self):
    i = 0
    while True:
      try:
        self.ok = False
        self._test_suits_seem_random(i)
        break
      except Exception as e:
        i += 1
        if not self.ok: raise
        if i > 10: raise

  def _test_ranks_seem_random (self, num):
    if not os.path.isfile("./cards"): self.skipTest("Program doesn't exist")
    self.ok = False
    srand = "call srand(%s)" % (num,)
    self.rc,self.r = run(*["gdb","./cards","-ex","break main","-ex","r","-ex",
                           srand,"-ex","c","-ex","q"])
    self.r = self.r.split("\nContinuing.\n",1)[1]
    self.r = self.r.rsplit("[",1)[0].strip()
    self.r = lines(self.r)
    self.assertGreater(self.rc, -1, "Program crashed!")
    self.assertEqual(self.rc, 0, "Program returned nonzero")

    cards = [x.lower().split(" of ") for x in self.r]

    rankname = lambda r: {1:"ace",11:"jack",12:"queen",13:"king"}.get(r,str(r))
    ac = [(rankname(r),s) for s in "hearts spades diamonds clubs".split()
                            for r in range(1,14)]

    counts = {c:0 for c in ac}

    for c in cards:
      if len(c) != 2: self.skipTest("Bad deck")

      c = tuple(c)
      if c not in ac: self.skipTest("Bad deck")

      counts[c] += 1

    missing = {c for c,n in counts.items() if n == 0}
    multiple = {c for c,n in counts.items() if n > 1}

    if multiple or missing: self.skipTest("Bad deck")

    rn_to_n = {rankname(n):n for n in range(1,14)}

    prev = None
    switches = 0
    for c in cards:
      rank,suit = c
      rank = rn_to_n[rank]
      if prev is None: prev = rank
      if abs(prev-rank) > 1: switches += 1
      prev = rank

    self.assertGreater(switches, 25)

  def test_ranks_seem_random (self):
    i = 0
    while True:
      try:
        self.ok = False
        self._test_ranks_seem_random(i)
        break
      except Exception as e:
        i += 1
        if not self.ok: raise
        if i > 10: raise


class CardsMemoryTests (Valgrind.Case):
  arg = "./cards"


if __name__ == "__main__":
  unittest.main()
