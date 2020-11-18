from test_mhcsh import *

@skipIfFailed(ExternalProgramsWithArgs)
class Background1 (SimpleTest.Case):
  prog = "./mhcsh"
  stdin = "/usr/bin/zip -9 DELETE_THIS_FILE /boot/initrd.img &\n/usr/bin/echo -e \\x48\\x65LlO"

  def _check_output (self):
    self.assertEqual(self.e, "")
    self.assertIn("HeLlO", self.r)
    self.assertIn("deflated", self.r)
    h = self.r.find("HeLlO")
    d = self.r.find("deflated")
    self.assertLess(h, d, "Echo didn't happen before zip finished")


@skipIfFailed(ExternalProgramsWithArgs)
class Background2 (Background1):
  prog = "./mhcsh"
  stdin = "/usr/bin/zip -9 DELETE_THIS_FILE /boot/initrd.img &   \n/usr/bin/echo -e \\x48\\x65LlO"

  def _check_output (self):
    self.assertEqual(self.e, "")
    self.assertIn("HeLlO", self.r)
    self.assertIn("deflated", self.r)
    h = self.r.find("HeLlO")
    d = self.r.find("deflated")
    self.assertLess(h, d, "Echo didn't happen before zip finished")


@skipIfFailed(ExternalProgramsWithArgs)
class ValgrindTests (Valgrind.Case):
  args = ["./mhcsh"]
  stdin = "cd /proc\nls locks\npwd\nset foo bar\n\n\n\nls\nexit 0\nnot_a_command"
