def game():
    def is_pronic(x):
        pronic = False
        for i in range(x):
            if x == i * (i+1):
                pronic = True
        if pronic == True:
            return ('the number is pronic')  
        else:
            return('the number is not pronic')
    
    
    #////////////////////////////////////////////////
    
    def is_prime(x):
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
        if prime:
            return('the number is prime')
        else:
            return('the number is not prime')
    
    #/////////////////////////////////////////////////////
    
    print("__________ Hello, Welcome to NumChecker __________")
    user_num_input = int(input("please enter a number: "))
    user_process_1st_choice = input('please choose process (prime or pronic): ').lower()
    if user_process_1st_choice == 'prime':
        print(is_prime(user_num_input))
    if user_process_1st_choice == 'pronic':
        print(is_pronic(user_num_input))
    if input("Do you want to play again? (yes or no) ") == "yes":
        game()
    else:
        print("ok, Bye Bye")
game()







