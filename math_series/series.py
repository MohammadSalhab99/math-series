
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
    


def locus(n):
    if n==0:
        return 2
    if n==1:
        return 1
    else:
        return locus(n-2)+locus(n-1)

def sum_series(n,n1=0,n2=1):
  if n1 == 0 and n2 == 1:
    return fibonacci(n)
  elif n1 == 2 and n2 == 1:
    return locus(n)
  else:
      if n==0:
        return n1
      if n==1:
        return n2
      else:
        return sum_series(n-2,n1,n2)+sum_series(n-1,n1,n2)
