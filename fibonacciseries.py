def getFilbonacci (numb):
  if (numb <= 0):
    return "incorrect number";
  elif (numb == 1):
    return 0;
  elif (numb == 2):
    return 1;
  return getFilbonacci(numb-1) + getFilbonacci(numb-2)

print(getFilbonacci(5));
