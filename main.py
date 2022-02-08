from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(start_text, shift_amount, cipher_type):
    flag = True
    caesar_text = ""

    for letter in text:
        if letter == ' ':
            caesar_text += ' '
            continue
        elif letter not in alphabet:
            caesar_text += letter
            continue

        letter_index = alphabet.index(letter)
        new_shift = shift % 26

        if direction == "encode":
            new_index = letter_index + new_shift

        elif direction == "decode":
            new_index = letter_index - new_shift
            flag = False

        new_letter = alphabet[new_index]
        caesar_text += new_letter

    if flag == True:
        print(f"\nThe encoded text is: {caesar_text}")
    else:
        print(f"\nThe decryption text is: {caesar_text}")


retry = "yes"
while retry == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_type=direction)
    retry_response = input("\nDo you want to restart the cipher program? Type yes or no. ").lower().strip()
    if retry_response == "no":
        retry == False
        print("Goodbye.")
        break


