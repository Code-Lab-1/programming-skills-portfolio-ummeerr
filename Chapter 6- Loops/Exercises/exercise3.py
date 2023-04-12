while True:
    age = input("What is oyur age? ")
    
    age = int(age)
    if age < 3:
        print("ticket is free")
    elif age < 12:
        print("ticket is $10") 
    else:
        print("ticket is $15")