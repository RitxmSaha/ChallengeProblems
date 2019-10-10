divisor = 0
for i in range(999):
    dividend = 0
    divisor += 0.01
    for z in range(99):
        dividend += .1
        x = round(100 * divisor)
        y = round(100 * dividend)
        dividend = round(dividend, 1)
        divisor = round(divisor, 2)
        k = y % x
        if k != 0:
            if k * 10 % x == k * 10:
                if k * 100 % x == k * 100:
                    if k * 1000 % x == 0:
                        print(dividend, divisor)