import csv
import login

if __name__ == '__main__':
    with open('accounts.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        loginTool = login
        loginTool.login.login(csv_reader)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
