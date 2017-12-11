# -*-coding: utf8 -*-

import re

DIC = {chr(x): x - 97 for x in range(97, 123)}


def ask(quest, cond=None):
    while True:
        if cond == 'd':
            answer = input(quest)
            if not answer.isdigit():
                print('Only digits')
                continue
            else:
                return int(answer)
        answer = input(quest)
        if re.search(r'[^a-zA-Z \',.:"?!]',
                     answer):
            print('Only English alph')
            continue
        return answer.lower()


def cEncode(string, key):
    new_string = ''
    for i in string:
        if i not in DIC:
            new_string += i
            continue
        ch = DIC[i] + key
        if ch > 25:
            ch = ch - 26
        new_string += get_key(DIC, ch)
    return print(new_string)


def cDecode(string, key):
    new_string = ''
    for i in string:
        if i not in DIC:
            new_string += i
            continue
        ch = DIC[i] - key
        if ch < 0:
            ch = 26 + ch
        new_string += get_key(DIC, ch)
    return print(new_string)


def get_key(dic, val):
    for i in dic.items():
        if val in i:
            return i[0]


def main():
    while True:
        string = ask('Enter the string: ')
        enDe = ask('Encode or Decode(e/d): ')
        key = ask('Enter the key: ', 'd')
        if enDe == 'e' or enDe == 'encode':
            cEncode(string, key)
        elif enDe == 'd' or enDe == 'decode':
            cDecode(string, key)
        else:
            continue


if __name__ == '__main__':
    main()
