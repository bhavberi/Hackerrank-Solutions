if __name__ == '__main__':
    N = int(input())
    arr=list()
    for i in range(N):
        a=input()
        if a.startswith('insert'):
            arr.insert(int(a[7]),int(a[9:]))
        if a=='print':
            print(arr)
        if a.startswith('remove'):
            arr.remove(int(a[7:]))
        if a.startswith('append'):
            arr.append(int(a[7:]))
        if a=='sort':
            arr.sort()
        if a.startswith('pop'):
            arr.pop()
        if a=='reverse':
            arr.reverse()
        
