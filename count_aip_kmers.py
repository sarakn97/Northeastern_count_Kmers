#!/usr/bin/env python

import re

#set Path to fastq file to read
fastq_file = '/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq'

#initialize variable to place sequence
seq = ''

#set kmer length
kmer_length = 6

#Initialize kmer dictionary
kmer_dictionary = {}


#open file & add kmers from each sequence (seq) to kmer dictionary
with open(fastq_file, 'r') as fastq_seq:
    for line in fastq_seq:
        line = line.rstrip()
        if re.match('^[ATGCN]+$', line):
            seq += line
            #set stop to length of sequence
            stop = len(seq) - kmer_length + 1
            for start in range(0, stop):
                kmer = seq[start:start + kmer_length]

                if kmer in kmer_dictionary:
                    #If kmer is already in dictionary, add 1 to count
                    kmer_dictionary[kmer] += 1
                else:
                    #If kmer is not in dictionary, add the kmer to dictionary with count = 1
                    kmer_dictionary[kmer] = 1
        #clear the sequence variable to add next sequence          
        seq = ''

        
#Set variable for tab seperation
sep = "\t"

#Open output file for writing
filename = "aip_kmers.txt"
with open(filename, 'w') as out:
    for kmer in kmer_dictionary:
        count = kmer_dictionary[kmer]
        output = (kmer, str(count))
        #format output to kmer + tab + count + newline
        out.write(sep.join(output) + "\n")
       
