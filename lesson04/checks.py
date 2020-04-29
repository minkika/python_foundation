from random import randint


def user_input(text, only_positives=True, limit=None):
    """
    asks for 1 input and converts it into integer or exit program

    arguments:
    text - what to write before input
    only_positives (True) - check that input is positive
    limit (None) - absolute of integer limitation

    Returns integer or exit programm
    This function after short instructions and text (arguments) cyclingly asks
    for input from user, while it is not possible to return after converting
    into integer. If user types 'q', the script finish itself
    """

    while True:
        uinput = input(f'For exit enter "q" \n{text}')
        if uinput == 'q':
            print('Quit')
            quit(0)
        else:
            try:
                uinput = int(uinput)
                if not limit or (limit and abs(uinput) < limit):
                    if only_positives:
                        if uinput > 0:
                            return uinput
                        else:
                            print('Input must be a positive number')
                    else:
                        return uinput
                elif limit and abs(uinput) > limit:
                    print(f'Try less than {limit}')
            except:
                print('Input must be a number')


def auto_list(length, lower=0, upper=100):
    # creates list of random integers from lower (arg) to upper (arg) with length (arg)
    return [randint(lower, upper) for i in range(length)]


def check_one_float(a):
    # checks if one argument is float or can be a float
    if a == 0 or a == 0.0:
        return True
    try:
        a = float(a)
    except:
        return False
    return True


def check_input(*args):
    # checks all arguments can be float
    if all(check_one_float(el) == True for el in args):
        return list(map(float, args))
    return False


def check_limits(low, high):
    if low > high:
        low, high = high, low
    return low, high
