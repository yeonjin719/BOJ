import sys
print = sys.stdout.write
input = sys.stdin.readline
M = int(input())
S =0b0

for i in range(M):
    order = input()
    if order == "all\n":
        S = 0b111111111111111111111
    elif order == "empty\n":
        S = 0b0
    else:
        order_ed, x = order.split()
        x = int(x)
        if order_ed == "add":
            S = S | (0b1 << x)
        elif order_ed == "remove":
            S = S & ~(0b1 << x)
        elif order_ed == "check":
            if (S&(0b1<<x)):
                print('1')
            else:
                print('0')
        else:
            S = S ^ (0b1<<x)