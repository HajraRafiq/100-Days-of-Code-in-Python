from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    def caesar(start_text,shift_amount,cipher_direction):
        end_text = ""
        for char in start_text:
            if char in alphabet:
                position=alphabet.index(char)

                if cipher_direction == "encode":
                    new_position = position + shift_amount
                else:
                    new_position = position - shift_amount
                end_text= end_text +  alphabet[new_position]
            else:
                end_text = end_text + char
        print(f"The {cipher_direction}d text is: {end_text}")

    caesar(start_text=text,shift_amount=shift,cipher_direction=direction) 
    result = input("Do you want to continue . Type yes or no\n")
    if result  == "no":
        repeat = False
        print("Good Bye")



# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for char in plain_text:
#         position=alphabet.index(char)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded msg is {cipher_text}")



# def decrypt(plain_text,shift_amount):
#     cipher_text=""
#     for char in plain_text:
#         position=alphabet.index(char)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The decoded msg is {cipher_text}")

# if direction == "encode":

#     encrypt(plain_text=text, shift_amount =shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount =shift)