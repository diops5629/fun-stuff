message = "put either the encrypted or decrypted message here whatever you like"
key = "wouldnt you like to know"

def convert_to_number(msg):
    output = []
    for i in msg:
        if i == ' ':
            output.append(26)
        else:
            output.append(ord(i)-ord('a'))
    return output

def convert_to_three(conv):
    final = []
    for i in conv:
        check = 0
        number = 1000
        while i > 0:
            number += pow(10, check) * (i%3)
            i = int(i/3)
            check += 1
        final.append(number)
    return final

def convert_to_ten(conv):
    final = []
    for i in conv:
        check = 0
        number = 0
        while i > 0:
            number += pow(3, check) * (i%10)
            i = int(i/10)
            check += 1
        final.append(number)
    return final

def change_type(conv, what):
    final = []
    if what:
        for i in conv:
            final.append(str(i)[1:4])
        return final
    for i in conv:
        final.append(int(i))
    return final

def encode(msg, k):
    new_message = []
    for i in range(len(msg)):
        new_token = ""
        for j in range(3):
            if msg[i][j] == '0' and k[i%len(k)][j] == '0':
                new_token += '0'
            elif msg[i][j] == '1' and k[i%len(k)][j] == '1':
                new_token += '2'
            elif msg[i][j] == '2' and k[i%len(k)][j] == '2':
                new_token += '1'
            elif msg[i][j] == '0' and k[i%len(k)][j] == '1':
                new_token += '1'
            elif msg[i][j] == '1' and k[i%len(k)][j] == '0':
                new_token += '1'
            elif msg[i][j] == '0' and k[i%len(k)][j] == '2':
                new_token += '2'
            elif msg[i][j] == '2' and k[i%len(k)][j] == '0':
                new_token += '2'
            elif msg[i][j] == '1' and k[i%len(k)][j] == '2':
                new_token += '0'
            elif msg[i][j] == '2' and k[i%len(k)][j] == '1':
                new_token += '0'
            else:
                print("ERROR")
        new_message.append(new_token)
    return new_message

def decode(msg, k):
    new_message = []
    for i in range(len(msg)):
        new_token = ""
        for j in range(3):
            if msg[i][j] == '0' and k[i%len(k)][j] == '0':
                new_token += '0'
            elif msg[i][j] == '1' and k[i%len(k)][j] == '1':
                new_token += '0'
            elif msg[i][j] == '2' and k[i%len(k)][j] == '2':
                new_token += '0'
            elif msg[i][j] == '0' and k[i%len(k)][j] == '1':
                new_token += '2'
            elif msg[i][j] == '1' and k[i%len(k)][j] == '0':
                new_token += '1'
            elif msg[i][j] == '0' and k[i%len(k)][j] == '2':
                new_token += '1'
            elif msg[i][j] == '2' and k[i%len(k)][j] == '0':
                new_token += '2'
            elif msg[i][j] == '1' and k[i%len(k)][j] == '2':
                new_token += '2'
            elif msg[i][j] == '2' and k[i%len(k)][j] == '1':
                new_token += '1'
            else:
                print("ERROR")
        new_message.append(new_token)
    return new_message

def convert_to_words(msg):
    output = ""
    for i in msg:
        if i == 26:
            output += " "
        else:
            output += chr(i+ord('a'))
    return output


converted = convert_to_number(message)
converted = convert_to_three(converted)
converted = change_type(converted, True)

new_key = convert_to_number(key)
new_key = convert_to_three(new_key)
new_key = change_type(new_key, True)

encoded_msg = encode(converted, new_key)
encoded_msg = change_type(encoded_msg, False)
encoded_msg = convert_to_ten(encoded_msg)
encoded_msg = convert_to_words(encoded_msg)
print(encoded_msg)

decoded_msg = decode(converted, new_key)
decoded_msg = change_type(decoded_msg, False)
decoded_msg = convert_to_ten(decoded_msg)
decoded_msg = convert_to_words(decoded_msg)
print(decoded_msg)
