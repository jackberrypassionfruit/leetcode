from math import log

sint = -1563847412

rev, temp = 0, 0
pos_max = "2147483647"
neg_max = "2147483648"

neg = False
fail = False

test_sint = sint

if test_sint < 0:
    neg = True
    test_sint *= -1
    sint *= -1
    
print(test_sint)


# Check if number has more digits than max number
if sint == 0:
    pass
elif log(test_sint, 10) > 10:
    fail = True
    print("too big")
# Great, number is not outright too big. Check if it at least HAS the max number of digits
elif log(test_sint, 10) > 9:
    print("just right")
    if neg:
        for i in range(len(neg_max)):
            # print(f"test_sint ones's dig is {str(test_sint % 10)} and pos_max[i] is {str(pos_max[i])}")
            if test_sint % 10 > int(neg_max[i]):
                fail = True
                break
            elif test_sint % 10 == int(neg_max[i]):
                test_sint //= 10
            else:
                break
    else:
        for i in range(len(pos_max)):
            if test_sint % 10 > int(pos_max[i]):
                fail = True
                break
            elif test_sint % 10 == int(pos_max[i]):
                test_sint //= 10
            else:
                break
else:
    print("too small")
        

while sint > 0 and not fail:
    
    tmp = sint % 10
    sint //= 10
    rev *= 10
    rev += tmp
    
if neg:
    rev *= -1    

if not fail:
    print(rev)
else:
    print("failed")
