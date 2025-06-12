# 1) მომხმარებლისგან სახელი და ასაკის მიღება
name = input("შეიყვანეთ თქვენი სახელი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")
print("Name: " + name + ", Age: " + age)

# 2) სიგანის და სიმაღლის შეყვანა, ფართობის და პერიმეტრის გამოთვლა
width = float(input("შეიყვანეთ სიგანე: "))
height = float(input("შეიყვანეთ სიმაღლე: "))
area = width * height  # ფართობი (S)
perimeter = (width + height) * 2  # პერიმეტრი (P)
print("ფართობი: " + str(area) + ", პერიმეტრი: " + str(perimeter))

# 3) Input და Output ახსნა (კომენტარებით)
# input() - ფუნქცია, რომელიც მომხმარებლისგან იღებს მონაცემს.
# output (print) - ფუნქცია, რომელიც გამოტანს ინფორმაციას ტერმინალში.

# 4) მომხმარებლისგან ორი რიცხვის მიღება და მათემატიკური ოპერაციები
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

sum_result = num1 + num2  # მიმატება
sub_result = num1 - num2  # გამოკლება
mul_result = num1 * num2  # გამრავლება
div_result = num1 / num2  # გაყოფა

print("ჯამი: " + str(sum_result))
print("სხვაობა: " + str(sub_result))
print("ნამრავლი: " + str(mul_result))
print("განაყოფი: " + str(div_result))