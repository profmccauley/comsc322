#!/usr/bin/env python3

import unittest
import subprocess
import os

from test_common import run, Valgrind, lines


class SizeTestCases (unittest.TestCase):
  def setUp (self):
    if not os.path.isfile("./sizes"): self.skipTest("Program doesn't exist")
    self.rc,self.r = run("./sizes")

  def test_return_code (self):
    self.assertEqual(self.rc, 0, "Nonzero exit code")

  def test_number_of_results (self):
    self.assertEqual(len(lines(self.r)), 5, "Expected five lines of output")

  def _ts (self, t, *sizes):
    sizes = set(int(i) for i in sizes)

    for l in lines(self.r):
      if not l.startswith("size of "): continue
      l = l.split("size of ", 1)[1].split(" is ")
      if len(l) != 2: continue
      if l[0] != t: continue
      if l[1].lower() == "x": self.fail("Size should not be 'X'!")
      if not l[1]: self.fail("Size should not be empty")
      if not l[1].isdigit(): self.fail("Size value is not an integer?")

      self.assertTrue(int(l[1]) in sizes,
                      "Size %s should be one of %s, not %s"
                      % (t, list(sizes), l[1]))
      return

    self.fail("Did not find size for " + t)

  def test_char (self):
    self._ts("char", 1)

  def test_short (self):
    self._ts("short", 2)

  def test_int (self):
    self._ts("int", 4, 8)

  def test_long (self):
    self._ts("long", 8)

  def test_voidp (self):
    self._ts("void *", 8)


if __name__ == "__main__":
  unittest.main()
