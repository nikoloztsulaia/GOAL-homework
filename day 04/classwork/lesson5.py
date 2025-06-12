# ხუთი ცვლადის შექმნა
name = "Niko"
age = 18
city = "Tbilisi"
favorite_hobby = "Coding"
favorite_food = "Pizza"

# წინადადების შექმნა ცვლადების გამოყენებით
sentence = "Hello, my name is " + name + ". I am " + str(age) + " years old and I live in " + city + ". My favorite hobby is " + favorite_hobby + ", and I love eating " + favorite_food + "."

# წინადადების დაბეჭდვა
print(sentence)



# მომხმარებლისგან მონაცემების მიღება
name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")

# შედეგის გამოტანა მითითებული ფორმატით
print("-სახელი: {" + name + "}-")
print("-გვარი: {" + surname + "}-")
print("-ასაკი: {" + age + "}-")
