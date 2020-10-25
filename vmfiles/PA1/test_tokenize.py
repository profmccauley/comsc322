#!/usr/bin/env python3

import unittest
import subprocess
import os

from test_common import run, Valgrind, lines


class TokenizeTest (object):
  class Case (unittest.TestCase):
    arg1 = None
    arg2 = None
    expect = False # Fail
    expect_fail = False

    def setUp (self):
      if self.expect is False: self.expect_fail = True
      a = [self.arg1]
      if self.arg2 is not None: a.append(self.arg2)
      a = [str(x) for x in a]
      if not os.path.isfile("./tokenize"): self.skipTest("Program doesn't exist")
      self.rc,self.r = run("./tokenize", *a)

    def test (self):
      if self.rc < 0: self.fail("Program crashed!")
      if self.expect_fail:
        self.assertNotEqual(self.rc, 0, "Expected nonzero return value")
        if self.expect is False: return
        self.assertEqual(self.r, self.expect)
      else:
        self.assertEqual(self.rc, 0, "Expected zero return value")
        self.assertEqual(self.r, self.expect)


class TokenizeArg2 (TokenizeTest.Case):
  arg1 = "Mount Holyoke College"
  arg2 = 2
  expect = "Holyoke"

class TokenizeNoArg (TokenizeTest.Case):
  arg1 = "Mount Holyoke College"
  expect = "Mount\nHolyoke\nCollege"

class TokenizeArgTooBig (TokenizeTest.Case):
  arg1 = "Mount Holyoke College"
  arg2 = 5
  expect = "The string contains fewer than 5 tokens."
  expect_fail = True

class TokenizeArgTooSmall1 (TokenizeTest.Case):
  arg1 = "Mount Holyoke College"
  arg2 = 0
  expect = False


class TokenizeMemoryTests (Valgrind.Case):
  args = ["./tokenize","this is a test",2]


if __name__ == "__main__":
  unittest.main()
