#  დაწერეთ ფუნქცია რომელსაც გადაეცემა 4 ნიშნა მთელი რიცხვი (თქვენ მაინც ინტს გადაცემთ მაგრამ ჩათვალეთ რომ გადმოცემული რიცხვი ყოველთვის 4 ნიშნაა) და აბრუნებს ამ რიცხვის ციფრთა ჯამს

def my_func(number):
    sum = 0
    for num in str(number):
        sum += int(num)
        
    return sum

print(my_func(4444))