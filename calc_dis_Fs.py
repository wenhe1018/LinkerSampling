from classPoint import Point
fi = open('coor_confs.txt','r')
fo = open('dist_confs.txt','w')
def get_coor():

    
        l = line.split()
        fl1 = l[0]
        fl2 = l[1]
        fl3 = l[2]
        x = float(fl1)
        y = float(fl2)
        z = float(fl3)
        a = Point (x,y,z)
        return a

l = []
for line in fi.readlines():
    if '   ' in line:
        a = get_coor()
        l.append(a)
print(len(l))
for i in range(len(l)):
    if i%2 == 0:
        dist = Point.distance_to_another_point(l[i],l[i+1])
        print(dist)
        fo.write(str(dist))
        fo.write('\n')


fi.close()
fo.close()

