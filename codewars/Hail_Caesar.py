import string


def hail_caesar(enc_str):
    alphabet = list(string.ascii_uppercase)
    letters = list(enc_str)
    enc_res = ''
    for i in letters:
        if i in alphabet:
            letterIndex = alphabet.index(i)
            enc_res += alphabet[letterIndex-13]
        else:
            enc_res += i
    return enc_res


hail_caesar("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.")
