#  შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას, ფუნქციამ ამ წინადადების თითოეული სიტყვა უნდა შეინახოს სიაში, როგორც ცალკე ელემენტი. საბოლოოდ გადააქციეთ სია ისევ წინადადებად, სადაც სიტყვებს შორის არის მძიმე და ერთი დაშორება(", ")
def process_sentence(sentence):
    
    words = sentence.split()
    new_sentence = ", ".join(words)
    return new_sentence


input_text = "მე ვარ მკლავჭიდელი"
result = process_sentence(input_text)
print(result)


# შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)
def print_word_lengths(sentence):
    words = sentence.split()
    for word in words:
        print(word, "→", len(word))

input_text = "მე ვსწავლობ პროგრამირებას"
print_word_lengths(input_text)


#  შექმენით ფუნქცია, რომელიც იღებს წინადადებას, სადაც ყოველი სიტყვის შორის ერთზე მეტი დაშორებაა(space). თქვენი დავალებაა ჩამოაშოროთ გადმოცემულ წინადადებას ზედმეტი space-ები(სიტყვებს შორის მხოლოდ ერთი უნდა იყოს). საბოლოოდ დააბრუნეთ ეს წინადადება
def clean_spaces(sentence):
    words = sentence.split()
    cleaned_sentence = " ".join(words)
    return cleaned_sentence


input_text = "ეს   არის   წინადადება   ზედმეტი   space-ებით"
result = clean_spaces(input_text)
print(result)



#  შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას
def replace_spaces_with_dash(sentence):
    words = sentence.split()
    dashed_sentence = "-".join(words)
    return dashed_sentence

input_text = "ეს არის ტესტური წინადადება"
result = replace_spaces_with_dash(input_text)
print(result)


#  შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება. თქვენი დავალებაა ამ წინადადების სიტყვები შეაბრუნოთ და დააბრუნოთ(სიტყვების სიმბოლოები არ უნდა იყოს შებრუნებული) 
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    new_sentence = " ".join(reversed_words)
    return new_sentence

input_text = "მე ვსწავლობ პროგრამირებას"
result = reverse_words(input_text)
print(result)
