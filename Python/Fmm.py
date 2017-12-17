#Github username : yashvermac

# Fast Modulo Multipication calcaulates (a^b)%m in log(b) time
# It is based on the fact (a*b)%m = ((a%m)*(b%m))%m
def fast_mul(base, exp, mod):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res*base)%mod
        base = (base*base)%mod
        exp //= 2
    return res%mod
b, e, m = map(int, input().split())
print (fast_mul(b,e,m))
#wrong implementation was given.. please correct before posting...
