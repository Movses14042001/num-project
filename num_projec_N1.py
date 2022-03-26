def getFactors(num):
    
    factors = []
    for i in range(num):
        i += 1
        if num % i == 0:
            factors.append(i)

    return factors

def isAbundant(num):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.
    """
    abundant_numbers = getFactors(num)
    for i in abundant_numbers:
        if num < sum(abundant_numbers) - num:
            return f'the number {num} is isAbundant'
    
print(isAbundant(12))
print(isAbundant.__doc__)
