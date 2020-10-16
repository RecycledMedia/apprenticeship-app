def predict_magic_number(number):
    calc = number + 1
    calc = calc * 2
    calc = calc + 4
    calc = calc / 2
    calc = calc - number
    return calc


def test_magic_number(number):
    print(number, "->", predict_magic_number(number))


number = 1
while number <= 20:
    test_magic_number(number)
    number = number + 1
