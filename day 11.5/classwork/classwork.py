# ჩაწერე განსხვავებული მონაცემთა ტიპების (int, float, string, boolean) ცვლადები.
# int 
name = "nikolozi"
# float
num = 5.5
# string
num1 = 5
# boolean
num2 = 10
num3 = 20
print(num2 > num3)


# მომხმარებელს შემოატანინეთ მისი ასაკი და type() ფუნქციით შეამოწმეთ,თუ რა ტიპის მონაცემია შემოტანილი ასაკი.
age = 22
print(type(age))

#მომხმარებელს შემოატანინე მისი ასაკი და ბოლოს დაბეჭდე თუ რამდენი წლის იქნება ის 5 წლის შემდეგ
age = int(input("enter your age:"))
print(age * 5)

#მომხმარებელს შემოატანინეთ სახელი გვარი ასაკი სიმაღლე საყვარელი ფერი და გამოიტანეთ ეს ყველაფერი ერთ დიდ წინადადებაში.
name = input("tape your name:")
surname = input("enter your surname:")
age = input("entert your age:")
height = input("enter your height:")
collor = input("enter your faworite collor:")
print("your name is" " "  + name +  " "  + surname + " "  "you are" " " + age + " "  "years old" " " "your height is" " " + height + " " "your faworite collor is" " " + collor + "")