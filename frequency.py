# Toy Reid
# CS494 - Bioinformatics
# Homework 1 #4: Compute frequencies of nucleotides in .fasta

from sys import argv
import string

# arg1 = file name


def printFreq(freqs):
    """ Prints the frequencies in a given frequency table """
    print "Nucleotide frequencies:"
    for key, value in freqs.items():
        if len(key) == 1:
            print "\t%s: %d/%d = %f" % (key, freqs[key], freqs['nTot'], freqs[key] / freqs['nTot'])
        if len(key) == 2:
            print "\t%s: %d/%d = %f" % (key, freqs[key], freqs['dTot'], freqs[key] / freqs['dTot'])


def countNuc(gen):
    """ Counts each nucleotide and dinucleotide in a genome gen """
    freqs = {
        'A': 0, 'T': 0, 'C': 0, 'G': 0,
        'nTot': 0, 'dTot': 0
    }

    for key, value in freqs.items():
        if len(key) == 1:
            freqs[key] = float(gen.count(key))
            freqs['nTot'] += freqs[key]
    for nuc in range(0, len(gen) - 1):
        temp = gen[nuc] + gen[nuc + 1]
        if temp not in freqs:
            freqs[temp] = 0
        freqs[temp] += float(1)
        freqs['dTot'] += float(1)
    return freqs


if __name__ == "__main__":
    genome = open(argv[1])
    genome.readline()  # Skip first line
    string = genome.read().replace('\n', '')
    frequencies = countNuc(string)
    printFreq(frequencies)
