#2023/9/13 homework

#1

print("請輸入日期(YYYY-MM-DD)：")
year=input()
month=int(input())
day=int(input())

if month < 10:
  month = "0"+str(month)
if day < 10:
  day = "0"+str(day)

print("日期：%s-%s-%s" %(year, month, day))

#2
name = input("請輸入三人的名字並用空格隔開").split()
weight = input("請輸入三人的體重並用空格隔開").split()
for i in range(3):
  weight[i] = float(weight[i])
print("姓名 地球 月球體重")
print("{}  {:.2f}  {:>.2f}".format(name[0], weight[0], weight[0]*0.17))
print("{}  {:3.2f}  {:>.2f}".format(name[1], weight[1], weight[1]*0.17))
print("{}  {:3.2f}  {:>.2f}".format(name[2], weight[2], weight[2]*0.17))

#3
name = input()
year = input()
print("{}是一位調皮的同學，於{}出生。一天早上，{}醒來時聽到一陣可怕的喧鬧聲：一群殭屍正在朝村莊接近，現在只有{}才能拯救村里的居民......".format(name, year, name, name))
