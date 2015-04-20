# -*- coding: utf-8 -*-

from random import randint

loto = []


def nakljucje():
    rnd = randint(1, 99)
    return rnd


def kolicina(rnd_st, kolicina_st):
    while len(rnd_st) != kolicina_st:
        rnd_st.append(nakljucje())
    return rnd_st

x = int(raw_input("Koliko številk želiš izpisanih ?: "))

stevilke = kolicina(loto, x)
loto.sort()

print("Zmagovalne loto številke: ")
print(stevilke)
