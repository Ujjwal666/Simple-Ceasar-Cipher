#!/bin/bash
#python3 mycipher 3 < plaintext
#python3 mycipher 3 < plaintext > cryptedtext
#python3 mycipher 23 < cryptedtext
import os.path
import sys

punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
shift = sys.argv[1] # defining the shift count
message = sys.stdin.read()
output = sys.stdout
message_upper = message.upper()
for el in message_upper: 
    if el in punc: 
        message_upper = message_upper.replace(el, "") 
encrypted = ""
encrypted_list = []
for i in range(len(message_upper)):
  char = message_upper[i]
  encrypted += chr((ord(char)+int(shift)-65)%26+65)
if len(encrypted)%5 != 0:  
  for i in range(int(len(encrypted)/5)+1):
    encrypted_list.append(encrypted[5*i:5*(i+1)])
else:
  for i in range(int(len(encrypted)/5)):
    encrypted_list.append(encrypted[5*i:5*(i+1)])
count = 1
if output != "":
  for ele in encrypted_list :
    if count % 10 == 0:
      output.write(ele+'\n')
    else:
      output.write(ele+" ") 
    count += 1  
else:
  decrypt = ""
  if count % 10 == 0:
      decrypt += (ele+'\n')
  else:
      decrypt += (ele+" ") 
      
