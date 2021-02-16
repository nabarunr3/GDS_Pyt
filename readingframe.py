
#!/usr/bin/python3.8

"""
This module will show all the orfs and find the longest orf

"""
import fastautil

import sys

fastafile = sys.argv[1]

try:
	fasta_string = open(fastafile, 'r')

except IOError:
	print("File nonexistant")


def orf_find(seq):
	"""This function takes a DNA sequence and 
	finds all the orfs in all three reading frames. It returns a dictionary
	containing all the three frames. Each frame is a list which contains a several ORF 
	entries. An ORF entry is a nested list which enlists the start codon, the stop codon and the 
	distance between the start and stop codons."""

	framedict = {}
	start_codon = "ATG"
	stop_codon_tuple = ("TAA", "TAG", "TGA")

	for frame in range(3):	#frame will run 0,1,2
		seq_frame = seq[frame:]	#setting the start position
		start_positions = []
		framedict["frame" + str(frame + 1)] = [] 
		"""initializing the ORF entries list corresponding to the 
		frame of reference"""

		for index in range(len(seq_frame)):
			codon = seq_frame[index:(index + 3)]
			#going codon by codon

			if codon == start_codon:
				start_positions.append(index + frame)

			if codon in stop_codon_tuple and start_positions != []:
				#we would want a start codon 
				#preceeding a stop codon
				stop_pos = index + frame

				for start_codon_pos in start_positions:
					framedict["frame" + str(frame + 1)].append(\
					[start_codon_pos, stop_pos, (stop_pos - start_codon_pos)])
					"""this should consider as ORFs the sequences
					between each start codons before the discovered stop codon
					and the stop codon"""

				start_positions = [] #empyting the start codon position buffer to store new start positions

			index = index + 3 #so that the window reads three bases at a time w/o overlap
	return framedict

#Test orf_find()
test_strings = ["ATGCCGGGGGGGTAGCGGGCGGGGGG", "CATGCGGGGGGGTAGCGGGCGGGGGG", "CCATGGGGGGGGTAGCGGGCGGGGGG"]
framedict = orf_find(test_strings[0])
for frames,orfs in framedict.items():
	print(frames, orfs)


def fasta_ORFs(fasta_string):
	"""
	This function displays the positions of all the orfs from 
	all three reading frames from all the sequences 
	of a given fasta file

	"""
	fasta_dict = fastautil.fastadict(fasta_string)
	"""fasta_dict contains the identifier-sequence pairs from all 
	the sequences in the fasta file, as key-value pairs in a dictionary"""

	by_seq_by_frame_ORF_list_dict = {}
	"""this is a dictionary where each key-value pair represents 
	the identifier of a sequence in the fasta file and a corresponding 
	*nested dictionary*. This *nested dictionary* contains 3key-value 
	pairs, where the keys are three reading frames, and each reading 
	frame corresponds to a *list* containing more *nested lists*,
	each containing the following:
	[start_position, stop_position, ORF length]"""  

	for identifier in fasta_dict:
		by_seq_by_frame_ORF_list_dict[identifier] = {}
		by_seq_by_frame_ORF_list_dict[identifier] = orf_find(fasta_dict[identifier])
		"""We're passing each sequence of the fasta file to the function
		orf_find which will return a dictionary containing the
		key-value pairs, where each key represents a reading frame..
		Each reading frame stores a list of all the ORFs."""

	return by_seq_by_frame_ORF_list_dict

def orf_compare(seq_dict):
	"""
	This function takes in a complex nested ORF containing dictionary,
	created from a fasta file.
	It then compares the length of the ORFs in all sequences of the file. 
	"""

	for seq_identifier in seq_dict:
		print(seq_identifier + "\n")

		for frame in seq_dict[seq_identifier]:
			print(frame + "\n")

			print(*seq_dict[seq_identifier][frame])

#				for parameters in range(len(seq_dict[seq_identifier][frame][ORF_index]) - 1):
#					print()

			print("\n")


#	for keys, values in seq_dict.items():
#		print(keys, values, "\n")

	return 0

#orf_compare(fasta_ORFs(fasta_string))

