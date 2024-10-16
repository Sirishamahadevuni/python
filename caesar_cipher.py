letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',     
         's','t','u','v','w','x','y','z']

def encrption(plain_text,shift_key): #hello h=7
    cipher_text=""
    for char in plain_text:
        if char in letters:
            position=letters.index(char)
            new_position=(position + shift_key) % 26
            cipher_text += letters[new_position]
        else:
            cipher_text +=char
    print(f"Here is the text after encryption: {cipher_text}")

def decryption(cipher_text,shift_key): #hello h=7
    plain_text=""
    for char in cipher_text:
        if char in letters:
            position=letters.index(char)
            new_position=(position - shift_key) %26
            plain_text += letters[new_position]
        else:
            plain_text += char
    print(f"Here is the text after encryption: {plain_text}")
wanna_end=False        
while not wanna_end:
    what_to_do=input("Type 'encrypt' for encryption,type 'decrypt' for decryption: ")
    text=input("Type your message:\n").lower()
    shift=int(input("Enter shift key:\n"))
    if what_to_do=="encrypt":
        encrption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(cipher_text=text,shift_key=shift)
    play_again=input("Type 'Yes' To play again or else 'No'")
    if play_again=='No':
        wanna_end=True
        print("Have a Nice Day See You next Time!!")