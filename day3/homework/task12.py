# დაწერეთ ფუნქცია რომელსაც გადაეცემა ქულების აღმნიშვნელო რიცხვების მასივი და აბრუნებს იგივე ზომის შესაბამის სტრინგების მასივს სადაც თითოეული ელემენტი არის "F" - თუ კონკრეტული ქულა 51-ზე ნაკლებია,  "E" თუ ქულა 51-61 შუალედშია, "D" თუ ქულა 61-71 შუალედშია, "C" თუ ქულა 71-81 შუალედშია, "B" თუ ქულა 81-91 შუალედშია და "A" თუ ქულა 91-101 შუალედშია

def scores(arr):
    final_arr = []
    
    for element in arr:
        if element < 51:
            final_arr.append("F")
        elif element > 52 and element < 61:
            final_arr.append("E")
        elif element > 61 and element < 71:
            final_arr.append("D")
        elif element > 71 and element < 81:
            final_arr.append("B")
        elif element > 91 and element < 101:
            final_arr.append("A")
            
            
            