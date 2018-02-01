def main():
 a=int(input())
 n=int(input())
 num=[]
 b=0
 for i in range(a):
     num.append(input())

 for y in range(n):
     b=b+int(num[y])
 print(b)
if __name__ == '__main__':
    main()
