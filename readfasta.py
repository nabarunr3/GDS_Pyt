
#!/usr/bin/python3.8

"""
four tasks at hand:

1. read the fasta file in a dictionary and count the number of sequence records
2. Lengths of the sequences in a file returned as a dictionary. 
3. Identify all the ORFs of each sequence present in the FASTA file. 
	Also identify the identifier containing the longest ORF.
	For a given Identifier what is the longest ORF contained in that sequence?
	The starting position of the longest ORF?
4. Given a length n, identify all repeats of length n in all the sequneces in the file. 
	Also how many times each repeat occurs in the file. 
	Which is the most frequent repeat of a given length. 

"""

import sys

#now we will take the second argument of our command line input
fasta_file = sys.argv[1]

#try to open, read the file and store in a string
try:
	open(fasta_file)
except IOError:		#pass exception of cannot open
	print("File nonexistant")

#now we define a function for storing the file in the dictionary

def fastadict(fastafile):
	"""
	This function reads a fasta file and stores in a dictionary

	"""
	fasta_dict = {}	#initializing empty dictionary
	for line in fastafile:
		line = line.rstrip()	#removing newline characters
		if line[0] == '>':
			key = line
			"""Assigning the line as key. Depending on the header,
			individual words might also be assigned as headers
			by splitting the header using

			line.split(splitting character, default whitespace)

			This stores the word strings in a list."""

			fasta_dict[key] = ''
		else:	#sequence, not header
			fasta_dict[key] = fasta_dict[key] + line
			"""The 'key' key is used because key variable is
			already initialized with the previous header.
			A new header will automatically be initialized with
			as a new key, because of the if codeblock."""

	close(fastafile)
	return fasta_dict

dict = fastadict(fasta_file)
for header, sequence in dict.items():
	print(header, sequence)

