#!/usr/bin/python3

with open('input', 'r') as f:
  input=f.readline()

the_list = list(input.strip())
x=0
total=0
for i in the_list:
  i = int(i.strip())
  if x == int(len(the_list))-1:
    if i == int(the_list[0]):
      total += i
  elif i == int(the_list[x+1]):
    total += i
 # print("%s == %s" % (i, the_list[x+1]))
  x += 1

print(total)
