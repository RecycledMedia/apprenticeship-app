def predict_magic_number(number):
    calc = number + 1
    calc = calc * 2
    calc = calc + 4
    calc = calc / 2
    calc = calc - number
    return calc


def test_magic_number(number):
    if number < 1:
        print(f"{number} is not between 1 and 20")
    elif number > 20:
        print(f"{number} is not between 1 and 20")
    else:
        print(number, "->", predict_magic_number(number))


for the_number in range(-5, 25):
    test_magic_number(the_number)
