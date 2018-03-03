import sys
import re
sys.path.append('.')
from light_tester import *
import pytest
from click.testing import CliRunner



def testParseFile():
	file = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
	N, instructions = light_tester.LightTester.parseFile(file)
	assert N is not None
	assert instructions is not None	

#def test_length_parse():
#    data = "10\nturn on 8,-40 through the pixels 9,11"
#    z = re.split('\n', data)
#    tv_screen = LightTester(z[0])
#    assert tv_screen != None

#def TXest_ten_pixels():
#    data = "10\nturn on 8,-40 through the pixels 9,11"
#    z = re.split('\n', data)
#    for i in z:
#        if z.index(i) != 0:
#       		result = tv_screen.apply(i)
#	else:
#		pass		
#    assert result == 20 
