#!/usr/bin/python3
import pprint

with open('input') as f:
  data = f.read().split("\n")

t=0
for i in data:
  tmp = list()
  if not i:
    continue
  l = i.split()
  l.sort(key=int)
  for a in reversed(l):
    tmp.append(a)
  l = tmp
  for j in range(0, len(l)):
    for k in range(0,len(l)):
      if j==k:
        continue
      if int(l[j]) % int(l[k]) == 0:
        t += int(l[j])/int(l[k])


print(t)
