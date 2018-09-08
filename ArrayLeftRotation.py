def main():
    
    n,d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    d = {i : a[(i + d % n)% n]for i in range(n)}
        
    for i in d:
        print(d[i],end=" ")
        
main()
