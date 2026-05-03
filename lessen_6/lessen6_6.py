def vigenere_encrypt(text: str, key: any):
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    res = ""
    key = key.lower()
    key_idx = 0
    for char in text:
        if char.lower() in alphabet:
            # Находим сдвиг через букву ключа
            shift = alphabet.find(key[key_idx % len(key)])
            # Шифруем
            idx = (alphabet.find(char.lower()) + shift) % len(alphabet)
            new_char = alphabet[idx]
            res += new_char.upper() if char.isupper() else new_char
            key_idx += 1
        else:
            res += char
    return res

def vigenere_decrypt(text: str, key: any):
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    res = ""
    key = key.lower()
    key_idx = 0
    for char in text:
        if char.lower() in alphabet:
            # Находим сдвиг и вычитаем его
            shift = alphabet.find(key[key_idx % len(key)])
            idx = (alphabet.find(char.lower()) - shift) % len(alphabet) # меняем + на - для дешифровки
            new_char = alphabet[idx]
            res += new_char.upper() if char.isupper() else new_char
            key_idx += 1
        else:
            res += char
    return res

vigener = input("1 - Шифровать, 2 - Дешифровать: ")
message = input("Введите сообщение: ")
key_word = input("Введите ключ (слово): ")

if vigener == '1':
    print("Результат:", vigenere_encrypt(message, key_word))
elif vigener == '2':
    print("Результат:", vigenere_decrypt(message, key_word))
else:
    print("Ошибка выбора!")
