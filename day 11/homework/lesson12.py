#  შემოაყვანინეთ მომხმარებელს n რიცხვი და დაპრინტეთ ყველა რიცხვი ნოლიდან n+1-მდე
n = int(input("შეიყვანეთ რიცხვი: "))  # მომხმარებელი შეჰყავს რიცხვი

for i in range(0, n + 1):  # ციკლი 0-დან n+1-მდე
    print(i)

# მომხმარებელს სთხოვე შეიყვანოს თავისი ასაკი და მიუთითოს, აქვს თუ არა სტუდენტური ბარათი.
# შემდეგ:
# თუ ასაკი ნაკლებია 18-ზე ან სტუდენტური ბარათი აქვს → დაბეჭდე "დანაზოგი გაქვს!"
# თუ ასაკი 60 ან მეტია და არ აქვს ბარათი → დაბეჭდე "პენსიონერის ფასდაკლება გაქვს!"
# სხვა შემთხვევაში → "ფასდაკლება არ გეკუთვნის."
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
student_card = input("გაქვს სტუდენტური ბარათი? (დიახ/არა): ").strip().lower()

if age < 18 or student_card == "დიახ":
    print("დანაზოგი გაქვს!")
elif age >= 60 and student_card != "დიახ":
    print("პენსიონერის ფასდაკლება გაქვს!")
else:
    print("ფასდაკლება არ გეკუთვნის.")


#  მომხმარებელს სთხოვე შეიყვანოს ორი რიცხვი. შემდეგ:
# თუ ორივე რიცხვი დადებითია → დაბეჭდე "ორივე დადებითია"
# თუ მხოლოდ ერთი დადებითია → "მხოლოდ ერთი დადებითი რიცხვია"
# თუ არცერთი არ არის დადებითი → "არცერთი არ არის დადებითი"
num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > 0 and num2 > 0:
    print("ორივე დადებითია")
elif num1 > 0 or num2 > 0:
    print("მხოლოდ ერთი დადებითი რიცხვია")
else:
    print("არცერთი არ არის დადებითი")

#  მომხმარებელი შეიყვანს ორ რიცხვს და ოპერაციას (+, -, *, /)
# დაბეჭდე შედეგი შესაბამისი მოქმედებით.
# თუ ოპერაცია არასწორია (მაგ 0-ს გაყოფა ან ტექსტი ან უცხო სიმბოლო) → "არასწორი ოპერაცია!"
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
operation = input("შეიყვანეთ ოპერაცია (+, -, *, /): ").strip()

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("არასწორი ოპერაცია!")
else:
    print("არასწორი ოპერაცია!")



#  შეამოწმეთ რესურსებში ჩაგდებული სურათი და მის მიხედვით დაწერეთ კომენტარებად ან პრეზენტაციაში მოქმედედების თანმიმდევრობა და საბოლოო პასუხი, ასევე როგორც ნამდვილი პითონის კოდი (შექმენით a,b,c ცვლადები, შექმენით result_0, result_1, result_2 ცვლადები და შეინახეთ თითოეულში შესაბამისი მნიშვნელობა და გამოპრინტეთ)



