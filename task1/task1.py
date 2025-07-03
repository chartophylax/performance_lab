def arr (index, n):
	return (index % n) + 1

def main_p():
    while True:
        size = input("Введите размер массива: ")
        if not size.isnumeric():
            print("Введённое значение не является числом.")
            continue  # Повторить итерацию

        number = input("Введите интервал: ")
        if not number.isnumeric():
            print("Введённое значение не является числом.")
            continue  # Повторить итерацию

        break	

    size = int(size)
    number = int(number)

#    res=0
#    j=0
#    ans=arr(j, size)

#    while True:
#        for i in range(number):
#            res=arr(j, size)
#            rint(res, j)
#            j = j + 1
#        print("")
#        if res==1:
#            break
#        j = j - 1
#        ans=ans*10 + res
#
#    print(ans)

    res=0
    j=0
    ans=arr(j, size)

    while True:
        j = j + number-1
        res = arr(j, size)
        if res==1:
            break
        ans=ans*10 + res

    print("Путь:", ans)



while True:
    main_p()
    answer = input("Для повторения программы введите да или yes: ").strip().lower()
    if answer not in ['да', 'yes', 'y', 'д']:
        print("Завершение работы программы.")
        break
