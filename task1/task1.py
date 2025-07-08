import sys

if len(sys.argv) < 3:
    print("Ошибка: Нужно два паратаметра.")
    input("Нажмите Enter для выхода...")
    sys.exit()

def arr (index, n):
	return (index % n) + 1

size = sys.argv[1]
number = sys.argv[2]

missing1 = not size.isnumeric()
missing2 = not number.isnumeric()

if missing1 or missing2:
    if missing1 and missing2:
        print(f"Ошибка. {size} и {number} не являются целыми неотрицательными  числами.")
    elif missing1:
        print(f"Ошибка. {size} не является числом.")
    elif missing2:
        print(f"Ошибка. {number} не является числом.")
    input("Заверешние. Нажмите Enter для выхода...")
    sys.exit()

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
input("Заверешние. Нажмите Enter для выхода...")
