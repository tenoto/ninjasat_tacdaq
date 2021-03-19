#!/usr/bin/env python

import os 
import sys
import pandas as pd 
import matplotlib.pyplot as plt


if len(sys.argv) != 2:
	print("Error: (usage) %s logfile" % sys.argv[0])
	print("exapmle, %s tests/data/2021-02-15T184534_log_event_oscillo.txt" % sys.argv[0])
	exit()

logfile = sys.argv[1]
print("input file: %s" % logfile)

outdir = os.path.splitext(os.path.basename(logfile))[0]
basename = outdir.split('_')[0]
event_data = '%s_evt.csv' % basename
oscil_data = '%s_osc.csv' % basename
hk_data = '%s_hk.csv' % basename

infile = '%s/%s' % (outdir,event_data)
df_evt = pd.read_csv(infile)
outpdf = os.path.splitext(infile)[0] + '.pdf'
fig = plt.figure()
plt.plot(df_evt['unixtime']-df_evt['unixtime'][0],df_evt['peak'])
plt.xlabel('unixtime')
plt.ylabel('peak')
plt.savefig(outpdf)
