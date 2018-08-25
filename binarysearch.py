def binarysearch (arr, item):
  n = len(arr);
  middle = int(round(n / 2));
  if (n <= 1):
    return arr[0];
  if (arr[middle] == item):
    return arr[middle];
  elif (item > arr[middle]):
    return binarysearch(arr[middle:n], item);
  elif (item < arr[middle]):
    return binarysearch(arr[0:middle], item);

arr = [1,2,3,4,5,8];
print(binarysearch(arr, 2));
