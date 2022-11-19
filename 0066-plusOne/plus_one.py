def plusOne(digits):        
  over9000 = True
  for i in range(len(digits) - 1, -1, -1):
    print(i)
    if digits[i] != 9:
      digits[i] += 1
      over9000 = False
      break
    else:
      digits[i] = 0
  if over9000:
    digits.insert(0, 1)



arr = [9, 9, 9, 9]
plusOne(arr)