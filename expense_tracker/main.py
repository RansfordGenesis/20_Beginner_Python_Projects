import argparse
import csv
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='Expense Tracker Application')
    parser.add_argument('command', choices=['add', 'view', 'summary'], help='Choose a command')
    parser.add_argument('arguments', nargs='*', help='Arguments for the chosen command')
    return parser.parse_args()

def add_expense(amount, date, category, description):
    with open('expense_tracker/data/expenses.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([amount, date, category, description])

def main():
    args = parse_arguments()

    # Extract the command and arguments from the parsed arguments
    command = args.command
    arguments = args.arguments

    if command == 'add':
        
        if len(arguments) != 4:
            print('Invalid number of arguments supplied. Please try again.')

        else:
            amount, date, category, description = arguments
            add_expense(amount, date, category, description)
            print("Expense added successfully!")

    elif command == 'view':
        #print all expenses
        with open('expense_tracker/data/expenses.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)

add_expense(10, '2023-01-01', 'Other', 'Bought data')


    

if __name__ == '__main__':
    main()

