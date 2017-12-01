#!/usr/bin/python3

with open('input', 'r') as f:
  input=f.readline()

the_list = list(input.strip())
fulhackad_list = the_list+the_list
x=0
total=0
list_len = int(len(the_list))
for i in the_list:
  k = int(((x)+(list_len/2)) % list_len)
  print(k)
  i = int(i.strip())
  if i == int(the_list[k]):
    total += i
  x += 1


print(total)
