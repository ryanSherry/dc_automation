import csv

from login import Login

if __name__ == '__main__':
    with open('accounts.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        loginTool = Login
        loginTool.login(loginTool, csv_reader)
    csv_file.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
