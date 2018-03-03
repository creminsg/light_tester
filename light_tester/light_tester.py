# -*- coding: utf-8 -*-

"""Main module."""

import urllib.request
import re 

class LightTester:
    
    def __init__(self, N):
        N = int(N)
        self.lights = [[False]*N for i in range(N)] 
    
    def parseFile(A):
        instructions = []
        if A.startswith('http'):
            response = urllib.request.urlopen(A)
            data = response.read().decode('utf-8')
            z = re.split('\n', data)
            for i in z:
                instructions.append(i)
            N = instructions.pop(0)
            return N, instructions

        else:
            N, instructions = None, []
            with open(A,'r') as f:
                N = int(f.readline()) 
                for line in f.readline(): 
                        instructions.append(line)
                return N, instructions
        return 


