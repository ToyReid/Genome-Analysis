# Toy Reid
# CS494 - Bioinformatics
# Homework 1 #6: Compute multinomial and markov order x of a sequence
# 	trained on another given sequence.

from sys import argv
from math import log
import frequency

# arg1 = tester genome; arg2 = trainer genome; arg3 = order

def multinomial(gen, train):
	""" Computes the multinomial probability of a genome given a trainer """
	freqs = frequency.countNuc(train)
	totalProb = 1
	genProb = 0

	for key in freqs:
		if len(key) == 1:
			totalProb *= freqs[key] / freqs['nTot']

	for char in gen:
		genProb += log(freqs[char] / freqs['nTot'])
	return genProb


def makeMarkovTable(order, train):
	""" Makes a table containing Markov probabilities of each sequence preceded
		by an orderer length string of nucleotides based on a trainer genome """
	freqTable = {}
	temp = [None] * (order + 1)

	for i in range(0, len(train) - order):
		temp[0:order + 1] = train[i:i + order + 1]
		string = "".join(temp)
		if train[i] not in freqTable:
			freqTable[train[i]] = 0
		freqTable[train[i]] += 1
		if string not in freqTable:
			freqTable[string] = 0
		freqTable[string] += 1
		if string[0:order] not in freqTable:
			freqTable[string[0:order]] = 0
		freqTable[string[0:order]] += 1

	for i in range(len(train) - order, len(train)):
		if train[i] not in freqTable:
			freqTable[train[i]] = 0
		freqTable[train[i]] += 1

	for key in freqTable:
		if len(key) == 1:
			freqTable[key] = float(freqTable[key]) / len(train)
		elif len(key) == 4:
			freqTable[key] = float(freqTable[key]) / \
				float(freqTable[key[0:order]])

	return freqTable


def markovProb(freqTable, order, gen):
	""" Uses a table of Markov probabilities to determine the probability
		of a given genome """
	prob = 0
	temp = [None] * (order + 1)

	for i in range(0, order):
		prob += log(freqTable[gen[i]])

	for i in range(0, len(gen) - order):
		temp[0:order + 1] = gen[i:i + order + 1]
		string = "".join(temp)
		prob += log(freqTable[string])

	return prob


if __name__ == "__main__":
	genome = open(argv[1])
	trainer = open(argv[2])
	inOrder = int(argv[3])

	genome.readline()  # Skip first line
	genoString = genome.read().replace('\n', '')
	genoString.replace('N', 'A')
	trainer.readline()
	trainString = trainer.read().replace('\n', '')
	trainString.replace('N', 'A')

	multiProb = multinomial(genoString, trainString)
	markFreqs = makeMarkovTable(inOrder, trainString)

	markProb = markovProb(markFreqs, inOrder, genoString)

	print "Multinomial Probability = %f" % multiProb
	print "Markov Probability = %f" % markProb
