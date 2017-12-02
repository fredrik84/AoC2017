#!/usr/bin/python3
import pprint

with open('input') as f:
  data = f.read().split("\n")
t=0
for i in data:
  if not i:
    continue
  chksm=0
  for j in i.split():
    l = sorted(list(j))
    sum = int(l[-1])-int(l[0])
    chksm += sum
  print(chksm)
  t += chksm

print(t)
