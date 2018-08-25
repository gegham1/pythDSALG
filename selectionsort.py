def selectionsort (arr):
  i = 0;
  while (i < len(arr)):
    min = i;
    j = i;
    while (j < len(arr)):
      if (arr[j] < arr[min]):
        min = j;
      j+=1;
    arr[i], arr[min] = arr[min], arr[i];
    i+=1; 
  return arr;

arr = [6,2,8,1,5];
sorted = selectionsort(arr);
for i in sorted:
  print(i);
