from day_6_art import logo

# value_collection
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def encode_and_decode():
    again = True
    while again:
        direction = input("enter 'encode' to 'shift' and 'decode' to 'see' = ").lower()
        if direction == "encode" or direction == "decode":
            shift = int(input("enter the shift value = "))
            user_input = input("enter the input = ").lower()
            shift_value = shift % 26
            final_result = ""

            # encode and decode
            for char in user_input:
                if char in alphabet:
                    selected_letter_index_in_alphabetic = alphabet.index(char)
                    if direction == "encode":
                        shifting_the_values = selected_letter_index_in_alphabetic + shift_value
                        final_result += alphabet[shifting_the_values]
                    elif direction == "decode":
                        shifting_the_values = selected_letter_index_in_alphabetic - shift_value
                        final_result += alphabet[shifting_the_values]
                    else:
                        print("type error")

                else:
                    final_result += char

            # final_result
            print(final_result)
        else:
            print("type error")
            again = True
        again_want = input("Do you want to encode/decode again? (yes or no): ").lower()
        if again_want != "yes":
            again = False


# Main execution
encode_and_decode()
