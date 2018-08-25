def bublesort(arr):
  n = len(arr);
  i = n - 1;
  j = 0;
  while(i > 0):
    while(j < n - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1], arr[j];
      j+=1;
    j = 0;
    i-=1;
  return arr;

arr = [54,4,815,2,1];
sorted = bublesort(arr);
for i in sorted:
  print(i);
