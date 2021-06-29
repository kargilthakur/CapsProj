from tts import notestts,cantBdispense,aur, ultimate
def nota(i):
  count = 0
  total = 0
  splitup = {}
  if i >= 2000:
    splitup[2000] = int(i//2000)
    i = i - splitup[2000]*2000
  if i >= 500:
    splitup[500] = int(i//500)
    i = i - splitup[500]*500
  if i >= 200:
    splitup[200] = int(i//200)
    i = i - splitup[200]*200
  if i >= 100:
    splitup[100] = int(i//100)
    i = i - splitup[100]*100
  if i != 0:
    cantBdispense()
    return None
  for key,value in splitup.items():
    count += 1
    total += value
    if count > 1 and count <= len(splitup):
      aur()
    notestts(key,value)

  ultimate(total)
    
