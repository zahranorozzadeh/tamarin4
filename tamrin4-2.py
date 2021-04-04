def ab(m,n):
    for i in range(1,m+1):
        if i % 2 == 0:
            for j in range(1,n+1):
                if j % 2 == 0:
                    print('*', end='  ')
                else:
                    print('#', end='  ')    
            print()

rows = int(input())
clumns =int(input())


ab(rows,clumns)
