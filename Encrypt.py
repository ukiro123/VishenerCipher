def vigenere_encrypt(text, keyword):
    encrypted_text = ""
    keyword = keyword.upper()
    text = text.upper()
    key_length = len(keyword)
    key_index = 0

    for char in text:
        if char.isalpha():
            encrypted_char = chr((ord(char) + ord(keyword[key_index % key_length]) - 2 * ord('А')) % 30 + ord('А'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text


text = input("Введите текст для шифра:")
keyword = input("Введите ключ для шифра:")

encrypted_text = vigenere_encrypt(text, keyword)
print("Зашифрованный текст:", encrypted_text)

