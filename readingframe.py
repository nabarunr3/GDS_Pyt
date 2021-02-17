
#!/usr/bin/python3.8

"""
This module will show the start and stop codons 
of all the orfs and find the longest orf

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
	finds all the orfs in all three reading frames.
	It returns a dictionary containing all the
	three frames. Each frame is a list which contains
	several ORF entries. An ORF entry is a nested list
	which enlists the start codon, the stop codon and the
	distance between the start and stop codons."""

	framedict = {}
	start_codon = "ATG"
	stop_codon_tuple = ("TAA", "TAG", "TGA")

	for frame in range(3):	#frame will run 0,1,2
		seq_frame = seq[frame:]	#setting start of reading position
#		print(seq_frame) #tests if correct frames are loaded in loop

		start_positions = []
		framedict["Frame" + str(frame + 1)] = []
		"""initializing the ORF entries list corresponding to the
		frame of reference"""
		
		index = 0
		for index in range (0, len(seq_frame), 3):
			"""so that the window reads three bases 
			at a time w/o overlap"""

			codon = seq_frame[index:(index + 3)]
			#going codon by codon
#			print(codon)	#tests if codons are being extracted properly

			if codon == start_codon:
				start_positions.append(index + frame)

			if codon in stop_codon_tuple and start_positions != []:
				"""we would want at least one start codon
				preceeding a stop codon"""
				stop_pos = index + frame

				for start_codon_pos in start_positions:
					framedict["Frame" + str(frame + 1)\
					].append([start_codon_pos, stop_pos])
					"""this should consider as ORFs the 
					sequences between each start codon
					before the discovered stop codon
					and, the stop codon"""

				start_positions = []
				"""empyting the start codon position 
				buffer to store new start positions"""

	return framedict

"""
#Test orf_find()
test_strings = ["ATGCATGTGGGGTAGCTGACGGGGGG",  
		"ATGCGGGGGGGTAGCGGGCGGGGGG",   
		"ATGGGGGGGGTAGCGGGCGGGGGG"]
framedict = orf_find(test_strings[0])
for frames,orfs in framedict.items():
	print(frames, orfs)
"""

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
		by_seq_by_frame_ORF_list_dict[identifier] \
		= orf_find(fasta_dict[identifier])
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
	->After each frame prints the longest ORF.
	->After each identifier entry prints the longest ORF and the 
	  corresponding frame considering all the frames.
	->At the end of the file prints the length of the longest 
	  ORF and the corresponding identifier in:
	a)Frame1 b)Frame2 c)Frame3 d)In all frames

	"""

	for seq_identifier in seq_dict:
		print(seq_identifier + "\n")
		#printing sequence identifier

		for frame in seq_dict[seq_identifier]:
			print(frame + "\n")
			#printing frame number

#			print(*seq_dict[seq_identifier][frame])
			intraframe_maxORF = 0
			intraframe_maxORF_positions = []
			for ORF_index in range(len(seq_dict[seq_identifier][frame])):

				ORF_length = seq_dict[seq_identifier][frame][ORF_index][1]\
						- seq_dict[seq_identifier][frame][ORF_index][0]

				if ORF_length > intraframe_maxORF:
					intraframe_maxORF = ORF_length
					intraframe_maxORF_positions\
					 = seq_dict[seq_identifier][frame][ORF_index]

				print(*seq_dict[seq_identifier][frame])
				print("The longest ORF is of length %d and has start and stop positions "\
					 + intraframe_maxORF_positions\
					%(intraframe_maxORF))

			print("\n")


#	for keys, values in seq_dict.items():
#		print(keys, values, "\n")

	return 0

orf_compare(fasta_ORFs(fasta_string))

