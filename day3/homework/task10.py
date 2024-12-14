# დაწერეთ ფუნქცია რომელსაც გადაეცემა რიცხვების ორი ლისტი და პრინტავს მხოლოდ იმ უნიკალურ ელემენტებს რომლებიც ორივე ლისტში გვხვდება


def is_same_element(arr1, arr2):
    for element in arr1:
        if element in arr2:
            print(element)
            
            
is_same_element(["aa", "khjkh", "gasgas", "bb"], ["asasa", "aa", "gasgas", "bb"])



