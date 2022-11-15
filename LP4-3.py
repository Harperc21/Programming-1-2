def main():
  eggs = int(input("Enter # of eggs purchased: "))
  dozen = eggs // 12.0
  remainder = eggs % 12.0

  if dozen >= 0 and dozen < 4:
    price = 0.50
  elif dozen >= 4 and dozen < 6:
    price = 0.45
  elif dozen >= 6 and dozen < 11:
    price = 0.40
  elif dozen >= 11:
    price = 0.35
  else:
    print("Invalid purchase")

  bill = dozen * price + (remainder * (1.0 / 12.0 * price))
  print("The bill is equal to $ " + str(bill))
  pass


if __name__ == "__main__":
  main()