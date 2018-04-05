def creat_matrix():
    while True:
        try:
            rnum = int(input("請輸入矩陣列數: "))
            cnum = int(input("請輸入矩陣行數: "))

        except ValueError:
            print("請重新輸入數字")
        else:
            break

    matrix = [[0 for i in range(cnum)] for j in range(rnum)]
    for i in range(rnum):
        while True:
            row = input("請輸入第%d列元素,以空格間隔: " %(i+1))
            row = row.split()
            if len(row) != cnum:
                continue
            try:
                for j in range(cnum):
                    matrix[i][j] = int(row[j])
            except ValueError:
                continue
            else:
                break

    print("%d X %d的矩陣如下: " %(rnum, cnum))

    for i in range(rnum):
        for j in range(cnum):
            print("{:3}".format(matrix[i][j]), end = '')
        print()

    return matrix

def mplus(a, b):
    m = len(a)
    n = len(a[0])
    if len(b) == m and len(b[0]) == n:
        c = [[a[i][j]+b[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                print("{:3}".format(c[i][j]), end = '')
            print()

    else:
        print("請重新定義相加的矩陣，維度必須相等")

