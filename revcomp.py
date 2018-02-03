# Toy Reid
# CS494 - Bioinformatics
# Homework 1 #3: Reverse complement of a genome .fasta file

from sys import argv
import string

# arg1 = file name


def reverseString(s):
    """ Reverse a given string s """
    s.rstrip()  # Remove newline characters before reversing
    s = s[::-1]
    return s


def replaceNuc(line):
    """ Using a translation table, convert nucleotides to their base pair """
    inTab = "ATCG"
    outTab = "TAGC"
    tranTab = string.maketrans(inTab, outTab)
    return line.translate(tranTab)


def makeReverse(genome, reverse):
    """ Run through genome, complement, reverse, and output to .rev.fasta file """
    reverse.write(genome.readline())  # Add header lines
    reverse.write('>reversed')
    for line in genome:
        line = replaceNuc(line)
        revLine = reverseString(line)
        reverse.write(revLine)


genome = open(argv[1])
revName = genome.name[:-6] + '.rev.fasta'
reverse = open(revName, 'w+')

makeReverse(genome, reverse)
