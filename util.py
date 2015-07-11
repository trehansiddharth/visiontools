def listop(f, *ls):
	return map(lambda l: f(*l), zip(*ls))

def tupleop(f, *ts):
	return tuple(map(lambda t: f(*t), zip(*ts)))

def curry(f, *argsf):
	def g(*argsg):
		return f(*(argsf + argsg))
	return g

def compose(f, g):
	def h(*x):
		o = g(*x)
		return f(*o)
	return h

def join(list):
	return reduce(lambda x, y: x + y, list, [])