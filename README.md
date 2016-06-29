Project: pdb_parser v1.0

Authors: Aaronmhahs

Date: Jun 28, 2016

Description: pdb_parser is a python script which parses through inputted .pdb files for molecular dynamics information.

Requirements: 
- Python

Options:
- Set author of resulting file in pdb_parser.py line 11
- Set ligand charge in pdb_parser.py line 14 
- Set system information in pdb_parser.py lines 17-18  

Useage: "python pdb_parser.py [input file] > [output file]".

Arguments: 
- [input file] - .pdb file to be parsed for coordinates.
- [output file] - desired .in file name.  

Return:
- Text file containing molecular coordinate information.
	- file format ready for psi4 program.  
