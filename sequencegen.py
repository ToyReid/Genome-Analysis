# Toy Reid
# CS494 - Bioinformatics
# Homework 1 #7: Generate a random .fasta genome trained on a genome with
# 	a Markov Model of a given order.

from sys import argv
from random import random
import probability

# arg1 = trainer genome, arg2 = output file name, arg3 = order, arg4 = length
LINE_LENGTH = 80

def generateFirst(freqTable, order):
	""" Calculate the first order nucleotides using a multinomial model """
	sequence = []
	A = freqTable['A']
	T = A + freqTable['T']
	C = T + freqTable['C']

	for i in range(0, order):
		num = random()
		if num < A:
			sequence.append('A')
		elif num >= A and num < T:
			sequence.append('T')
		elif num >= T and num < C:
			sequence.append('C')
		else:
			sequence.append('G')

	return sequence

def generateString(freqTable, order, length):
	""" Generate genome of given length using the Markov Model """
	sequence = generateFirst(freqTable, order)

	for i in range(0, length - order):
		tmp = "".join(sequence[i:i + order])
		A = freqTable[tmp + 'A']
		T = A + freqTable[tmp + 'T']
		C = T + freqTable[tmp + 'C']

		num = random()
		if num < A:
			sequence.append('A')
		elif num >= A and num < T:
			sequence.append('T')
		elif num >= T and num < C:
			sequence.append('C')
		else:
			sequence.append('G')

	s = "".join(sequence)
	return s

def printGenome(gen, outFile):
	""" Output the generated genome to a given file """
	for i in range(0, len(gen)):
		if i % LINE_LENGTH == 0:
			outFile.write("\n")
		outFile.write(gen[i])

if __name__ == "__main__":
	trainer = open(argv[1])
	out = open(argv[2], 'w+')
	inOrder = int(argv[3])
	inLength = int(argv[4])

	trainer.readline()
	trainString = trainer.read().replace('\n', '')
	trainString.replace('N', 'A')

	out.write(">Sequence of length %d trained on %s with order %d Markov Model" \
		% (inLength, trainer.name, inOrder))

	markFreqs = probability.makeMarkovTable(inOrder, trainString)
	genome = generateString(markFreqs, inOrder, inLength)
	printGenome(genome, out)
