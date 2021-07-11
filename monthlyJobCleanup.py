import calendar
from genericpath import exists
import os
from datetime import date
from os import listdir
import re


def main():
    # move to the correct folder
    current_folder = r'/Users/briandunn/Documents/Job_Search_2021'
    os.chdir(current_folder)

    # dynamically assign last month as a number to a variable
    last_month = str(date.today())
    last_month = last_month.split('-')
    last_month = int(last_month[1]) - 1

    # create new folder within the Job_Search_Folder
    folder_to_create = calendar.month_name[last_month] + ' Resumes'
    # print('folder_to_create: ', folder_to_create)
    full_new_folder_path = os.path.join(
        current_folder + r'/' + folder_to_create)

    if not(os.path.exists(full_new_folder_path)):
        os.mkdir(full_new_folder_path)

    # find all folders with dates within last month and place into a list
    all_files = [x for x in listdir(os.getcwd()) if not(
        x.endswith(('pdf', 'docx', 'rtf', 'txt', 'Store', 'points', 'py', 'Cheat Sheets', 'Resumes', 'Interviews')))]
    print('the length of all files is ', len(all_files))
    folders_to_move = [x for x in all_files if
                       int(x.split('-')[1]) == last_month]

    # move those folders to the newly created folder
    for x in folders_to_move:
        each_cmd = os.path.join('mv -v ' + x + ' \'' +
                                str(folder_to_create) + '\'')
        os.system(each_cmd)


if __name__ == '__main__':
    main()
