def crack_enigma_code():
    encrypted_message = input()

    while True:
        command = input()

        if command == 'Decode':
            break

        action, *params = command.split('|')

        if action == 'Move':
            number_of_letters = int(params[0])
            encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

        elif action == 'Insert':
            index, value = int(params[0]), params[1]
            encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

        elif action == 'ChangeAll':
            substring, replacement = params
            encrypted_message = encrypted_message.replace(substring, replacement)

    print(f'The decrypted message is: {encrypted_message}')


crack_enigma_code()
