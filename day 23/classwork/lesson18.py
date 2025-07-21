#  მომხმარებელს შემოატანეთ ინფუთი სანამ პირველი და ბოლო ასო ინფუთის არ იქნება თანხმოვანი
vowels = "აეიოუ"

while True:
    word = input("შეიყვანე სიტყვა: ")
    if word[0] not in vowels and word[-1] not in vowels:
        print("სწორია. პირველი და ბოლო ასო თანხმოვანია ")
        break