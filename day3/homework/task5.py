# დაწერეთ ფუნქცია რომელსაც გადაეცემა ორი მთელი რიცხვი და დაპრინტავს პირველი რიცხვიდან მეორე რიცხვამდე არსებული რიცხვების  ა)საშუალო არითმეტიკულს, ბ) მედიანას, გ) საშუალო კვადრატულ გადახრას

import math

def median_numbers(sorted_arr):
    if len(sorted_arr) % 2 == 1:
        return sorted_arr[len(sorted_arr) // 2]
    return "median " + str((sorted_arr[len(sorted_arr) // 2] + sorted_arr[(len(sorted_arr) // 2) - 1]) // 2)

def deviation(avarage_numbers, sorted_arr):
    deviation_numbers = 0
    
    for num in sorted_arr:
        deviation_numbers += (num - avarage_numbers) ** 2
        
    deviation_numbers = deviation_numbers // len(sorted_arr)
    deviation_numbers = int(math.sqrt(deviation_numbers))
    
    return "deviation " + str(deviation_numbers)
        
    

def avarage_numbers(num1, num2):
    sorted_arr = []
    numbers_sum = 0   
    avarage = 0
    
    for i in range(num1, num2):
        sorted_arr.append(i)
        
    sorted_arr.sort()
    numbers_sum = sum(sorted_arr)
    avarage = numbers_sum / len(sorted_arr)
    
    

        
    print(median_numbers(sorted_arr))    
    print(deviation(avarage, sorted_arr))
    return avarage
    
    
    
print(avarage_numbers(1, 5))


