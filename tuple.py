tupleFruits = ('apple','banana','cherry') #Tuple
listFruits = ['apple','banana','cherry'] #list
print('original tuple:',tupleFruits)
print('original list:',listFruits)
#เปลี่ยนค่าในtuple
x=list(tupleFruits)#แปลงเป็นlistแล้วเก็บในตัวแปร x
x[1]='blueberry'
tupleFruits=tuple(x)
print('เปลี่ยนค่าtuple:',tupleFruits)
#เพิ่มค่าใน tuple
x=list(tupleFruits)
x.append('melon')
tupleFruits=tuple(x)
print('เพิ่มค่าtuple:',tupleFruits)
#ลบtuple
x=list(tupleFruits)
x.remove('cherry')
tupleFruits=tuple(x)
print('ลบค่าtuple:',tupleFruits)
#join tuple 
vege=('tomato','cucumber','onion')
fruitVege=tupleFruits+vege
print('join tuple:',fruitVege)
x = range(3,6)#จะหยุดก่อนค่าstop
for n in x:
    print('range x:',n)
y = range(3,20,2)
for m in y:
    print('range y:',m)    
#เอกอนันต์ ฮะสุน ม.6/11 เลขที่ 7 