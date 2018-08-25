def insertionsort (arr):
  i = 1;
  while (i < len(arr)):
    j = i;
    while (j > 0):
      if (arr[j] < arr[j-1]):
        arr[j], arr[j-1] = arr[j-1], arr[j];
      j-=1;
    i+=1;
  return arr;

arr = [54,4,815,2,1];
sorted = insertionsort(arr);
for i in sorted:
  print(i);

