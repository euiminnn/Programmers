s = "AbCeYzx"
n = 1

import string

def cipher(c, n) :
    Uplist = list(string.ascii_uppercase)
    Lolist = list(string.ascii_lowercase)
    if c == ' ' :
        return c
    if c.isupper() :
        ind = Uplist.index(c)
        ### recursion needed ###
        #if (ind + n) > 25 :
            #ind = ind - 26
        c = Uplist[(ind + n) % 26] #use remainder, don't need recursion!
    elif c.islower() :
        ind = Lolist.index(c)
        #if (ind + n) > 25 :
            #ind = ind - 26
        c = Lolist[(ind + n) % 26]
    return c

def solution(s, n) :
    answer = ""
    for i in range(0, len(s)) :
        answer = answer + cipher(s[i], n)
    print(answer)

solution(s, n)
