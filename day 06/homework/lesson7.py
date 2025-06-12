
# - კომენტარებით ახსენით რა არის sequences, iteration და selection. მოიყვანეთ მათი მაგალითები


# **Sequences** (მიმდევრობა) - ეს არის ბრძანებების რიგი, რომლებიც შესრულდება თავიანთი დაწერის რიგით.
print("Hello")  # პირველი ბრძანება
print("World")  # მეორე ბრძანება

# **Iteration** (გამეორება) - ეს არის ციკლი, რომელიც ერთსა და იმავე მოქმედებას რამდენჯერმე ასრულებს.
for i in range(5):  # 5-ჯერ ბეჭდავს "Repeat"
    print("Repeat")

# **Selection** (არჩევანი) - ეს არის კოდის ნაწილი, რომელიც გარკვეულ პირობაზეა დამოკიდებული.
num = 10
if num > 5:  # თუ num მეტია 5-ზე, გამოიტანს შემდეგს
    print("Number is greater than 5")
else:
    print("Number is 5 or less")


    # - კომენტარებით ახსენით, რა არის ალგორითმი და ჩამოთვალეთ რა გზები არსებობს მის წარმოსადგენად.
# **ალგორითმი** - ეს არის მოქმედებების თანმიმდევრობა, რომელიც გამოიყენება კონკრეტული ამოცანის გადასაჭრელად.
# ალგორითმი განსაზღვრავს, როგორ უნდა შესრულდეს პრობლემის გადაჭრა ყველაზე ოპტიმალურად.

# **ალგორითმის ძირითადი მახასიათებლები:**
# 1. **სიზუსტე (Definiteness)** - ყოველი ნაბიჯი მკაფიოდ განსაზღვრულია.
# 2. **შეყვანა (Input)** - ალგორითმს შეიძლება ჰქონდეს ერთი ან რამდენიმე შეყვანის მონაცემი.
# 3. **გამოსავალი (Output)** - ალგორითმი საბოლოოდ უზრუნველყოფს გარკვეულ შედეგს.
# 4. **დასრულებადობა (Finiteness)** - ალგორითმი უნდა მთავრდებოდეს განსაზღვრული რაოდენობის ნაბიჯებში.
# 5. **ეფექტურობა (Efficiency)** - ალგორითმი უნდა იყოს ოპტიმალური და სწრაფი.


# - შეეცადეთ თქვენით მიხვდეთ, თუ რა პასუხს გამოიტანს შემდეგი კოდი:
# print(True or False and False or True and False or False and False or False and True and False or True) print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)
# პირველ რიგში დაუყევით and ლოგიკურ ოპერატორებს, შემდეგ კი დარჩენილ or ოპერატორებს
print(True or False and False or True and False or False and False or False and True and False or True)
# ლოგიკურ ოპერატორებს ვუყურებთ შემდეგნაირად:
# ჯერ **and** ოპერატორებს ვამუშავებთ: (False and False = False), (True and False = False), (True and False = False)
# შემდეგ **or** ოპერატორებით: (True or False = True), (True or False = True), (False or True = True)
# საბოლოოდ პასუხი იქნება: **True**

print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)
# ფარდობითი ოპერატორებით გამოთვლა:
# 7 * 7 / 7 == 7 → True, "1234" != "1234" → False, 7 + 3 * 3 + 1 == 15 → True, 100 > 100 → False
# **and** ოპერატორებით → (True and False = False), (True and True = True)
# **or** ოპერატორებით → (False or True = True), (True or False = True)
# საბოლოო პასუხი: **True**

# - მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True

num = int(input("შეიყვანეთ რიცხვი: "))

# ლუწია და 10-ზე მეტია, ან ტოლია 7-ის?
print((num % 2 == 0 and num > 10) or (num == 7))



# - ივარჯიშეთ შემდეგ ფუნქციებზე: int, str, float, bool. თითოეულზე გააკეთეთ 3-3 მაგალითი

# **int** - მთელ რიცხვებად გარდაქმნა
print(int("5") + 3)  # 8
print(int(4.7))  # 4
print(int(False))  # 0

# **str** - ტექსტად გარდაქმნა
print(str(123))  # "123"
print(str(True))  # "True"
print(str(4.56))  # "4.56"

# **float** - ათწილადებად გარდაქმნა
print(float("3.14") * 2)  # 6.28
print(float(7))  # 7.0
print(float(False))  # 0.0

# **bool** - ბულის მნიშვნელობებად გარდაქმნა
print(bool(0))  # False
print(bool(""))  # False
print(bool("Hello"))  # True



# - მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ, თუ ის არის ნაკიანი დაბეჭდეთ "This is leap year".(ნაკიანი წელიწადი იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე)
year = int(input("შეიყვანეთ წელი: "))

# ნაკიანი წელიწადის შემოწმება
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is leap year")
else:
    print("This is not a leap year")