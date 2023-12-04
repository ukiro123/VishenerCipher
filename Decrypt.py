def vigenere_decrypt(encrypted_text, keyword):
    decrypted_text = ""
    keyword = keyword.upper()
    encrypted_text = encrypted_text.upper()
    key_length = len(keyword)
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            decrypted_char = chr((ord(char) - ord(keyword[key_index % key_length]) + 30) % 30 + ord('А'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

text = input("Введите текст для дешифрации:")
keyword = input("Введите ключ для дешифрации:")

decrypted_text = vigenere_decrypt(text, keyword)
print("Расшифрованный текст:", decrypted_text)