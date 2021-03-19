#!/usr/bin/env python

import os 
import sys

if len(sys.argv) != 2:
	print("Error: (usage) %s logfile" % sys.argv[0])
	print("exapmle, %s tests/data/2021-02-15T184534_log_event_oscillo.txt" % sys.argv[0])
	exit()

logfile = sys.argv[1]
print("input file: %s" % logfile)

outdir = os.path.splitext(os.path.basename(logfile))[0]
cmd = "rm -rf %s; mkdir -p %s" % (outdir,outdir)
print(cmd);os.system(cmd)

basename = outdir.split('_')[0]

event_data = '%s_evt.csv' % basename
oscil_data = '%s_osc.csv' % basename
hk_data = '%s_hk.csv' % basename

f_event_data = open('%s/%s' % (outdir,event_data),'w')
f_oscil_data = open('%s/%s' % (outdir,oscil_data),'w')
f_hk_data = open('%s/%s' % (outdir,hk_data),'w')

header = "unixtime,mode,peak,sum_rise,sum_tail,NaN\n"
f_event_data.write(header)

header = "unixtime,mode,adc_values,NaN\n"
f_oscil_data.write(header)

header = "unixtime,mode,adc_ch1,adc_ch2,a,hk_ch1,hk_ch2,hk_ch3,hk_ch4,hk_ch5,hk_ch6,hk_ch7,hk_ch8,NaN\n"
f_hk_data.write(header)

for line in open(logfile):
	print(line)
	cols = line.split(',')
	if 'P' in cols: # event data 
		print(cols)
		f_event_data.write(line)
	elif 'S' in cols: # oscilloscope mode
		print(cols)
		f_oscil_data.write(line)
	elif 'M' in cols: # oscilloscope mode
		print(cols)
		f_hk_data.write(line)

f_event_data.close()
f_oscil_data.close()
f_hk_data.close()


