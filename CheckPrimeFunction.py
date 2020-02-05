def check_prime(num):
    a = 1
    p_list = []
    while a <= num:
        if num % a == 0:
            p_list.append(a)
            a += 1
        if len(p_list) - 2 = 0:
            return "prime"
        else:
            return "not prime"  

yet:
    n = input("Choose number: ")
except ValueError as err:
    print("Error: " + str(err))
    
print("Your number is " + check_prime(n) + "!")
