#  მომხმარებელს შემოატანინეთ თავისი გულის ცემა გააკეთეთ პატარა გულის ცემის სისტემა რომელიც ითვლის რა თქმა უნდა გულის ცემას  თუ 180 ზე მეტია ამ შემთხვევაში მაღალია თუ 160-დან 170 მდე არის ამ შემთვევაში არის ნორმალური თუ 160-ზე ნაკლებია ამ შემთხვევაში დაბალია 
# მომხმარებელი შეჰყავს გულის ცემის სიხშირე
heart_rate = int(input("შეიყვანეთ თქვენი გულისცემა (BPM): "))

# შეფასება
if heart_rate > 180:
    print("მაღალი გულისცემა!")
elif 160 <= heart_rate <= 170:
    print("ნორმალური გულისცემა!")
else:
    print("დაბალი გულისცემა!")

# შექმენი პროგრამა, რომელიც მომხმარებლის მიერ შეყვანილი ასაკის მიხედვით დაადგენს, რომელი ასაკობრივი ჯგუფის წევრია ადამიანი.
# თუ ასაკი უარყოფითია — გამოიტანე: "არასწორი ასაკი"
# თუ ასაკი ნაკლებია 13-ზე — გამოიტანე: "ბავშვი"
# თუ ასაკი არის 13-დან 19-ის ჩათვლით — გამოიტანე: "თინეიჯერი"
# თუ ასაკი არის 20-დან 59-ის ჩათვლით — გამოიტანე: "ზრდასრული"
# თუ ასაკი არის 60 ან მეტი — გამოიტანე: "პენსიონერი"
age = int(input("შეიყვანეთ თქვენი ასაკი: "))  # მომხმარებელი შეჰყავს ასაკს

if age < 0:
    print("არასწორი ასაკი")  # უარყოფითი რიცხვი არასწორია
elif age < 13:
    print("ბავშვი")  # 0-12 წელი
elif 13 <= age <= 19:
    print("თინეიჯერი")  # 13-19 წელი
elif 20 <= age <= 59:
    print("ზრდასრული")  # 20-59 წელი
else:
    print("პენსიონერი")  # 60 ან მეტი