
#1
try:
 a = 1/0;
except Exception as e:
    print(e)

#2
try:
 a = 1/0
 print(a)
except Exception as e:
    print(e)
# except is to generally

#except IOError = Error open a file



# Create a file
def create_file(name):
 try:
  fh = open('words.txt','w')
  fh.write(name)
  print(fh)
 #fh.close()
 except Exception as e:
  print(e)



create_file('Noam Lederman')
