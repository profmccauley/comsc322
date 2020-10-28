#!/usr/bin/env python3

import unittest
import subprocess
import os
import tempfile

from test_common import run, Valgrind, SimpleTest


class UniqTooFewArgs (SimpleTest.Case):
  prog = "./uniq_ints"
  args = ()
  expect_fail = True

class UniqTooManyArgs (SimpleTest.Case):
  prog = "./uniq_ints"
  args = (1,2,3)
  expect_fail = True


# Generate some data
uniq_data = [5,6,2,1,1,1,1,2,3,4,100,1000,0x7fFFffFe,9,9,9,9,0x7fFFffFe]
uniq_result = []
for x in uniq_data:
  if x not in uniq_result: uniq_result.append(x)
uniq_result = "\n".join(str(x) for x in uniq_result)

tmp = tempfile.NamedTemporaryFile(mode="w")
tmp.write("\n".join(str(x) for x in uniq_data))
tmp.flush()


class UniqKnownResult (SimpleTest.Case):
  prog = "./uniq_ints"
  args = (tmp.name,)
  expect = uniq_result


class UniqMemoryTests (Valgrind.Case):
  args = ["./uniq_ints", tmp.name]


if __name__ == "__main__":
  unittest.main()
