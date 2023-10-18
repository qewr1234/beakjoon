Money = {'Quarter': 25, 'Dime': 10, 'Nickel': 5, 'Penny': 1}

num = int(input())

for i in range(num):
    arr = int(input())
    Q = 0
    D = 0
    N = 0
    P = 0
    
    while arr >= Money['Quarter']:
        arr = arr - Money['Quarter']
        Q += 1
        
    while arr >= Money['Dime'] and arr < Money['Quarter']:
        arr = arr - Money['Dime']
        D += 1
        
    while arr >= Money['Nickel'] and arr < Money['Dime']:
        arr = arr - Money['Nickel']
        N += 1
        
    while arr >= Money['Penny'] and arr < Money['Nickel']:
        arr = arr - Money['Penny']
        P += 1
    print(Q, D, N, P) 
