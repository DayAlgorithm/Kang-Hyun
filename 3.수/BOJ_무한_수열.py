N, P, Q = map(int, input().split())
ref = {0:1}
entry_finder = set([0])

def dp(n,p,q):
    if n in entry_finder:
        return ref[n]
    else:
        An = dp(n//p,p,q) + dp(n//q,p,q)
        ref[n] = An
        entry_finder.add(n)
        return An

print(dp(N,P,Q))