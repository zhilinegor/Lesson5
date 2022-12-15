def any_digits(*digits):
    sum = 0
    print("\nВы ввели:",digits)
    for i in digits:
        sum += int(i)
    return sum

print("Cумма чисел:",any_digits(0, 1, 2))
print("Cумма чисел:",any_digits(0, 11, 22))
print("Cумма чисел:",any_digits(0, 11, 22, 44, 55, 0))