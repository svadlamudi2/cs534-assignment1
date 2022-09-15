import csv

def readCSV(file):
    data = []
    with open(file, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            tempList = []
            for value in row:
                if value == '':
                    tempList.append(0)
                else:
                    tempList.append(int(value))
            data.append(tempList)

    return data

print(readCSV('board.csv'))
