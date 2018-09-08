def main():
    a = [[int(x) for x in input().split()] for _ in range(6)]
    
    m = -9999
    
    for i in range(1,5):
        for j in range(1,5):
            
            sum = a[i][j]+a[i-1][j]+a[i-1][j-1]+a[i-1][j+1]+a[i+1][j]+a[i+1][j-1]+a[i+1][j+1]
            
            if sum > m:
                m = sum
    
    print(m)

main()
            
            
