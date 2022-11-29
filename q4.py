binary_no=input("enter binary no.")
dec = int(binary_no, 2)

def dec_to_Roman(n):
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbols = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while n:
        div = n // numbers[i]
        n %= numbers[i]
        while div:
            print(symbols[i], end = "")
            div -= 1
        i -= 1
  
print("Roman value is:", end = " ")
dec_to_Roman(dec)
