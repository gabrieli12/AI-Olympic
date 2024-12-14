#  დაწერეთ ფუნქცია რომელსაც გადაეცემა სტრინგების ლისტი და აბრუნებს ამ ლისტში ყველაზე გრძელ სტრინგს

def longest_string(arr):
    longest_str = arr[0]
    
    for element in arr:
        if len(element) > len(longest_str):
            longest_str = element
            
    return longest_str


print(longest_string(["gas", "agsgas", "aaaa", "asfgasfasfa"]))