import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
         
         's','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','@','#','$','%','&','*','()',')','_']

print("WELCOME TO PASSWORD GENERATION")
n_letters=int(input("How many letters you want in your password: \n"))
n_symbols=int(input("How many letters you want in your password: \n"))
n_numbers=int(input("How many letters you want in your password: \n"))
password=[]   
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for _ in range(1,n_numbers+1):
    num=random.choice(numbers)
    password+=num
for _ in range(1,n_symbols+1):
    sym=random.choice(symbols)
    password += sym
random.shuffle(password)
password_generated=" "
for i in password:
    password_generated+=i
print("Your generated password is :",password_generated)