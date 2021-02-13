
#!/usr/bin/python3.8

"""
This module will show all the orfs and find the longest orf

"""
import fastautil

fastafile = sys.argv[1]

try:
	fasta_string = open(fastafile, 'r')

except IOError:
	print("File nonexistant")

def fileoriffind(fasta_string):
	"""
	This function displays all the orfs from a given fasta file
	and finds the longest orf

	"""
	fasta_dict = fastautil.fastadict(fasta_string)
	"""fasta_dict contains the identifier-sequence pairs from all 
	the sequences in the fasta file, as key-value pairs in a dictionary"""

def orifind(seq):
	rf1 = fasta_dict[identf][0:]
	rf2 = fasta_dict[identf][1:]
	rf3 = fasta_dict[identf][2:]

	rf = 0
		for rf in range(len(rf) - 1):
			codon = 



