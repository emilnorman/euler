#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time

def flush(h):
    if h[0][1] == h[1][1] and h[1][1] == h[2][1] and h[2][1] == h[3][1] and h[3][1] == h[4][1]:
        return True
    else:
        return False


def four_kind(h):
    if (h[0][0] == h[1][0] and h[1][0] == h[2][0] and h[2][0] == h[3][0]) or \
       (h[0][0] == h[1][0] and h[1][0] == h[2][0] and h[2][0] == h[4][0]) or \
       (h[0][0] == h[1][0] and h[1][0] == h[4][0] and h[4][0] == h[3][0]) or \
       (h[0][0] == h[4][0] and h[4][0] == h[2][0] and h[2][0] == h[3][0]) or \
       (h[4][0] == h[1][0] and h[1][0] == h[2][0] and h[2][0] == h[3][0]):
        return True
    else:
        return False
       
def full_house(h):
    if ((h[0][0] == h[1][0] and h[1][0] == h[2][0]) and (h[3][0] == h[4][0])) or \
       ((h[0][0] == h[1][0]) and (h[2][0] == h[3][0]) and (h[3][0] == h[4][0])):
        return True
    else:
        return False

def straight(h):
    c = sorted([int(card[0].replace('T', '10').replace('J','11').replace('Q', '12').replace('K', '13').replace('A', '14')) for card in h])

    if c[0] + 1 == c[1] and c[1] + 1 == c[2] and c[2] + 1 == c[3] and c[3] + 1 == c[4]:
        return True
    else:
        return False

def three_kind(h):
    if ((h[0][0] == h[1][0] and h[1][0] == h[2][0]) or \
        (h[1][0] == h[2][0] and h[2][0] == h[3][0]) or \
        (h[2][0] == h[3][0] and h[3][0] == h[4][0])):
        return True
    else:
        return False

def two_pairs(h):
    if ((h[0][0] == h[1][0] and h[3][0] == h[4][0]) or \
        (h[1][0] == h[2][0] and h[3][0] == h[4][0]) or \
        (h[0][0] == h[1][0] and h[2][0] == h[3][0])):
        return True
    else:
        return False

def pair(h):
    c = sorted([int(card[0].replace('T', '10').replace('J','11').replace('Q', '12').replace('K', '13').replace('A', '14')) for card in h])

    if c[0] == c[1]:
        return c[0]
    if c[1]== c[2]:
        return c[2]
    if c[2] == c[3]:
        return c[3]
    if c[3] == c[4]:
        return c[4]
    return False

def high_card(h):
    c = sorted([int(card[0].replace('T', '10').replace('J','11').replace('Q', '12').replace('K', '13').replace('A', '14')) for card in h])
    return c

start_time = time.time()

wins_p1 = 0
unknown = 0

with open("p054_poker.txt", "r") as f:
    for row in f:
        r = row.replace("\n", "")
        c = r.split(" ")
        h1 = sorted(c[:5])
        h2 = sorted(c[5:])

        if four_kind(h1) or four_kind(h2):
            if four_kind(h1) and not four_kind(h2):
                wins_p1 += 1
            elif four_kind(h2) and not four_kind(h1):
                pass
            else:
                print("Error")
                exit(0)
        if full_house(h1) or full_house(h2):
            if full_house(h1) and not full_house(h2):
                wins_p1 += 1
                continue
            elif full_house(h2) and not full_house(h1):
                continue
            else:
                print("Error")
                exit(0)
        if flush(h1) or flush(h2):
            if flush(h1) and not flush(h2):
                wins_p1 += 1
                continue
            elif flush(h2) and not flush(h1):
                continue
            else:
                print("Error")
                exit(0)
        if straight(h1) or straight(h2):
            if straight(h1) and not straight(h2):
                wins_p1 += 1
                continue
            elif straight(h2) and not straight(h1):
                continue
            else:
                print("Error")
                exit(0)
        if three_kind(h1) or three_kind(h2):
            if three_kind(h1) and not three_kind(h2):
                wins_p1 += 1
                continue
            elif three_kind(h2) and not three_kind(h1):
                continue
            else:
                print("Error")
                exit(0)
        if two_pairs(h1) or two_pairs(h2):
            if two_pairs(h1) and not two_pairs(h2):
                wins_p1 += 1
                continue
            elif two_pairs(h2) and not two_pairs(h1):
                continue
            else:
                print("Error")
                exit(0)
        if pair(h1) or pair(h2):
            if pair(h1) > pair(h2):
                wins_p1 += 1
                continue
            elif pair(h2) > pair(h1):
                continue
            else:
                print("Error!!!", h1, h2)
              

        hc1 = high_card(h1)
        hc2 = high_card(h2)
        if hc1[4] == hc2[4]:
            if hc1[3] == hc2[3]:
                if hc1[2] == hc2[2]:
                    if hc1[1] == hc2[1]:
                        if hc1[0] == hc2[0]:
                            print("Error")
                            exit(0)
                        elif hc1[0] > hc2[0]:
                            wins_p1 += 1
                    elif hc1[1] > hc2[1]:
                        wins_p1 += 1
                elif hc1[2] > hc2[2]:
                    wins_p1 += 1
            elif hc1[3] > hc2[3]:
                wins_p1 += 1
        elif hc1[4] > hc2[4]:
            wins_p1 += 1

print(wins_p1)

