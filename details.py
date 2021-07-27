import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["NAME", "AGE", "CONTACT - NO", "E - mail"])

        writer.writerow(info_list)

if __name__=='__main__':
condition = True

while condition:
    student_detail = input("Enter student details in the following format(Name Age Contact-num E-mail-Id)")

    student_detail_list = student_detail.split(' ')
    print("\nThe entered information is:\nName:{}\nAge:{}\nContact number:{}\nE-mail:{}\n"
          .format(student_detail_list[0],student_detail_list[1],student_detail_list[2],student_detail_list[3]))
    write_into_csv(student_detail_list)
    student_check=input("Is the entered information correct:Yes/No")
    if student_check=='Yes':
        write_into_csv(student_detail_list)

        condition_check = input("Enter yes/no if you want to enter details for another student: ")
        if condition_check == 'yes':
            condition = True
        elif condition_check == 'no':
            condition = False
    elif student_check == 'No':
        print("Enter the correct details")