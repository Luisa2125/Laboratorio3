import csv
train=[]

with open('./train.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        matrix_train = []
        matrix_file = []
        n = 0
        for i in row:
            matrix_file.append(i)
            if(n == 27):
                matrix_train.append(matrix_file)
                matrix_file = []
                n = -1
            n+=1
        train.append(matrix_train)
    print(len(train),len(train[0]), len(train[0][0]))
    print(train[1][0])

test=[]

with open('./test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        matrix_test = []
        matrix_file = []
        n = 0
        for i in row:
            matrix_test.append(i)
            if(n == 27):
                matrix_test.append(matrix_file)
                matrix_file = []
                n = -1
            n+=1
        test.append(matrix_test)
    print(len(test),len(test[0]), len(test[0][0]))
    print(test[1][0])
    
        
