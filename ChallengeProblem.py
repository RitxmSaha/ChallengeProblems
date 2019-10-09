divisor = 0
dividend = 0
FoundSolution = False


def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1


for i in range(999):
    dividend = 0
    divisor += 0.01
    for x in range(99):
        dividend += .1
        divisor = round(divisor, 2)
        dividend = round(dividend, 1)
        if (num_after_point((dividend / divisor))) == 3:
            if len(list(str(dividend / divisor))) == 5:
                if int(list(str(dividend / divisor))[2]) == 0:
         #           k = float("0" + "".join(list(str(dividend/divisor))[1:]))
  #                  print(k)

