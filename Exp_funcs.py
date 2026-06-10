import time
import csv

def find_ID():
    with open("Expenses.csv","r") as read:
        reader=csv.reader(read)
        last=None
        header=next(reader)
        for row in reader:
            last=row
        if not last:
            return 0
    return int(last[0])

def add(desc,amt):
    ID=find_ID()+1
    Data=[ID,amt,desc,time.time()]
    with open("Expenses.csv","a") as write:
        writer=csv.writer(write)
        writer.writerow(Data)
    print(f"Expense Added successfully (Id:{ID})")

def summary():
    with open("Expenses.csv","r")as read:
        reader=csv.reader(read)
        header=next(reader)
        sum_of_expenses=0
        for row in reader:
            sum_of_expenses+=int(row[1])
    print(f"Total expenses:${sum_of_expenses}")

def delete(id):
    with open("Expenses.csv","r") as read:
        reader=csv.reader(read)
        data=[]
        header=next(reader)
        for row in reader:
            data.append(row)
    for entry in data:
        if int(entry[0])==id:
            data.remove(entry)
            break
    with open("Expenses.csv","w") as write:
        writer=csv.writer(write)
        writer.writerow(header)
        writer.writerows(data)
    print("Expense deleted successfully")

def listing():
    pass

def summary_by_month(month):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    curr=time.localtime()
    if curr.tm_mon < month:
        print("Cannot access future expenses.")
        return
    else:
        sum_by_month=0
        with open("Expenses.csv","r") as read:
            reader=csv.reader(read)
            next(reader)
            for row in reader:
                if time.localtime(float(row[3])).tm_mon==month:
                    sum_by_month+=int(row[1])
        print(f"Total expenses in the month of {months[month-1]}:{sum_by_month}")

def display():
    with open("Expenses.csv","r") as read:
        reader=csv.reader(read)
        headers=next(reader)
        Data=[]
        for row in reader:
            Data.append(row)
    print(f"{headers[0]}    {headers[1]}    {headers[2]}    {headers[3]}")
    for row in Data:
        print(f"{row[0]}  {int(row[1])}  {row[2]}  {time.strftime('%d-%m-%Y',time.localtime(float(row[3])))}")


if __name__ =="__main__":
    add("Coffee",100)
    add("Food",200)
    add("Books",300)

    display()
    summary()

    delete("2")

    display()
    summary()
    summary_by_month(8)
    summary_by_month(4)

