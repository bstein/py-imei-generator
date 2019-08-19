"""
Generates random IMEI numbers.

The user specifies the 8-digit TAC and up to 4-digits of the serial number.
The user also specifies the number of random IMEIs to generate.
"""

import sys
import random


# Src: https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/luhn.py
def checksum(number, alphabet='0123456789'):
    """
    Calculate the Luhn checksum over the provided number.

    The checksum is returned as an int.
    Valid numbers should have a checksum of 0.
    """
    n = len(alphabet)
    number = tuple(alphabet.index(i)
                   for i in reversed(str(number)))
    return (sum(number[::2]) +
            sum(sum(divmod(i * 2, n))
                for i in number[1::2])) % n


def calc_check_digit(number, alphabet='0123456789'):
    """Calculate the extra digit."""
    check_digit = checksum(number + alphabet[0])
    return alphabet[-check_digit]


def main():
    """Ask for the base IMEI, how many to generate, then generate them."""
    # Loop until the first 8-12 digits have been received & are valid
    start = ''
    while True:
        try:
            start = str(input('Enter the first 8 - 12 digits: ')).strip()
        except KeyboardInterrupt:
            print('')
            sys.exit()

        # If all conditions are met, the input is valid
        if start.isdigit() and len(start) >= 8 and len(start) <= 12:
            break

        # Tell the user why their input is invalid
        if not start.isdigit():
            print('*** Invalid input: you must enter digits only\n')
        elif len(start) <= 8:
            print('*** Invalid input: you must enter at least 8 digits\n')
        elif len(start) >= 12:
            print('*** Invalid input: you must enter no more than 12 digits\n')

    # Loop until we know how many random numbers to generate
    count = 0
    while True:
        try:
            count_input = str(
                input('Enter the number of IMEI numbers to generate: ')
                ).strip()
        except KeyboardInterrupt:
            print('')
            sys.exit()

        # If all conditions are met, the input is valid
        if count_input.isdigit() and int(count_input) > 0:
            count = int(count_input)
            break

        # Tell the user that they need to enter a number > 0
        print('*** Invalid input: you must enter a number greater than zero\n')

    # IMEIs will be generated based on the first 8 digits (TAC; the number
    #   used to identify the model) and the next 2-6 digits (partial serial #).
    #   The final, 15th digit, is the Luhn algorithm check digit.

    # Generate and print random IMEI numbers
    print('')

    for _ in range(count):
        imei = start

        # Randomly compute the remaining serial number digits
        while len(imei) < 14:
            imei += str(random.randint(0, 9))

        # Calculate the check digit with the Luhn algorithm
        imei += calc_check_digit(imei)
        print(imei)

    print('')


# Backwards compatibility (raw_input was renamed to input in Python 3.x)
try:
    # Using Python 2.x; calls to input will be treated as calls to raw_input
    input = raw_input
except NameError:
    # Using Python 3.x; no action required
    pass


if __name__ == '__main__':
    main()
