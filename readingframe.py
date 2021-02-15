
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


def orf_find(seq):
	framedict = {}
	start_codon = "ATG"
	stop_codon_tuple = ("TAA", "TAG", "TGA")

	for frame in range(2):	#frame will run 0,1,2
		seq_frame = seq[frame:]	#setting the start position
		start_positions = []
		framedict["frame" + str(frame + 1)] = [] 
		"""initializing the ORF list corresponding to the 
		frame of reference"""

		for index in len(seq[frame]):
			codon = seq_frame[index:(index + 3)]
			#going codon by codon

			if codon == start_codon:
				start_posistions.append(index + frame)

			if codon in stop_codon_tuple and start_pos != []:
				#we would want a start codon 
				#preceeding a stop codon
				stop_pos = index + frame

				for start_codon_positions in start_pos:
					framedict["frame" + str(frame + 1)].append(\
					[start_codon_pos, stop_pos, (stop_pos - start_codon_pos)])
					"""this should consider as ORFs the sequences
					between all start codons before the discovered stop codon"""

				start_pos = [] #empyting the start codon position buffer

			index = index + 3 #so that the window reads three bases at a time w/o overlap
	return framedict




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
		by_frame_ORF_list_dict[identifier] = {}
		by_seq_by_frame_ORF_list_dict = orf_find(fasta_dict[identifier])
		"""We're passing each sequence of the fasta file to the function
		orf_find which will return a dictionary containing the
		key-value pairs, where each key represents a reading frame..
		Each reading frame stores a list of all the ORFs."""

	return by_seq_by_frame_ORF_list_dict

def orf_compare(input_frame):
	"""
	This function takes in a complex nested ORF containing dictionary.
	It then compares the length of the ORF 
	"""

for i
