# value = '11122233445555'
value = 'aaaasssdddbbbcccccc'
def count_frequency(value):
  dct = {}
  for i in value:
    if i not in dct:
      dct[i] =1
    else:
      dct[i] += 1
  return dct

print(count_frequency(value)) 