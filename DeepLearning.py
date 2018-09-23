import csv


def getTrain():
    train=[]
    valor=[]
    with open('./train.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        label = 0
        for row in readCSV:
            matrix_train = []
            matrix_file = []
            n = 0
            if label != 0:
                for i in row:
                    if n == 0:
                        valor.append(i)
                    if n != 0 :
                        matrix_file.append(i)
                    if(n == 28):
                        matrix_train.append(matrix_file)
                        matrix_file = []
                        n = 0
                    n+=1
                train.append(matrix_train)
            label = 1
        #print(len(valor))
        return train, valor
        #print(len(train),len(train[27]),len(train[27][0]))
        #print(train[0])

def getTest():
    test=[]
    with open('./test.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        label = 0
        for row in readCSV:
            matrix_test = []
            matrix_file = []
            n = 0
            if label != 0:
                for i in row:
                    matrix_file.append(i)
                    if(n == 27):
                        matrix_test.append(matrix_file)
                        matrix_file = []
                        n = -1
                    n+=1
                test.append(matrix_test)
            label = 1
        return test
        #print(len(train),len(train[27]),len(train[27][0]))
    
        
