# def my_function(x, y):
#     result = (x+y)/2
#     return result
# print(my_function(5, 10))


# def my_function(var)
#     for i in  len(var)
#         if i != "!":
#         print(input("Enter a sentence: "))

# def remove_exclamation_marks(abc):
#     return abc.replace("!", "")
# input_str = "Hello! This is an example!"
# result = remove_exclamation_marks(input_str)
# print(result)

def calculate_sum(numbers):
    total = sum(numbers)
    if total > 20:
        return "Bigger than 20"
    else:
        return total
num1 = 1
num2 = 2
num3 = 7
num4 = 4
result = calculate_sum([num1, num2, num3, num4])
print(result)



