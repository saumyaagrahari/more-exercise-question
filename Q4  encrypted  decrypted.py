def find_in_list(query,mainlist):

    mainlist_len = len(mainlist)
    
    range_for_loop = range(mainlist_len)
    
    index = 0
    
    for i in range_for_loop:
    
        element = mainlist[i]
    
        if element == query:
    
            index = i
    
    return index

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

def encrypt_msg(plain_msg):

    encrypted_msg = plain_msg   
    for character in encrypted_msg:

        if character in chars:

            char_index = find_in_list(character,chars)

            new_char = shifted_chars[char_index]

            encrypted_msg =  new_char
            print(encrypted_msg)


def decrypt_message (encrypted_msg):

    decrypted_msg = encrypted_msg

    for character in decrypted_msg:

        if character in shifted_chars:

            char_index = find_in_list(character,shifted_chars)

            new_char = chars[char_index]

            decrypted_msg = new_char

            print(decrypted_msg)

    ############################################ Code starts form here ##################################################

flag = True

while flag == True:

    choice = input("what do you want to do? 1. Encrypt a message 2. Decrypt a message Enter e or d respectively!")

    if choice == 'e':
        
        plain_msg = input("Enter message to encrypt?")
        encrypt_msg(plain_msg)

    elif choice == 'd':

        encrypted_msg = input("Enter message to decrypt?")

        decrypt_message(encrypted_msg)
    else:
        plain_again = input("Do you want to try again ro Do you want to exit? (Y/N)")

        while plain_msg==True:
        
            if plain_again =="Y":
                
                continue

            elif plain_again == "N":

                break