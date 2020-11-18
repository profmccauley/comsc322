#!/usr/bin/env python3

import unittest
import subprocess
import os
import tempfile
from unittest import skipIf

from test_common import Valgrind, SimpleTest, skipIfFailed


def random_string (size=10):
  import random
  import string
  v = ""
  for _ in range(size):
    v += random.choice(string.ascii_uppercase)
  return v


class TooManyArgs (SimpleTest.Case):
  prog = "./mhcsh"
  args = (1,)
  expect_fail = True
  expect_err = False


class ExitNo (SimpleTest.Case):
  prog = "./mhcsh"
  rv = None

  def __init__ (self, *args, **kw):
    super().__init__(*args, **kw)
    if self.rv is None:
      self.stdin = "exit\n"
      self.rv = 0
    else:
      self.stdin = "exit %s\n" % (self.rv,)
    self.expect_fail = self.rv != 0

  def _check_output (self):
    self.assertEqual(self.rc, self.rv)


class Exit0 (ExitNo):
  rv = 0


class Exit8 (ExitNo):
  rv = 8


class Prompt1 (SimpleTest.Case):
  prog = "./mhcsh"

  def _check_output (self):
    r = self.r.split("\n")[0]
    self.assertEqual(r, "mhcsh>")


class Prompt2 (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "X"

  def _check_output (self):
    r = self.r.split("\n")[0]
    self.assertEqual(r, "mhcsh> X")


class NoErrorOnNothing (SimpleTest.Case):
  prog = "./mhcsh"

  def _check_output (self):
    self.assertEqual(self.e, "")


class InvalidCommand (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "this_is_not_a_valid_command"

  def _check_output (self):
    self.assertIn("mhcsh>", self.r)
    self.assertNotEqual(self.e, "")


@skipIfFailed(Prompt2)
class EmptyLines (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "\n\n\n\n\n\n\n\n\n"

  def _check_output (self):
    self.assertEqual(self.e, "")
    p = "mhcsh> \n"
    p = p * 4
    self.assertIn(p, self.r)


class Pwd (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "pwd"

  def _check_output (self):
    import os
    wd = os.getcwd()

    r = self.r.split("\n")
    self.assertIn(wd, r)
    self.assertEqual(self.e, "")


class PwdArg (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "pwd 3"

  def _check_output (self):
    self.assertNotEqual(self.e, "")


@skipIfFailed(Pwd)
class Cd (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "cd /proc\npwd"

  def _check_output (self):
    r = self.r.split("\n")[-2:]
    self.assertIn("/proc", r)


@skipIfFailed(Pwd)
class CdHome (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "cd\npwd"

  def _check_output (self):
    import pathlib
    home = str(pathlib.Path.home())

    r = self.r.split("\n")[-2:]
    self.assertIn(home, r)


class CdTwoArgs (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "cd / /"

  def _check_output (self):
    self.assertNotEqual(self.e, "")


class ExternalProgramsWithPath (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "/usr/bin/env"

  def _extraSetUp (self):
    import os
    n = "TEST_VARIABLE_" + random_string()
    v = random_string()
    os.environ[n] = v
    self.var = n,v

  def _check_output (self):
    self.assertEqual(self.e, "")
    self.assertIn("%s=%s" % self.var, self.r.split("\n"))


class ExternalProgramsNoPath (ExternalProgramsWithPath):
  stdin = "env"


@skipIfFailed(ExternalProgramsWithPath)
class ExternalProgramsWithArgs (SimpleTest.Case):
  prog = "./mhcsh"

  def _extraSetUp (self):
    import os
    for i in range(10):
      n = "TEST_VARIABLE_" + str(i) + "_" + random_string()
      v = random_string()
      os.environ[n] = v
    n = "TEST_VARIABLE_" + random_string()
    v = random_string()
    self.var = n,v
    self.stdin = "/usr/bin/env -i %s=%s" % self.var

  def _check_output (self):
    self.assertEqual(self.e, "")
    r = [x for x in self.r.split("\n") if x]
    self.assertIn("%s=%s" % self.var, r)
    self.assertLess(len(r), 6)


@skipIfFailed(ExternalProgramsWithArgs)
class Set (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "set TESTVARIABLE foo\n/usr/bin/env"

  def _check_output (self):
    self.assertEqual(self.e, "")
    r = self.r.split("\n")
    self.assertIn("TESTVARIABLE=foo", r)


@skipIfFailed(ExternalProgramsWithArgs)
class Waits (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "/usr/bin/sleep 0.5"

  def _extraSetUp (self):
    import time
    self.start = time.time()

  def _check_output (self):
    self.assertEqual(self.e, "")
    import time
    t = time.time() - self.start
    self.assertGreaterEqual(t, 0.5)


@skipIfFailed(ExternalProgramsWithArgs)
class SpacesAfter (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = '/usr/bin/date   '
  expect_fail = False


@skipIfFailed(ExternalProgramsWithArgs)
class SpacesBefore (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = '    /usr/bin/date'
  expect_fail = False


@skipIfFailed(ExternalProgramsWithArgs)
class SpacesBetween (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = '/usr/bin/date    -R'
  expect_fail = False


@skipIfFailed(Exit8)
class SpaceBetweenBuiltin (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "exit     9"
  expect_fail = True

  def _check_output (self):
    self.assertEqual(self.rc, 9)


if __name__ == "__main__":
  unittest.main()
