# შექმენით ფუნქცა რომელიც იღებს წინადადებას და აბრუნებ რამდენი სიტყვაა მასში.
def count_words(sentence):
    words = sentence.split()
    return len(words)
print(count_words("i love programing"))



# შექმენით ფუნქცია რომელიც მიიღებს რიცხვების სიას და დაბრუნებს მხოლოდ ლუწების ჯამს.
def even_sum(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
print(even_sum([1, 2, 3, 4, 5, 6]))

#  შექმენით ფუნქცია რომელიც აბრუნებს სიაში უმაღლეს რიცხვს.
def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number
print(find_max([5, 3, 9, 2, 8]))
