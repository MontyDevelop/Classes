# Create a code to find th mean, median and mode of the data

# data = [60,70,80,90]
# sum = data[0]+data[1]+data[2]+data[3]
# no_of_data = len(data)
# mean_of_data = sum / no_of_data
# print(mean_of_data)
# median = (data[1]+data[2]) / 2
# print(median)



# list2 = [2,2,3,4,5,6,2,2,6,7,2,10,11]

# for i in list2:
#     if 2 == > 1


import numpy as np
from scipy import stats

data = [60,70,80,90,70,20,50,70]
arra1 = np.array(data)
print(np.mean(arra1))
print(np.median(arra1))
print(stats.mode(arra1))

