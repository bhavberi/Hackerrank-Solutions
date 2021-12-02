if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    l.sort()
    i=-2
    m1=l[-1]
    while True:
        if m1==l[i]:
            i-=1
        else: 
            print(l[i])
            break       
    
