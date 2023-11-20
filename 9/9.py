if __name__ == "__main__":
  for a in range(1, 1000):
    for b in range(1, 1000 - a):
      if (1000 - a - b)**2 == a**2 + b**2:
        print(a * b * (1000 - a - b))