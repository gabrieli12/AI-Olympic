# დაწერეთ ფუნქცია რომელსაც გადაეცემა სტრინგების ლისტი და აბრუნებს ამ სიაში ყველაზე ხშირად გამეორებულ სტრინგს. ( თუ ორი ან რამდენიმეა ასეთი მაშინ დააბრუნეთ ნებისმიერი)

def frequency(arr):
    final_result = arr[0]
    
    for element in arr:
        if arr.count(element) > arr.count(final_result):
            final_result = element
            
    return final_result


print(frequency(["a", "a", "b", "c", "b", "b"]))