import sys
import re
sys.path.append('.')
from light_tester.ledSolve import *
import pytest
from click.testing import CliRunner

def testParseOnlineFile():
	file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
	count, instructions, lights, N = parseFile(file)
	assert N is not None
	assert instructions is not None	

def testParseLocalFile():
        file = "../../data/input_assign3.txt"
        count, instructions, lights, N = parseFile(file)
        assert N is not None
        assert instructions is not None

def testIgnoreInvalidCommands():
        count, instructions, lights, N = parseFile("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
        totalCommandCount = 0
        instructions, lights, N = apply(instructions)
        for i in instructions:
                totalCommandCount += 1
        assert validCommandCount != totalCommandCount

def testGridBoundary():
	count, instructions, lights, N = parseFile("10\nturn on -10,8 through 3,11")
	assert count == 8	
