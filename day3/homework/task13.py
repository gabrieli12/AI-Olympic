# დაწერეთ 3 ფუნქცია რომლებსაც გადაეცემათ ასაკის აღმნიშვნელი რიცხვების მასივი სადაც ზოგიერთი ასაკი გამოტოვებულია (ჩვენ შემთხვევაში გამოტოვებულია ნიშნავს რომ მასივში წერია None (იმის შემოწმება არის თუ არა რაიმე ცვლადის მნიშვნელობა None შეგიძლიათ == გამოიყენოთ ან  is None, მაგალითად arr[i] is None თუ დააბრუნებს True-ს თუ arr[i] None-ია)) და აბრუნებენ მასივს სადაც ყველა ეს None ჩანაცვლებულია  ა) პირველი ფუნქციის შემთხვევაში არა-None რიცხვების საშუალოთი, ბ) მეორე ფუნქციის შემთხვევაში არა-None რიცხვების მედიანით გ) მესამე ფუნქციის შემთხვევაში არა-None რიცხვებში ყველაზე ხშირად შეხვედრადი რიცხვით


age_arr = [1, 2, None, 4, 5, None, 7, 8, 9, 5]

def removeNone(arr):
    filtered_arr = []
    
    for element in arr:
        if element is not None:
            filtered_arr.append(element)
            
    return filtered_arr

filtered_arr = removeNone(age_arr)


def change_none_avarage(arr, filter_arr):      
    for element in arr:
        if element is None:
            arr[arr.index(element)] = sum(filter_arr) // len(filter_arr)
                   
    return arr

def change_none_median(arr, filter_arr):
    filtered_arr.sort()
    
    for element in arr:
        if element is None:
            if len(filter_arr) % 2 == 1:
                arr[arr.index(element)] = filter_arr[len(filter_arr) // 2]
            else:
                arr[arr.index(element)] = (filter_arr[len(filter_arr) // 2] + filter_arr[(len(filter_arr) // 2) - 1]) // 2

    return arr
            
def change_none_frequency(arr, filter_arr):
    final_result = filter_arr[0]
    
    for element in filter_arr:
        if filter_arr.count(element) > filter_arr.count(final_result):
            final_result = element

    for element in arr:
        if element is None:
            arr[arr.index(element)] = final_result

    return arr
            
            
print(change_none_avarage(age_arr, filtered_arr))
print(change_none_median(age_arr, filtered_arr))
print(change_none_frequency(age_arr, filtered_arr))