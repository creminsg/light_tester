# -*- coding: utf-8 -*-
  
"""Main module."""

import urllib.request
import re

class LightTester:

    def __init__(self, N):
        self.N = int(N)
        self.lights = [[False]*N for i in range(N)]

    def parseFile(A):
        instructions = []
        if A.startswith('http'):
            response = urllib.request.urlopen(A)
            data = response.read().decode('utf-8')
            z = re.split('\n', data)
            for i in z:
                instructions.append(i)
            N = int(instructions.pop(0))
            lights = [[False]*N for i in range(N)]
            # trying to initiliase object so that the self.count works
            count = LightTester.apply(instructions, lights, N)
            return count
            
        elif A.startswith('10'):
            z = re.split('\n', A)
            for i in z:
                instructions.append(i)
            N = int(instructions.pop(0))
            lights = [[False]*N for i in range(N)]
            # trying to initiliase object so that the self.count works
            count = LightTester.apply(instructions, lights, N)
            return count
	
        else:
            # read from disk
            N, instructions = None, []
            with open(A,'r') as f:
                N = int(f.readline())
                for line in f.readline(): 
                    instructions.append(line)
            # main code goes here
            return N, instructions
        return
    
    def apply(instructions, lights, N):
        
        for line in instructions:
            cmd = 'Nothing'
            commandPattern = re.compile(".*turn on|turn off|switch")
            if commandPattern.search(line) == None:
                pass
            
            else:
                cmd = commandPattern.search(line).group(0)
                coordinates = [int(s) for s in re.findall(r'([+-]?\d+)',line)] 
                index = 0
                for i in coordinates:
                    coordinates[index] = max(0, i)
                    coordinates[index] = min(N - 1, coordinates[index])
                    index += 1    
                
                x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]

            if cmd == 'turn on':
                for i in range (y1,y2+1):
                    for j in range(x1,x2+1):
                        lights[i][j]=True

            elif cmd == 'turn off':
                for i in range (y1,y2+1):
                    for j in range(x1,x2+1):
                        lights[i][j]=False

            elif cmd == 'switch':
                for i in range (y1,y2+1):
                    for j in range(x1,x2+1):
                        if lights[i][j]==True:
                            lights[i][j]=False
                        else:
                            if lights[i][j]==False:
                                lights[i][j]=True
        count = 0
        for i in lights:
            for j in i:
                if j == True:
                    count += 1
        return count
