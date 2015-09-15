# !/usr/bin/python
# -*- coding: utf-8 -*-

total_sum = 0

letters_hundered = len("hundred")

number_words_low = ["", "one", "two", "three", "four", "five", "six", "seven",
                    "eight", "nine", "ten", "eleven", "twelve", "thirteen",
                    "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                    "nineteen"]
letters_low = [len(i) for i in number_words_low]

number_words_ten = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                    "eighty", "ninety"]
letters_ten = [len(i) for i in number_words_ten]



##### 1-100

# Up to and including 19
total_sum += sum(letters_low)

# 20-99
total_sum += sum(letters_ten) * 10
total_sum += sum(letters_low[1:10]) * 8

# 100-999
total_sum *= 10
total_sum += sum(letters_low[1:10]) * 100

# 1000
total_sum += len("onethousand")

# and
total_sum += len("and") * 9 * 99

# hundred
total_sum += letters_hundered * 900

print(total_sum)

