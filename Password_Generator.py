import random
import string

def Password_Generator(length):
    character= string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    password= "".join(random.choice(character) for _ in range(length))
    return password    

def get_length():
    while True:
        
       try:
        desired_length=int(input("Enter the desired length of the password: "))
        if desired_length<=0:
            print("password length must be greater than zero.")
        else:
            return desired_length  
       except ValueError:
            print("Invalid Input: Enter correct value please.")
        
def main():
    print("--------------------Password Generator-------------------------\n")
    length=get_length()
    password=Password_Generator(length)
    print("Generated Password is: " + str(password))
    
if __name__ == "__main__":
    main()    