import csv

def writeCsv(path, data):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)


path = r"E:\python\office文件操作\1.读写CSV文件\test.csv"
writeCsv(path, [[1,2,3], [4,5,6], [7,8,9]])