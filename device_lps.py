#!/usr/bin/python

import datetime
import os
import re
import fileinput
import sys

print "Average LPS will be printed to the screen and can also be found at the bottom of the samples file with today's date."

infile = open('device_lps.txt', 'r')
outfile = open('samples.log', 'w+')
samples = []

# Adding a sample comment.


for line in infile:
	if "incoming" in line:
		curr_sample = line[30:50]
		curr_sample = ''.join(curr_sample.split())
		curr_sample = curr_sample[:-4]
		samples.append(int(curr_sample))
		outfile.write(curr_sample)
		outfile.write('\n')

total_of_samples = sum(samples)
num_of_samples = len(samples)



if num_of_samples == 0:
	print "Wasn't able to obtain any samples"
	sys.exit()
else:
	avg_lps = total_of_samples / num_of_samples

print "Averate LPS is %i" % avg_lps
outfile.write("Average LPS is: ")
outfile.write(str(avg_lps))

outfile.close()
