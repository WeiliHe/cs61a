""" Optional problems for Lab 6 """

## Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    index = 0
    def call_sq():

        nonlocal index, snacks
        output = snacks[index]
#       how to iterate through the sequence
        index = (index + 1) % len(snacks)
        return output

    return call_sq
    "*** YOUR CODE HERE ***"
