def isNarcissistic(num):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """
    

    narcissistic_number = str(num)
    narcissistic_number = (list(narcissistic_number))
    numbers_sum = []

    for i in narcissistic_number:
        assert_true = len(narcissistic_number)
        numbers_sum.append(int(i) ** assert_true)
        if sum(numbers_sum) == num:
            return f"the number {num} is isNarcissistic"
        else:
            return f"the number {num} isn\'t isNarcissistic"
            
    

             
print(isNarcissistic(8208))
print(isNarcissistic.__doc__)
