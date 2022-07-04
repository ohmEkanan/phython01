fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[0])
#เปลี่ยนค่าใน list
fruits[1]="blackcurrent"
print(fruits)
fruits[1:3]=["banana","kiwi","melon"]
print(fruits)
fruits[1:3]=["blackcurrent"]
print(fruits)
#เพิ่มค่าใน list
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"banana")
print(fruits)
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าใน list
fruits.remove("pineapple")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits ลบตัวแปร list ทิ้งไป
#เรียงค่าใน list
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#รวม list
vege=['carrot','potato','cucamber']
all = fruits+vege
print(all)
#นายเอกอนันต์ ฮะสุน ม.6/11 เลขที่ 7 