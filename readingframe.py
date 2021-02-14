
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

def file_orf_find(fasta_string):
	"""
	This function displays all the orfs from a given fasta file
	and finds the longest orf

	"""
	fasta_dict = fastautil.fastadict(fasta_string)
	"""fasta_dict contains the identifier-sequence pairs from all 
	the sequences in the fasta file, as key-value pairs in a dictionary"""

def orf_find(seq):
	framedict = {}

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


