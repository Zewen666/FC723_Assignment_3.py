"""
Pseudocode

PROCESS GCD
a!=0
b!=0

WHILE
IF b>a THEN SWAP a,b
r = a%b
IF r=0 THEN PRINT "The GCD(NUMBER A,NUMBER B) is: ", b , EXIT WHILE
ELSE
a=b
b=r
END WHILE

END

"""


def gcd(a, b):
    while True:
        if b > a:
            a, b = b, a
        if b==0:
            return a
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r
            print(a, b)


def is_int(t_str) -> bool:
    try:
        t_int = int(t_str)
        if t_int > 0:
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == '__main__':
    while True:
        str_a = input("Enter first number A: ")
        if is_int(str_a):
            int_a = int(str_a)
            break
        else:
            print("Not a number or number <= 0")
    while True:
        str_b = input("Enter second number B: ")
        if is_int(str_b):
            int_b = int(str_b)
            break
        else:
            print("Not a number or number <= 0")
    gcd_number = gcd(int_a, int_b)
    print('GCD(' + str_a + ',' + str_b + ')=', gcd_number)
