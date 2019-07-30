#Anna Lieb
#7/5/18
#Summer Python Work
#al_employeeEarnings.py

#used this website to learn more about the formatting in histogram():
#https://www.programiz.com/python-programming/methods/string/format#numbers

EMPLOYEEMONTHLYSALARY = [5000, 10000, 6500, 3600, 2500, 1200, 5100, 7100, 5900,
                         7000, 7800, 3600, 18000, 8400, 5000, 9000, 4500, 9000,
                         7500, 3900, 8000, 3400, 6900, 4800, 2100, 6600, 11000,
                         3700, 8900, 20000, 2700, 3140, 8300, 3900, 3600, 5600,
                         6000, 6200, 2300, 7800, 5100, 4600, 4000, 2900, 3000,
                         5900, 3700, 9400, 9900, 25000, 8800, 3600, 4200, 2400,
                         3300, 6000, 3700, 3000, 3200, 8500, 14000, 5200, 4700,
                         2500, 2900, 7800, 8300, 31000, 4300, 6200, 5400, 8300,
                         7400, 5200, 6500, 8200, 4400, 9400, 8300, 2100, 3600,
                         4100, 6700, 8100, 3200, 2800, 8700, 6200]

NUMOFRESPONSES = len(EMPLOYEEMONTHLYSALARY)
# 390600 is the greatest salary. I found it by executing: print(max(yearlySalary)) in main().

def convertSalary(monthlySalary):
    #converts monthly salary to yearly salary with bonus
    yearlySalary = []
    for x in range(NUMOFRESPONSES):
        yearlySalary.append((monthlySalary[x]*12)*1.05)

    return yearlySalary

def countFrequencies(dataList):
    #organize the survey responses
    rankings = [0] * (40)
    for x in range(0, NUMOFRESPONSES):
        rankings[int(dataList[x]//10000)] += 1

    return rankings

def histogram(rankings):
    #output information to the user
    print ("Employee Annual Earnings Histogram: ")

    for x in range(10):
        print("{:>20}".format("$" + str(x*10000) + " - $" + str((x*10000)+9999)), "*" * rankings[x])
        
    lowerTotal = 0
    for y in range(10,15):
        lowerTotal += rankings[y]
    print("{:>20}".format("$100000 - $149999"), "*" * lowerTotal)

    upperTotal = 0
    for z in range(15, 40):
        upperTotal += rankings[z]
    print("{:>20}".format("$150000 and over"), "*" * upperTotal)

def main():
    yearlySalary = convertSalary(EMPLOYEEMONTHLYSALARY)
    sumData = countFrequencies(yearlySalary)
    histogram(sumData)


main()
