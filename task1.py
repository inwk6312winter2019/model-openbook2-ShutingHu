import csv
def subtask1():
    filename = 'Street_Centrelines.csv'
    tuple = ()
    with open(filename,'rb') as fin:
         reader = csv.reader(fin)
         colunm = [row[2] for row in reader]
         tuple = colunm
         colunm = [row[4] for row in reader]
         subtuple = colunm
         tuple = tuple + colunm
         colunm = [row[6] for row in reader]
         tuple = tuple + colunm
         colunm = [row[7] for row in reader]
         tuple = tuple + colunm
    return tuple;

def subtask2():
    filename = 'Street_Centrelines.csv'
    dic = dict()
    with open(filename,'rb') as fin:
         reader = csv.reader(fin)
         colunm = [row[12] for row in reader]
         dic = {'MAINTENANCE' : colunm}
    return dic

def subtask3():
    filename = 'Street_Centrelines.csv'
    list = []
    with open(filename,'rb') as fin:
         reader = csv.reader(fin)
         colunm = [row[12] for row in reader]
         list = colunm
    return list

def subtask4():
    filename = 'Street_Centrelines.csv'
    list_class_street = []
    with open(filename,'rb') as fin:
         reader = csv.reader(fin)
         colunm = [row[10] for row in reader]
         list_class_street = colunm
    return list_class_street






