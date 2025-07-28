#  შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, გამოიყენეთ slicing-ი
def middle_elements(lst):
    return lst[1:-1]
print(middle_elements(['a', 'b', 'c', 'd'])) 


#  შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ
def multiply_sums(list1, list2):
    sum1 = 0
    for num in list1:
        sum1 += num

    sum2 = 0
    for num in list2:
        sum2 += num

    return sum1 * sum2
print(multiply_sums([1, 2, 3], [4, 5]))




#  შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია
def double_numbers(lst):
    doubled = []
    i = 0
    while i < len(lst):
        doubled.append(lst[i] * 2)
        i += 1
    return doubled
print(double_numbers([1, 3, 5])) 


# შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია
def even_numbers(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens
print(even_numbers([1, 2, 3, 4, 5, 6])) 



#  შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია
def names_starting_with_n(names):
    result = []
    for name in names:
        if name.startswith("N"):
            result.append(name)
    return result
print(names_starting_with_n(["Nika", "Ana", "Nino", "Giorgi"]))