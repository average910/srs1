def caesar(text, shift, mode="encrypt"):
    if mode == "decrypt":
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            result += str((int(char) + shift) % 10)
        else:
            result += char

    return result

password = input("Введите пароль: ")
shift = int(input("Введите ключ: "))

encrypted = caesar(password, shift, "encrypt")
decrypted = caesar(encrypted, shift, "decrypt")

print("Зашифрованный:", encrypted)
print("Расшифрованный:", decrypted)
