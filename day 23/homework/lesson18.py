# შეიყვანე სიტყვა, სანამ მისი პირველი და ბოლო ასოები არ იქნებიან თანხმოვნები.


user_input = input("გთხოვთ შეიყვანოთ რაიმე სტრიქონი რომლის შემოწმება გსურთ: ")

x = "აეიოუ"

while True:
    if user_input[0] in x or user_input[-1] in x:
        user_input = input("არასწორია, გთხოვთ შეიყვანოთ სტრიქონი თავიდან: ")
    else:
        print(f"{user_input} სწორია, გმადლობთ.")
        break

# შეიყვანე 5 სიტყვა, მაგრამ შეინახე (დაახსოვრე) მხოლოდ ისინი, რომლებიც სწორია.


x = "აეიოუ"

correct_word_list = []

for i in range(5):
    user_input = input("გთხოვთ შეიყვანოთ რამე სიტყვა რანდომი სიის რედაქტორი და მითითება ტესტირებისათვის: ")
    print()
    if user_input[0] in x or user_input[-1] in x:
        print("არასწორია, სიტყვა შეიცავს")
        print()
    else:
        print("სწორია, სიტყვა არ შეიცავს არც ერთ დამთხვევას სიაში.")
        correct_word_list.append(user_input)
        print()

print(f"თქვენი სწორი სიტყვების სია: {correct_word_list}")



# რობოტმა უნდა დაითვალოს, რამდენჯერ სცადე სწორი სიტყვის შეყვანა.

user_input = input("გთხოვთ შეიყვანოთ ქართული სიტყვა რომლის პირველი და ბოლო ასოებია ქართული: ")
wrong_word_count = 0
x = "აეიოუ"

while True:
    if user_input[0] in x or user_input[-1] in x:
        user_input = input("სწორია, გთხოვთ შეიყვანოთ შემდეგი ქართული სიტყვა: ")
        wrong_word_count += 1
    else:
        print(f"{user_input} არასწორია, გმადლობთ.")
        print(f"არასწორი სიტყვების რაოდენობა არის: {wrong_word_count}")
        break


# შეიყვანე 10 სიტყვა, მაგრამ დაბეჭდოს (გამოაჩინოს) მხოლოდ სწორი სიტყვები.

x = "აეიოუ"

for i in range(10):
    user_input = input("შეიყვანეთ რაიმე სიმბოლო, რიცხვი ან სიტყვა და დააჭიროთ Enter-ს: ")
    if user_input[0] in x or user_input[-1] in x:
        print("თქვენს მიერ შეყვანილი სიმბოლო არასწორია!")
    else:
        print(user_input)
        print("გმადლობთ, თქვენ შეყვანეთ სწორი სიმბოლო!")


# შეიყვანე სიტყვა და რობოტმა უნდა დათვალოს რამდენი ხმოვანია და რამდენი თანხმოვანი აქვს მას.

user_input = input("გთხოვთ შეიყვანოთ სიტყვა 'რ'ით იწყება და 'ა'ით მთავრდება: ")

number_of_vowels = 0
number_of_consonants = 0

x = "აეიოუ"

while True:
    if user_input[0] in x or user_input[-1] in x:
        user_input = input("სწორედაა, გთხოვთ შეიყვანოთ სიტყვა თავიდან: ")
    else:
        print(f"{user_input} სიტყვა, გამოთვლილია.")
        for i in user_input:
            if i in x:
                number_of_vowels += 1
            else:
                number_of_consonants += 1
        print()
        print(f"ხმოვნების რაოდენობა: {number_of_vowels}")
        print(f"თანხმოვნების რაოდენობა: {number_of_consonants}")
        print()
        break
    