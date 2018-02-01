def main():
 a=int(input())
 b=a
 Reverse = 0
 while (a > 0):
     Reminder = a % 10
     Reverse = (Reverse * 10) + Reminder
     a = a // 10


 if Reverse==b:
    print("yes")
 else:
     print("no")


if __name__ == '__main__':
    main()
