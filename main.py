from collections import Counter


result = {}


def make_tree(txt):
    frequency = [[x, y] for [y, x] in Counter(txt).items()]

    while len(frequency) > 1:
        frequency.sort(key=lambda x: x[0])
        lLeaf = frequency[0]
        rLeaf = frequency[1]
        del frequency[:2]
        frequency.append([rLeaf[0] + lLeaf[0], [lLeaf[1], rLeaf[1]]])

    return frequency


def encode(array, code=''):
    global result
    if type(array) is list:
        encode(array[0], code + "0")
        encode(array[1], code + "1")
    else:
        result[array] = code if len(code) > 0 else "0"
        print(f"'{array}' {result.get(array)} {(15 - len(result.get(array)))*'-'}> (2^8 - 2^{len(result.get(array))}) * {Counter(text)[array]} = {(2**8 - 2**len(result.get(array))) * Counter(text)[array]} бит сжато")


def print_encoded_text(encoded):
    encoded_text = []
    for x in text:
        print(encoded.get(x), end=' ')
        encoded_text.append(encoded.get(x))
    print()
    return encoded_text


def decode(encoded, hash):
    for x in encoded:
        for key in hash:
            if hash.get(key) == x:
                print(key, end='')
                break


if __name__ == "__main__":
    text = input("Введите текст для сжатия: ")
    encode(make_tree(text).pop()[1])
    decode(print_encoded_text(result), result)
