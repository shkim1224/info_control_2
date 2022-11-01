import csv
 
# f = open('example1.csv','r')
# rdr = csv.reader(f)
#  
# for line in rdr:
#     print(line[1])
#  
# f.close()

with open('write1.csv','w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow([1,'림코딩', '부산'])
    wr.writerow([2,'김갑환', '서울'])
    wr.writerow([10,"kim","kunsan"])
 
#f.close()