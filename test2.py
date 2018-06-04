import sys

# filename_py = '/home/sgs75/test2.py'
filename_py = sys.argv[0]
print('Your program listing from '+filename_py+':')
f = open(filename_py, 'r')
text = f.read()
f.close
print(text)
