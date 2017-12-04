#!/usr/bin/python3
import pprint

with open('input') as f:
  data = f.read().split("\n")

t=0
for i in data:
  if not i:
    continue
  l = i.split()
  l.sort(key=int)
  t += int(l[-1])-int(l[0])

print(t)
