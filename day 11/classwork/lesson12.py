# მომხმარებელს შემოატანინეთ 3 რიცხვი და გამოიტანეთ მაგ სამი რიცხვის ჯამი 
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
num3 = int(input("enter num3:"))
print (num1+num2+num3)


# დაბეჭდეთ რიცხვები 10 - 1 მდე 
for i in range(10, 0, -1):
    print(i)

# დაბეჭდეთ 1- 100 რიცხვი მხოლოდ კენტები 
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# დაბეჭდეთ ყველა რიცხვი რომელიც 3 ზე უნაშთოდ იყოფა 1- 100
for i in range(1, 101):
    if i % 3 == 0:
        print(i)



# იპოვეთ 1 - 100 რიცხვის ჯამი 
total = 0
for i in range(1, 101):
    total += i
print(total)
