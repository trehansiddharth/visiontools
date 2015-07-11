import numpy
import numpy.fft
from numpy.linalg import *

def fft(arr):
	return numpy.fft.fftn(arr)

def ifft(arr):
	return numpy.fft.ifftn(arr)

def matrix(arr):
	return numpy.matrix(arr)