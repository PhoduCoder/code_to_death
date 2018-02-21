def factorial(x):
    fact=1
    if(x==0): fact=1
    for i in range(1,x+1):
        fact = fact*i
    return fact
    #print fact

def main():
    result = factorial(5)
    print result
    #factorial(8)
if __name__ == "__main__":
    main()
