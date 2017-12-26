def add_numbers(*args):
    total = 0;
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3, 12)
add_numbers(3, 12, 5)