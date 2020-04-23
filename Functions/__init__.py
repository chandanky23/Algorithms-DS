def isLeapYear(year):
  if year % 100 == 0:
    if year % 400 != 0:
      return False
    return True
  elif year % 4 == 0:
    return True
  return False

if __name__ == "__main__":
  year = int(input())
  print(isLeapYear(year))