def summ_mult(t):
    sum=0
    multi=1
    for i in t:
        sum+=i
        multi*=i
    return sum,multi

a,b=summ_mult(tuple(range(1,2)))
print(f"{a} \n {b}")