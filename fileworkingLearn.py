

path = 'files.txt'

outpath = 'newfiles.txt'

myfile = open(path, mode = 'r', encoding = 'UTF-8')
myfile1 = open(outpath, mode = 'a', encoding = 'UTF-8')

for z,x in enumerate(myfile,1):
    if 'kostya' in x:
        print(str(z) + ' hello ' + x.strip())
        myfile1.write(str(z) + ' hello ' + x)

myfile.close()
myfule1.close()