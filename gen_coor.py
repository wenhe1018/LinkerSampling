fi = open('confs.txt','r')
fo = open('coor_confs.txt','w')
a=1
for line in fi.readlines():
    
    if 'OpenBabel06152019253D' in line:
        fo.write('molecule ')
        fo.write(str(a))
        fo.write('\n')
        a+=1
        '''
    if 'OpenBabel06152019253D' in line:
        fo.write('molecule ')
        fo.write(str(a))
        fo.write('\n')
        a+=1
        '''

    if 'F' in line:
        for i in range(len(line)):
            if line[i] == 'F':
                fo.write(line[:i])
                fo.write('\n')

fi.close()
fo.close()        
