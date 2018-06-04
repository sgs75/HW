import os

print("Hello!")
name = input("Your name: ")
print('Hello, '+name+'!')
print('')
filename_py = '/home/sgs75/test2.py'
cl = 'python3 '+filename_py
os.system(cl)