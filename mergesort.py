def mergesort (arr):
  n = len(arr);
  middlePoint = int(round(n / 2));
  if (n <= 1):
    return arr;
  else:
    left = mergesort(arr[0:middlePoint]);
    right = mergesort(arr[middlePoint:n]);
    return merge(left, right);

def merge (arr1, arr2):
  merged = [];
  temp1 = 0;
  temp2 = 0;
  i = 0;
  while (i < len(arr1) + len(arr2)):
    if (temp1 < len(arr1) and temp2 < len(arr2) and arr1[temp1] < arr2[temp2]):
      merged.append(arr1[temp1]);
      temp1+=1;
    elif (temp1 < len(arr1) and temp2 < len(arr2) and arr1[temp1] >= arr2[temp2]):
      merged.append(arr2[temp2]);
      temp2+=1;
    elif (temp1 >= len(arr1) and temp2 < len(arr2)):
      merged.append(arr2[temp2]);
      temp2+=1;
    elif (temp2 >= len(arr2) and temp1 < len(arr1)):
      merged.append(arr1[temp1]);
      temp1+=1;
    i+=1;
  return merged;


arr = [6,70,6,0,6,1];
merged = mergesort(arr);
for i in merged:
    print(i);
