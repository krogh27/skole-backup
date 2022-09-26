import datetime
from shutil import copytree

date_backup = datetime.datetime.now()
# save year, month, date and time in str_date_backup variable
str_date_backup = date_backup.strftime("%Y-%m-%d.%H.%M.%S")
# select file or files to be included in backup and set destination
path_input = r'/Users/mks/Desktop/test1'
path_output = r'/Users/mks/Desktop/test2/' + str_date_backup + '.backup'
check = True


def fullbackup():
    copytree(path_input, path_output)


while check:
    user_input = int(input(
        "Welcome to Mathias' backup script \nPlease select option 1, 2 or 3 \n 1. full backup \n 2. differential backup\n 3. exit\n"))
    if user_input == 1:
        fullbackup()
        print("Full backup finished")
        check = False
    elif user_input == 2:
        print("Work in progress.. Differential backup is in development state, please select another backup option")
    elif user_input == 3:
        break
    else:
        print("Wrong input, try again..")
