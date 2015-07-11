import numpy
import math
import linear
import util
import scipy.ndimage.filters

def kernel(shape, f):
	ar = numpy.empty(shape, dtype=numpy.complex)
	for i in numpy.ndindex(shape):
		ar[i] = f(*i)
	return ar

def map(f, kern):
	newkern = numpy.empty(kern.shape, dtype=numpy.complex)
	for i in numpy.ndindex(kern.shape):
		newkern[i] = f(kern[i])
	return newkern

def concatmap(fs, kern):
	fshape = fs.shape
	kshape = kern.shape
	newshape = util.tupleop(lambda x, y: x * y, fshape, kshape)
	newkern = numpy.zeros(newshape)
	for i in numpy.ndindex(kshape):
		x = kern[i]
		result = map(lambda f: f(x), fs)
		for j in numpy.ndindex(fshape):
			newi = util.tupleop(lambda ii, ij, fs: ij + ii * fs, i, j, fshape)
			newkern[newi] = result
	return newkern

def gaussian(mu, sigma, *v):
	A = 1 / (sigma * math.sqrt(2 * math.pi))
	tau = (2 * (sigma ** 2))
	shift = util.tupleop(lambda x, m: x - m, v, mu)
	t = sum(util.tupleop(lambda s: s * s.conjugate(), shift))
	return A * math.exp(- t / tau)

def transform(mat, *t):
	tex = (1,) + t
	vector = numpy.array([tex]).T
	return tuple(util.join((mat * vector).tolist()))

def convolve(image, kern):
	imgreal = reals(image)
	kernreal = reals(kern)
	imgimag = imags(image)
	kernimag = imags(kern)
	f = scipy.ndimage.filters.convolve
	outputreal = complexes(f(imgreal, kernreal) - f(imgimag, kernimag))
	outputimag = complexes(f(imgreal, kernimag) + f(imgimag, kernreal))*1j
	return outputreal + outputimag
	#return scipy.ndimage.filters.convolve(image, kern)

def correlate(image, kern):
	return scipy.ndimage.filters.correlate(image, kern)

def reals(kern):
	newkern = numpy.empty(kern.shape, dtype=float)
	for i in numpy.ndindex(kern.shape):
		newkern[i] = kern[i].real
	return newkern

def imags(kern):
	newkern = numpy.empty(kern.shape, dtype=float)
	for i in numpy.ndindex(kern.shape):
		newkern[i] = kern[i].imag
	return newkern

def complexes(kern):
	return numpy.array(kern, dtype=complex)