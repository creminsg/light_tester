import sys
import re
sys.path.append('.')
from light_tester import *
import pytest
from click.testing import CliRunner

def testParseOnlineFile():
	file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
	N, instructions = light_tester.LightTester.parseFile(file)
	assert N is not None
	assert instructions is not None	

def testParseLocalFile():
        file = "./light_tester/data/input_assign3.txt"
        N, instructions = light_tester.LightTester.parseFile(file)
        assert N is not None
        assert instructions is not None

def testIgnoreInvalidCommands():
        N, instructions = light_tester.LightTester.parseFile("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
        totalCommandCount = 0
        validCommandCount = light_tester.LightTester.apply(instructions)
        for i in instructions:
                totalCommandCount += 1
        assert validCommandCount != totalCommandCount
