from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored

init()

print (Fore.GREEN, Back.WHITE, end ='')

def f(n):
    s = int(1);
    for i in range(1, n+1):
        s *= i;
    return s;

def C(n, k):
    return int(f(n) / f(k) / f(n-k))

def g(n):
    s = int(0)
    while n > 0:
        n = int(n/10)
        s += 1
    return s

def h(n):
    s = int(0)
    for k in range (0, n+1):
        s += 1 + g(C(n, k))
        if(k == n):
            s = s-1
    return s

N = int(input())
for n in range(0, N+1):
    m = int((h(N) - h(n))/2)+1
    p = int(0)
    for i in range (0, m-1):
        print(" ", end = '')
    for k in range(0, n+1):
        if n%2 == 0:
            if k%2 == 1:
                print (Fore.RED, end = '')                
        print(C(n, k), ' ', end = '')
        print (Fore.GREEN, end = '')
    print('\n')
input()
