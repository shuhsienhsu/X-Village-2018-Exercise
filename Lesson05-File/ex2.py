import csv

count = 0
with open('ex2.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    
    data = 78*[0]
    i = 0

    for row in reader:
        count += 1
        data[i] = row
        #print(data[i])
        i += 1
    
    #print(count)

    min = int(data[1][2])
    #print(min)
    for j in range(2,count):
        if(int(data[j][2]) < min):
            min = int(data[j][2])
            min_city = j
            #print(j, min)

    print(data[min_city][0]+"空氣最好，AQI是"+str(min))