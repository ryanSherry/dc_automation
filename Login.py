import sys, argparse, csv


class Login:
    def login:
        with open('accounts.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                email = row['email']
                password = row['password']
                print(email)
                print(password)
            csv_file.close()
