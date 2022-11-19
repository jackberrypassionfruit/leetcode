def addBinary_conversion(a, b):
  
  sum = 0
  pow = 0
  a = list(a)
  b = list(b)
  
  for i in range(1, len(a) + 1):
    sum += int(a[-1 * i]) * 2**pow
    pow += 1
  maxPow = pow
  pow = 0
  
  for i in range(1, len(b) + 1):
    sum += int(b[-1 * i]) * 2**pow
    pow += 1
  maxPow = max(pow, maxPow)
  
  print(maxPow)
  print(sum)
    
  res = "0"
  for i in range(maxPow * 2, -1, -1):
    # print(i)
    if sum // 2**i > 0:
      res += "1"
      sum -= 2**i
    else:
      res += "0"
      
  res = res.lstrip("0")
  if res == "":
    res = "0"
  return res

def addBinary(a, b):
  carry = 0
  res = ""
  
  a = list(a)
  b = list(b)
  
  while a or b or carry:
    if a:
      carry += int(a.pop())
    if b:
      carry += int(b.pop())
    res = str(carry % 2) + res
    carry //= 2 
  
  return res
      
a = "11"
b =  "1"
print(addBinary(a, b))