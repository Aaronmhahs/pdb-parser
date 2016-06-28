#Author: Aaron Hahs
#Date: 6/28/16
#Version: 1.0

# Script used to parse inputted PDB files for molecular coordinates
import sys
import os
import datetime

# Set charge of bound ligand
LIG_CHARGE = 1

# Set system information
NUM_CORES = 8
MEMORY = 16

# Check for proper command line usage
if len(sys.argv) != 2:
	print "Error: invalid command line arguments."
	print "Usage: python Extractor.py [input file]"
	sys.exit(0)
	
# File header information
print "#! " + os.path.splitext(sys.argv[1])[0] + " after equilibration"
print "#! DFMP2 calculation"
print "#! Aaron Hahs " + datetime.date.today().strftime('%d, %b %Y') 
print "molecule " + os.path.splitext(sys.argv[1])[0] + "{"
print "0 1"
	
# File parser
InFile = open(sys.argv[1], 'r')
done = False
while not done:
	line = InFile.readline().split()
	if line[0] == "ATOM":
		print line[11] + line[6].rjust(16) + line[7].rjust(14) + line[8].rjust(14)
	if line[0] == "TER":
		print "--"
		print LIG_CHARGE, "1"
	if line[0] == "HETATM":
		print line[11] + line[6].rjust(16) + line[7].rjust(14) + line[8].rjust(14)
	if line[0] == "ENDMDL":
		done = True
InFile.close()
print ''

# File footer information
print "units angstrom"
print "no_reorient"
print "symmetry c1"
print "}\n\n"

print "set globals{"
print "basis jun-cc-pVDZ"
print "guess sad"
print "scf_type df"
print "}\n"

print "set freeze_core true\n"

print "memory " + MEMORY + " Gb\n"

print "set_num_threads(" + NUM_CORES + ")\n"

print "cp('dfmp2')"

