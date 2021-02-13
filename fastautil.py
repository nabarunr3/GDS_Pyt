
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

#which is our file, and try to open it
try:
	fasta_string = open(fasta_file, 'r')
except IOError:		#pass exception of cannot open
	print("File nonexistant")

#We define a function for storing the file in the dictionary
def fastadict(fastafile):
	"""
	This function reads a fasta file and stores in a dictionary

	"""
	fasta_dict = {}	#initializing empty dictionary
	for line in fastafile:
		line = line.rstrip()	#removing newline characters
		if line[0] == '>':	#first character of fasta header is '>'
			words = line.split()
			dict_key = words[0][1:]	#Assigning fasta identifier as dict_key.
			fasta_dict[dict_key] = ''	#initializing an empty string against the key
		else:	#i.e., when sequence, not header
			fasta_dict[dict_key] = fasta_dict[dict_key] + line
			"""The 'dict_key' key is used because key variable is
			already initialized with the previous header.
			A new header will automatically be initialized
			as a new key, because of the if codeblock."""

	print("\n%d sequences added from file.\n" %len(fasta_dict))
	return fasta_dict

"""
#Testing fastadict()

dict = fastadict(fasta_string)
for header, sequence in dict.items():
	print(header, sequence)
"""



#now the function to calculate lengths
def seqlength(fasta_dictionary):
	"""
	This function calculates the length of each item in the fasta file,
	and some trivia:
	1. Max Length.
	2. Number of and identifiers of sequences with max length.
	3. Min Length.
	4. Number of and identifiers of sequences with min length.

	"""
	"""First, find lengths"""
	lengths_dictionary = {}
	for key in fasta_dictionary:
		lengths_dictionary[key] = len(fasta_dictionary[key])

	#print lengths
	for header, lengths in lengths_dictionary.items():
		print(header, lengths)

	"""Next, print max length(s)"""
	#first we find the max sequence length
	max = 0
	for key in lengths_dictionary:
		if lengths_dictionary[key] > max:
			max = lengths_dictionary[key]

	#to account for >1 sequence with same max length we 
	#make a dictionary with identifiers of max length
	max_dictionary = {}
	for key in lengths_dictionary:
		if lengths_dictionary[key] == max:
			max_dictionary[key] = lengths_dictionary[key]

	#finally, print
	print("\n%d entry(s) with maximum length %d :\n" %(len(max_dictionary), max))
	for identifiers, lengths in max_dictionary.items():
		print(identifiers, lengths)

	"""Finally, print min length(s)"""
	#first we find the min sequence length
	min = max
	for key in lengths_dictionary:
		if lengths_dictionary[key] < min:
			min = lengths_dictionary[key]

	#to account for >1 sequence with same min length we 
	#make a dictionary with identifiers of min length
	min_dictionary = {}
	for key in lengths_dictionary: 
		if lengths_dictionary[key] == min:
			min_dictionary[key] = lengths_dictionary[key]

	#finally, print
	print("\n%d entry(s) with minimum length %d :\n" %(len(min_dictionary), min))
	for identifiers, lengths in min_dictionary.items():
		print(identifiers, lengths)

	return 0

#Testing seqlength()

seqlength(fastadict(fasta_string))
