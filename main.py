import os
import requests

def transrate(URLs):
  for i in range(len(URLs)):
    URLs[i] = URLs[i].strip()
    URLs[i] = URLs[i].lower()
    print(URLs[i])
    if URLs[i][0:4] != 'http':
      URLs[i] = 'http://' + URLs[i]
  return URLs

def connect(URLs):
  for i in range(len(URLs)):
    try:
      result = requests.get(URLs[i])
      print(f"{URLs[i]} is UP!")
    except :
      print(f"{URLs[i]} is DOWN!")

while 1:
  os.system('clear')
  print("Welcome to IsItDown.py!")
  URL = input("Please write a URLs you want to check. (separated by comma)\n")
  URLs = URL.split(',')

  transrate(URLs)
  connect(URLs)
  while 'y':
    answer = input("Do you want start over? y/n ").lower()
    if answer == 'y' or answer == 'n':
      break
    else:
      print("that`s not vaild answer.")
  if answer == 'n':
    print("OK bye!")
    break
  