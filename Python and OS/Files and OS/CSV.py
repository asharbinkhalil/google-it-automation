import csv
# generating csv
# hosts=[['local','192.168.1.1','Easy'],['remote','192.168.1.2','Difficult']]
# with open("csv_file.txt",'w') as csv_f:
#     writer=csv.writer(csv_f)
#     writer.writerows(hosts)


# reading file
# https://docs.python.org/3/library/csv.html

# https://realpython.com/python-csv/
f=open ("csv_file.txt")
reader= csv.reader(f)
for row in reader:
    name,ip,mode=row
    print("Name : {}, Ip : {}, Mode : {} ".format(name,ip, mode))


    