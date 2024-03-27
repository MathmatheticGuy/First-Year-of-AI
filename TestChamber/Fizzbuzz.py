def fizzbuzz(num):
    conditions = {
        3: "Fizz",
        5: "Buzz",
        7: "Bazz",  
        8: "FAZZ",
    }
    
    for nigga in range(1, num + 1):
        output = ""
        for divisor, word in conditions.items():
            if nigga % divisor == 0:
                output += word

        print(output or nigga)  

fizzbuzz(1000) 
