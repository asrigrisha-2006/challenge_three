stu_id = input("Enter your student ID: ")
email = input("Enter your student email id: ")
password = input("Enter your password: ")
code = input("Enter your Referral Code: ")
c = 0
if len(stu_id) != 7 or stu_id[0:3] != "CSE" or stu_id[3] != '-' or not (stu_id[4].isdigit() and stu_id[5].isdigit() and stu_id[6].isdigit()):
    c = 1
elif '@' not in email or '.' not in email or email[0] == '@' or email[-1] == '@' or email[-4:] != '.edu':
    c = 1
if len(password) < 8:
    c = 1
elif not ('A' <= password[0] <= 'Z'):
    c = 1
elif not (password[1].isdigit() or password[2].isdigit() or password[3].isdigit() or
          password[4].isdigit() or password[5].isdigit() or password[6].isdigit() or password[7].isdigit()):
    c = 1
if len(code) != 6 or code[0:3] != 'REF' or not (code[3].isdigit() and code[4].isdigit()) or code[5] != '@':
    c = 1
if c == 0:
    print("APPROVED")
else:
    print("REJECTED")
