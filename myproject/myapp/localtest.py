__author__ = 'Fridge'
import parser.lowparse as low
a = open("../../a.txt").readlines()
count = low.get_api_times_count(a)
print count
