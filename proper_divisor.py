def proper_divisor(number):
    divisors = []
    for num in range(1,number):
        if number % num == 0 :
            divisors.append(num)
        return divisors
    
number = int(input("Enter a number to find its proper divisor : "))
print(proper_divisor(number))   