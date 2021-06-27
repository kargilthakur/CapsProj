i = int(input())
splitup = {}
if i % 2000 == 0:
  splitup[2000] = int(i/2000)
elif i % 500 == 0:
  splitup[500] = int(i/500)
elif i % 200 == 0:
  splitup[200] = int(i/200)
elif i % 100 == 0:
  splitup[100] = int(i/100)
else:
  print("This value cannot be dispensed")
for key,value in splitup.items():
  print("{} notes of {} are dispensed".format(value,key))
