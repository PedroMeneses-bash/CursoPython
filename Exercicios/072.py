countNumbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')


while True:

    number = int(input('Enter a number of 0 to 20: '))

    if number >= 0 and number <= 20:
        print(f'You entered the number {countNumbers[number]}.')
        break
    else:
        print('Please. ', end='')
