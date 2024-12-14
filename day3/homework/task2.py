# დაწერეთ ფუნქცია რომელსაც გადაეცემა მთელი რიცხვი ( ამჯერად არაა აუცილებელი რომ მხოლოდ 4 ნიშნა იყოს) და აბრუნებს ამ რიცხვის ციფრთა ჯამს


def my_func(number):
    sum = 0
    for num in str(number):
        sum += int(num)
        
    return sum

print(my_func(4444))