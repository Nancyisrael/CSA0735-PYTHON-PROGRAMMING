import statistics
elements=[16,18,27,16,23,21,19]
mean=sum(elements)/len(elements)
median=statistics.median(elements)
mode=statistics.mode(elements)
print("mean: ",mean)
print("median : ",median)
print("mode : ",mode)

