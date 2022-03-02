# string_name = "Shakrudin"
# print (len(string_name))

# string_name = "Rishabh Verma"
# print (len(string_name))

# string_name = "navgurukul"
# if "n" in string_name:
#     print ("n hai")
# else:
#     print ("n nahi hai")

# print ("n" in string_name)
# print (type("n" in string_name))


# Upper_case = input("enter tne upper case:")
# if Upper_case >='A' or Upper_case <='Z':
#     Lower_case = input("enter the lower case:")
#     if Lower_case >='a' or Lower_case <='z':
#         numeric_number =int (input("enter the numeric number:"))
#         if numeric_number >=0 or numeric_number <=9:
#             special_character = input("enter the special character:")
#             if special_character == '@' or special_character == '$' or special_character == '#' or special_character == '&':
#                 new = Upper_case + Lower_case + str(numeric_number) + special_character
#                 if len(new) == 8:
#                     print("it is a strong passward",new)
#                 else:
#                     print("it is not strong passward",new)


import  re 

def strong_passward(password1):
    if len(password1)>6 and len(password1)<16:
        if re.findall("[^a-zA-Z0-9]",password1):
            print('password is created')
            return True
        else:
            print("password1 must contain at least one character,one digit or one special character")
            # password1 = input ('enter the password:')
            # strong_password(password1)
    else:
        print('')
        return True
password = input ('enter the password:')
a=strong_passward(password)
print(a)