# Expense Tracker CLI

A simple command-line expense tracker built in Python. This application allows users to add, delete, list, and summarize expenses while storing data persistently in a CSV file.

Built as part of the roadmap.sh Expense Tracker project.

## Features

* Add expenses
* Delete expenses by ID
* List all expenses
* View total expenses
* View expenses for a specific month
* Persistent CSV storage
* Input validation using argparse
* Automatic CSV file creation

## Installation

Clone the repository:

```bash
git clone https://github.com/Prakhar88/Expense-Tracker-Cli.git
cd Expense-Tracker-Cli
```

## Requirements

* Python 3.8+

No external dependencies are required.

## Usage

### Add an Expense

```bash
python Expenses.py add --amount 100 --description Coffee
```

### List Expenses

```bash
python Expenses.py list
```

### View Total Expenses

```bash
python Expenses.py summary
```

### View Monthly Summary

```bash
python Expenses.py summary --month 6
```

### Delete an Expense

```bash
python Expenses.py delete --id 2
```

## Example Session

```bash
python Expenses.py add --amount 100 --description Coffee
# Expense Added successfully (Id:1)

python Expenses.py add --amount 200 --description Food
# Expense Added successfully (Id:2)

python Expenses.py add --amount 300 --description Books
# Expense Added successfully (Id:3)

python Expenses.py list
# ID    Amt    Desc    Date
# 1     100    Coffee  10-06-2026
# 2     200    Food    10-06-2026
# 3     300    Books   10-06-2026

python Expenses.py summary
# Total expenses:$600

python Expenses.py delete --id 2
# Expense deleted successfully

python Expenses.py list
# ID    Amt    Desc    Date
# 1     100    Coffee  10-06-2026
# 3     300    Books   10-06-2026

python Expenses.py summary
# Total expenses:$400

python Expenses.py summary --month 6
# Total expenses in the month of June:400
```

## Command Reference

### Add

```bash
python Expenses.py add --amount <amount> --description <description>
```

| Argument      | Required | Description                             |
| ------------- | -------- | --------------------------------------- |
| --amount      | Yes      | Expense amount (must be greater than 0) |
| --description | Yes      | Expense description                     |

### Delete

```bash
python Expenses.py delete --id <id>
```

| Argument | Required | Description |
| -------- | -------- | ----------- |
| --id     | Yes      | Expense ID  |

### List

```bash
python Expenses.py list
```

Displays all recorded expenses.

### Summary

```bash
python Expenses.py summary
```

Displays the total of all expenses.

### Monthly Summary

```bash
python Expenses.py summary --month <month>
```

| Argument | Required | Description         |
| -------- | -------- | ------------------- |
| --month  | No       | Month number (1-12) |

## Data Storage

Expenses are stored in:

```text
Expenses.csv
```

CSV Format:

```csv
ID,Amt,Desc,Date
1,100,Coffee,1749542400.123
2,200,Food,1749542500.456
```

Where:

* ID = Expense identifier
* Amt = Expense amount
* Desc = Expense description
* Date = Unix timestamp

## Validation

The application validates:

* Amount must be greater than 0
* Month must be between 1 and 12
* Required arguments must be supplied
* A valid command must be provided

## Project Link

https://roadmap.sh/projects/expense-tracker

## Author

Prakhar Srivastava
