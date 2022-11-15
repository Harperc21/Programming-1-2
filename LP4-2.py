def main():
  weight = int(input("Enter # of kilograms: "))
  length = int(input("Enter # of centimeters: "))
  width = int(input("Enter # of centimeters: "))
  height = int(input("Enter # of centimeters: "))

  if weight > 27:
    print("too heavy")
  elif length > 100000:
    Print("too long")
  elif width > 100000:
    print("too wide")
  elif height > 100000:
    print("too tall")
  else:
    print("normal")
  pass


if __name__ == "__main__":
  main()