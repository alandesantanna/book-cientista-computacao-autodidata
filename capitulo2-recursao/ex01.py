def cont(n):
    if n > 10:
        return "ok"
    else:
        print(n)
        return cont(n + 1) 
    
print(cont(1))