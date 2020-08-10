HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
	"""Represent an intersection using the Cantor pairing function."""
	return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
	return w(inter) - avenue(inter)

def avenue(inter):
	return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
	"""Return the taxicab distance between two intersections.

	>>> times_square = intersection(46, 7)
	>>> ess_a_bagel = intersection(51, 3)
	>>> taxicab(times_square, ess_a_bagel)
	9
	>>> taxicab(ess_a_bagel, times_square)
	9
	"""
	"*** YOUR CODE HERE ***"
	return abs(street(a)-street(b)) + abs(avenue(a)-avenue(b))

def squares(s):
	"""Returns a new list containing square roots of the elements of the
	original list that are perfect squares.

	>>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
	>>> squares(seq)
	[7, 3, 1, 10]
	>>> seq = [500, 30]
	>>> squares(seq)
	[]
	"""
	"*** YOUR CODE HERE ***"
	return [int(i**0.5) for i in s if round(i ** 0.5) ** 2 == i ]

def g(n):
	"""Return the value of G(n), computed recursively.

	>>> g(1)
	1
	>>> g(2)
	2
	>>> g(3)
	3
	>>> g(4)
	10
	>>> g(5)
	22
	>>> from construct_check import check
	>>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
	True
	"""
	"*** YOUR CODE HERE ***"
	if n <= 3:
		return n
	else:
		return g(n-1) + 2*g(n-2) + 3*g(n-3)


def g_iter(n):
	"""Return the value of G(n), computed iteratively.

	>>> g_iter(1)
	1
	>>> g_iter(2)
	2
	>>> g_iter(3)
	3
	>>> g_iter(4)
	10
	>>> g_iter(5)
	22
	>>> from construct_check import check
	>>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
	True
	"""
	if n <= 3:
		return n
	else:
		g_n_1, g_n_2, g_n_3 = 3, 2, 1
		# always update the g_i until reach the final n
		for i in range(4,n+1):
			g_i = g_n_1 + 2*g_n_2 + 3*g_n_3
# 			update the g(n-1), g(n-2), g(n-3)
			g_n_1, g_n_2, g_n_3 = g_i, g_n_1, g_n_2
		return g_i
	"*** YOUR CODE HERE ***"

def pingpong(n):
	"""Return the nth element of the ping-pong sequence.

	>>> pingpong(7)
	7
	>>> pingpong(8)
	6
	>>> pingpong(15)
	1
	>>> pingpong(21)
	-1
	>>> pingpong(22)
	0
	>>> pingpong(30)
	6
	>>> pingpong(68)
	2
	>>> pingpong(69)
	1
	>>> pingpong(70)
	0
	>>> pingpong(71)
	1
	>>> pingpong(72)
	0
	>>> pingpong(100)
	2
	>>> from construct_check import check
	>>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
	True
	"""
	# define two helper function, the recursion start from the bottom
	# from 1 to n
	"*** YOUR CODE HERE ***"
	def positive(n, k, turn):
		if turn == n:
			return k
		else:
			if (k % 7 == 0) or has_seven(k):
				return negative(n, k-1, turn + 1)
			else:
				return positive(n, k+1, turn + 1)

	def negative(n, k, turn):
		if turn == n:
			return k
		else:
			if (k % 7 == 0) or has_seven(k):
				return positive(n, k+1, turn + 1)
			else:
				return negative(n, k-1, turn + 1)    	

	return positive(n, 1, 1)

def has_seven(k):
	"""Returns True if at least one of the digits of k is a 7, False otherwise.

	>>> has_seven(3)
	False
	>>> has_seven(7)
	True
	>>> has_seven(2734)
	True
	>>> has_seven(2634)
	False
	>>> has_seven(734)
	True
	>>> has_seven(7777)
	True
	"""
	if k % 10 == 7:
		return True
	elif k < 10:
		return False
	else:
		return has_seven(k // 10)

def count_change(amount):
	"""Return the number of ways to make change for amount.

	>>> count_change(7)
	6
	>>> count_change(10)
	14
	>>> count_change(20)
	60
	>>> count_change(100)
	9828
	"""
	options = [2**i for i in range(amount+1) if 2**i <= amount]
	options = sorted(options, reverse = True)
	length = len(options)

	# print(length)
	def helper(remains, i, options, length):
		# loop until reaching the smallest coin
		if i >= length :
			return 0
		# check the remains
		if remains == 0:
			return 1
		elif remains < 0:
			return 0
		# every amount can be expressed by with_i + without_i
		else:
			with_i = helper(remains - options[i], i, options, length)
			without_i = helper(remains, i+1, options, length)
			return with_i + without_i
#   use a helper function
	return helper(amount, 0, options, length)
	"*** YOUR CODE HERE ***"

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
	"""Return the value of an expression that computes factorial.

	>>> make_anonymous_factorial()(5)
	120
	>>> from construct_check import check
	>>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
	True
	"""
	# u need to use a helper function if your lambda statement does
	# not have a name
	# fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
	def recursive2(f, n):
		return f(f, n)

	def recursive(n):

		return recursive2((lambda rec, n: 1 if n == 1 else mul(n, rec(sub(n, 1)))), n)

	return recursive
