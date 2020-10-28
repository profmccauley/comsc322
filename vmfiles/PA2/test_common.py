import unittest
import subprocess
import os


def run (cmd, *args):
  want_stderr = False
  if cmd is True:
    want_stderr = True
    cmd = args[0]
    args = args[1:]

  if args:
    cmd = [cmd] + [str(s) for s in args]
  else:
    cmd = cmd.split()

  r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL)

  if want_stderr:
    return r.returncode,r.stdout.decode("utf8").strip(),r.stderr.decode("utf8").strip()
  return r.returncode,r.stdout.decode("utf8").strip()


def lines (s):
  if not s: return []
  return s.split("\n")


class Valgrind (object):
  class Case (unittest.TestCase):
    arg = None
    args = []

    def setUp (self):
      if self.arg: assert not self.args
      else: assert not self.arg
      if self.arg: arg = self.arg.split(" ")
      else: arg = self.args

      if not os.path.isfile(arg[0]): self.skipTest("Program doesn't exist")

      arg = ["valgrind","--leak-check=full"] + arg
      self.rc,self.r,self.v = run(True, *arg)
      if self.rc < 0: self.skipTest("Program crashed")
      if self.rc == 127: self.skipTest("Valgrind error?")
      #self.assertEqual(self.rc, 0, "Expected 0 return value")
      l = [x[2:] for x in lines(self.v) if x.startswith("==")]
      l = [x.split("==",1)[-1] for x in l]
      self.v = l

    def test_no_definitely_lost (self):
      l = [x for x in self.v if x.strip().startswith("definitely lost: ")]
      if len(l) == 0: return
      assert len(l) == 1
      l = l[0]
      l = int(l.split(":",1)[1].strip().split()[0])
      self.assertEqual(l, 0, "Some memory definitely lost")

    def test_no_indirectly_lost (self):
      l = [x for x in self.v if x.strip().startswith("indirectly lost: ")]
      if len(l) == 0: return
      assert len(l) == 1
      l = l[0]
      l = int(l.split(":",1)[1].strip().split()[0])
      self.assertEqual(l, 0, "Some memory definitely lost")

    def test_jump_or_move_on_uninitialized_data (self):
      l = [x for x in self.v if x.strip().startswith("Conditional jump or move depends on uninitialised ")]
      self.assertEqual(len(l), 0, "Conditional jump/move depends on uninitialized data")

    def test_use_of_uninitialized_data (self):
      l = [x for x in self.v if x.strip().startswith("Use of uninitialised value ")]
      self.assertEqual(len(l), 0, "Use of uninitialized data")


class SimpleTest (object):
  class Case (unittest.TestCase):
    prog = None
    args = ()
    expect = False # Fail
    expect_fail = False

    def setUp (self):
      a = [str(x) for x in self.args]
      if not os.path.isfile(self.prog): self.skipTest("Program doesn't exist")
      self.rc,self.r = run(self.prog, *a)

    def test (self):
      if self.rc < 0: self.fail("Program crashed!")
      if self.expect_fail:
        self.assertNotEqual(self.rc, 0, "Expected nonzero return value")
        if self.expect is False: return
        self._check_output()
      else:
        self.assertEqual(self.rc, 0, "Expected zero return value")
        if self.expect is False: return
        self._check_output()

    def _check_output (self):
      self.assertEqual(self.r, self.expect)
