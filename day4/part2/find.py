#!/usr/bin/python3
import pprint

with open('input') as f:
  data = f.read().strip().split("\n")
ok = list()
for i in data:
  check = dict()
  for j in i.split():
    string = ''.join(sorted(j))
    if not string in check:
      check[string] = 1
  count = len(i.split())
  if count == len(check):
    ok.append(i)


pprint.pprint(len(ok))
