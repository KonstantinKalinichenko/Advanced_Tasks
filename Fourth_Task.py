def encode_string(string: str) -> str:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    splitted = string.rsplit(maxsplit=1)
    step = int(splitted.pop())
    text = splitted[0]

    res = ''
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.find(letter) + step) % len(alphabet)
            res += alphabet[new_index]
        elif letter == ' ':
            res += letter
    return res


input_string = input()
encoded_string = encode_string(input_string)
print(encoded_string)