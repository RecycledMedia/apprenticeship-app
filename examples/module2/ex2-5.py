def predict_magic_number(number):
    calc = number + 1
    calc = calc * 2
    calc = calc + 4
    calc = calc / 2
    calc = calc - number
    return calc


def test_magic_number(number):
    print(number, "->", predict_magic_number(number))


for the_number in range(1, 21):
    test_magic_number(the_number)
