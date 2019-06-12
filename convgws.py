#ToDo: Currently the view option only puts the text in the .gws header. It does NOT do conversion of the order of the points. If you pass it XYZIJK but say it's YZ(X), it won't make it YZXIJK. Similarly, if you pass it a .gws that is in YZ(X), it will not convert it to XYZIJK.

import argparse
import os

parser = argparse.ArgumentParser(description='Translate point cloud into .gws file for mCosmos or vice versa')
parser.add_argument('indir', type = str, help = 'input file path')
parser.add_argument('--outdir', type = str, default = '', help = 'output file path (default: inputfile.outtype)')
views = ['1:XY(Z)','2:YZ(X)','3:ZX(Y)']
viewhelp = 'Orientation (' + views[0] + ') ' + views[1] + ' ' + views[2]
parser.add_argument('--view', type = int, default = 1, help = viewhelp, choices = [1,2,3])

args = parser.parse_args()

#break indir out to path and file name. Create tmpfile path. Get file type from file name.
inpath = args.indir.rsplit(sep = '\\', maxsplit = 1)[0]
inname = args.indir.split(sep = '\\')[-1]
tmpdir = inpath + '/' + inname + '.tmp'
filetype = inname.rsplit(sep = '.', maxsplit = 1)[1]

#either it's currently a .gws, or anything else (doesn't matter). Set file type for out file.
if filetype == 'gws':
	outtype = '.txt'
else:
	outtype = '.gws'

#If outdir not specified, tack file out type onto the end of file name and save in same dir.
if args.outdir == '':
	outdir = inpath + '/' + inname + outtype
else:
	outdir = args.outdir

infile = open(args.indir, 'r', encoding = 'UTF-8')
tmpfile = open(tmpdir, 'w')

#Write gws header info. None of it matters generally except we do need to set the correct viewplane.
if outtype == '.gws':
	tmpfile.write('#00:GEOPAK-WIN Scanning\n' + '#04:' + views[args.view - 1][2:] + '\n#05:Opn\n#06:MM\n')

#Loop through in file, either adding #12: for .gws, or skip the header lines and strip the #12:,
#then write to temp file
a = 0
while a == 0:
	line = infile.readline()
	
	if line == '':
		a = 1
	else:
		if outtype == '.gws':
			tmpfile.write('#12: ' + line)
		elif line.split(maxsplit = 1)[0] == '#12:':
			tmpfile.write(line.split(maxsplit = 1)[1])

infile.close()
tmpfile.close()

#Try to rename temp file to output file. If can't, still has made the temp file you can go to get it.
try:
	os.rename(tmpdir,outdir)
except:
	print('File could not be renamed. Look for .tmp file with the input file.')

print('done')
	