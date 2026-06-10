import csv
import os
import sys
import argparse
import Exp_funcs

Fields=["ID","Amt","Desc","Date"]
if not os.path.exists("Expenses.csv"):
    with open("Expenses.csv","w") as file:
        writer=csv.writer(file)
        writer.writerow(Fields)
else:
    with open("Expenses.csv","r") as file:
        reader=csv.reader(file)
        fields=next(reader)
    if fields != Fields:
        with open("Expenses.csv","w") as file:
            writer=csv.writer(file)
            writer.writerow(Fields)

def month_valid(month):
    month=int(month)
    if month>12 or month<1:
        raise argparse.ArgumentTypeError("Must be between 1 and 12")
    
    return month  

def value_validation(money):
    money=int(money)
    if money<1:
        raise argparse.ArgumentTypeError("Must be greater than 0")
    return money
Parser=argparse.ArgumentParser()
#Subparser Creation
subParser=Parser.add_subparsers(dest="action",required=True)


#Parsing for Add function
add_money=subParser.add_parser("add")
add_money.add_argument("--amount",type=value_validation,required=True)
add_money.add_argument("--description",type=str,required=True)


#Parsing for summary function
summary=subParser.add_parser("summary")
summary.add_argument("--month",type=month_valid)

#Parsing for List function
listing=subParser.add_parser("list")

#Parsing for delete

delete=subParser.add_parser("delete")
delete.add_argument("--id",type=int,required=True)


#Parsing
Args=Parser.parse_args()



if Args.action=="add":
    Exp_funcs.add(Args.description,Args.amount)
elif Args.action=="list":
    Exp_funcs.display()
elif Args.action=="summary":
    if Args.month==None:
        Exp_funcs.summary()
    else:
        Exp_funcs.summary_by_month(Args.month)
elif Args.action=="delete":
    Exp_funcs.delete(Args.id)





