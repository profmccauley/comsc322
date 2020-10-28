#!/usr/bin/env python3

import unittest
import subprocess
import os

from test_common import run, Valgrind, SimpleTest

class RandomTooFewArgs1 (SimpleTest.Case):
  prog = "./make_random"
  args = ()
  expect_fail = True

class RandomTooFewArgs3 (SimpleTest.Case):
  prog = "./make_random"
  args = (1,2)
  expect_fail = True

class RandomTooManyArgs (SimpleTest.Case):
  prog = "./make_random"
  args = (1,2,3,4,5)
  expect_fail = True

class NumLines (SimpleTest.Case):
  prog = "./make_random"
  args = (1,2,10,42)

  def _check_output (self):
    self.assertEqual(len(self.r), 42)

class KnownOutput (SimpleTest.Case):
  prog = "./make_random"
  args = (5,0,10,5)
  expect = "\n".join(str(x) for x in [0,10,1,6,5])


if __name__ == "__main__":
  unittest.main()
