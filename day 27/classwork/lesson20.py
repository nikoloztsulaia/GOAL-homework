# მომხმარებელს შემოატანინეთ სიტყვა, თუ ამ სიტყვის სიგრძე არის 5-ზე მეტი, მაშინ გამოვიტანოთ ყველა ასო, პატარა შრიფტით, თუ არადა დიდით.
word = input("შემოატანე სიტყვა: ")

if len(word) > 5:
    print(word.lower())
else:
    print(word.upper())





# შექმენით ფუნქცია რომელიც არგუმენტად იღებს სიტყვას/წინადადებას და ასოს, ის აბრუნებს პირველი სად შეხვდა ასო ამ სიტყვაში
def find_letter_position(text, letter):
    return text.find(letter)
print(find_letter_position("გამარჯობა", "ა"))
    



# შექმენით ერთი ვოიდ ფუნქცია და ერთი ფუნქცია რომელიც აბრუნებს სტრინგს.
# void
def greet_user(name):
    print("სალამი" + name )
greet_user ("niko")

# str
def make_greeting(name):
    return "სალამი" + name
    message = make_greeting("ნიკო")
print(message)
