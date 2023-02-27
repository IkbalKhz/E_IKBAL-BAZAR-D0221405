data = [0, 2, 2, 1, 4, 0, 5]
n = len(data)
if n % 2 == 0:
    median1 = data[n//2]
    median2 = data[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = data[n//2]
print("median : " + str(median))
