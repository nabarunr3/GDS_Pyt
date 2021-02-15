
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

def fasta_ORFs(fasta_string):
	"""
	This function displays the positions of all the orfs from 
	all three reading frames from all the sequences 
	of a given fasta file

	"""
	fasta_dict = fastautil.fastadict(fasta_string)
	"""fasta_dict contains the identifier-sequence pairs from all 
	the sequences in the fasta file, as key-value pairs in a dictionary"""

	by_frame_ORF_list_dict = {}
	"""this is a dictionary where each key-value pair corresponds to 
	the identifier of a sequence in the fasta file and a corresponding 
	*nested dictionary*. This *nested dictionary* contains 3key-value 
	pairs, where the keys are three reading frames, and each reading 
	frame corresponds to a *list* containing all the valid ORF lengths."""  

	for identifier in fasta_dict:
		by_frame_ORF_list_dict[identifier] = {}
		by_seq_by_frame_ORF_list_dict = orf_find(fasta_dict[identifier])
		"""We're passing each sequence of the fasta file to the function
		orf_find which will return a dictionary containing the
		key-value pairs, where each key represents a reading frame..
		Each reading frame stores a list of all the ORFs."""

`	return by_seq_by_frame_ORF_list_dict

def orf_find(seq):
	framedict = {}
	ORF_list = []
	stop_codon_tuple = ("TAA", "TAG", "TGA")
	for frame in range(2):
		seq_frame = seq[frame:]
		start_pos = [None]
		start_codon_count = 0
		framedict["frame" + str(frame + 1)] = []
		for index in len(seq[frame]):
			codon = seq_frame[index:(index + 3)]
			if codon == "ATG":
				start_codon_count = start_codon_count + 1
				start_pos[start_codon_count]  = index + frame
			if codon in stop_tuple and start_pos != [None]:
				framelist["frame" + str(frame + 1) = 
				


	"""
	#extract strings of all 3 frames of reference
	frame_no = 1
	for frame_no in range(3):
		framedict["rf" + str(frame_no)] = seq[i:]

	#eliminate trailing letters which arent multiples of 3
	for frame in framedict:
		seq_trimmed_end = len(framedict[frame]) - (len(framedict[frame])%3)
		framedict[frame] = framedict[frame][:seq_trimmed_end]

	#calculating the lengths of the ORFs
	stop_codon_tuple = ("TAA", "TAG", "TGA")
	orf_len = {}
	frame_no = 1
	for frame in framedict:
		for index in len(framedict[frame]):
			codon = framedict[frame][index:index + 3]
			if codon == "ATG":
				orf_start = index + frame_no
			else if codon in stop_codon_tuple:
				orf_stop = index + frame_no
			
			orf_len[frame]  = orf_stop - orf_start
			
			index = index + 3
		frame_no = frame_no + 1
		"""

