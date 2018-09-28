#sampling probability
#according to population's number and population's mean and std
#calculating to sample's std

import math

while(True):
    groupnumber=float(input("group number:"))
    samplenumber=float(input("sample number"))
    popmean=float(input("population's mean:"))
    popstd=float(input("population's standard deviation:"))

    samplestd= popstd/(math.sqrt(samplenumber)) * math.sqrt((groupnumber-samplenumber)/(groupnumber-1))
    print(samplestd)
    break
