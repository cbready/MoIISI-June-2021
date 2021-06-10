"""
This was the homework for session 3.
"""

import os
import argparse

parser = argparse.ArgumentParser(description="The script opens a .mdout file and creates a .txt document with all the Etot values.")
parser.add_argument('mdout_file', help='The filepath of the mdout file to be analyzed.')
args = parser.parse_args()
file = args.mdout_file

outfile = open(file,'r')
data = outfile.readlines()
outfile.close()

filename = os.path.basename(file) #takes just name of the file from the filepath
filename = filename.split('.')[0]

datafile = open(F'{filename}_Etots.txt', 'w+')
for line in data:
    if 'Etot' in line:
        energy_line = line.split()
        datafile.write(F'{energy_line[0]} = {energy_line[2]} \n')
datafile.close()