import random
import string
print("Random Password Generator")
def main():
    length=int(input("Enter the length of the password :"))
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    symbol=string.punctuation
    digit=string.digits
    combine=uppercase+lowercase+symbol+digit
    password=random.sample(combine,length)
    print("".join(password))
    main()
main()