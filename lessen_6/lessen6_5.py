# Программа получает на вход строку – сообщение и
# указание, что нужно сделать: шифровать или дешифровать.
# Реализовать две функции: первая шифрует заданное сообщение
# шифром Цезаря, вторая – расшифровывает. В зависимости от
# выбора пользователя (шифровать или дешифровать) вызывается
# соответствующая функция, результат выводится в консоль

def encrypt(text: str, shift: int) -> str|int:
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = ""
    for char in text:
        if char.lower() in alphabet:
            idx = (alphabet.find(char.lower()) + shift) % len(alphabet)
            new_char = alphabet[idx]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# --- Логика выбора ---
action = input("Что сделать? (1 - шифровать, 2 - дешифровать): ")
message = input("Введите сообщение: ")
step = int(input("Введите шаг: "))

if action == '1':
    print("Результат:", encrypt(message, step))
elif action == '2':
    print("Результат:", decrypt(message, step))
else:
    print("Ошибка выбора!")
