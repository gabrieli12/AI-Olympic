# დაწერეთ ფუნქცია რომელსაც გადაეცემა მთელი რიცხვი, ფუნქცია უნდა გადაყვეს რიცხვებს 1 დან ამ რიცხვამდე და დაპრინტოს Fizz თუ რიცხვი იყოფა 3-ზე, Buzz თუ რიცხვი იყოფა 5-ზე და FizzBuzz თუ რიცხვი იყოფა სამზეც და ხუთზეც.

def fizz_buzz(num):
    for i in range(1, num):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")   

fizz_buzz(50)