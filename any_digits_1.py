def any_digits(digits):
    sum = 0
    print("\nВы ввели:",digits)
    for i in digits:
        sum += int(i)
    return sum

def inp_num(): # проверка ввода


    while True:
        
        try:
            num = int(input("\nВведите число: "))
            return num
            break
            
        except ValueError:
            print("\nВы должны ввести целое число, попробуйте снова.")

def str_digits():
    num_str = []      
    a = 1
    while a == 1:
        
        str_q = str(input("\nДля ввода числа нажмите +, для окончания любую клавишу: "))
        if str_q == '+':
            
            num_str.append(inp_num())
            continue
        
        else:
            return num_str
            break

new_digits_str = str_digits()
while True:
    if new_digits_str == []:
        print("\nВы ничего не ввели!")
        new_digits_str = str_digits()
    else:
        print("\nСумма чисел:",any_digits(new_digits_str))
        break
        
    


