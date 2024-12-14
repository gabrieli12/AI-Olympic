#  დაწერეთ ფუნქცია რომელსაც გადაეცემა მთელი რიცხვი და აბრუნებს ყველაზე დიდ მარტივ რიცხვს 1 დან ამ რიცხვამდე

def is_number_prime(num):
    prime_numbers = []
    not_prime_numbers = []
    
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                not_prime_numbers.append(i)
                break
        
    for i in range(2, num):
        if i not in not_prime_numbers:
            prime_numbers.append(i)
             
    return largest_prime(prime_numbers)
    # return prime_numbers


def largest_prime(prime_numbers_list):
    largest_prime_number = prime_numbers_list[0]
    
    for num in prime_numbers_list:
        if num > largest_prime_number:
            largest_prime_number = num
            
    print(prime_numbers_list)
    return largest_prime_number


print(is_number_prime(50))
    
    
    
    
    