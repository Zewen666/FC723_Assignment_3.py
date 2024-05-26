class GCDAlgorithm:
    def __init__(self):
        pass

    # 标准欧几里得算法
    def compute_gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # 扩展欧几里得算法
    def extended_gcd(self, a, b):
        if b == 0:
            return a, 1, 0
        else:
            gcd, x1, y1 = self.extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y

def get_input():
    while True:
        try:
            a = int(input("Enter the first positive integer: "))
            b = int(input("Enter the second positive integer: "))
            if a > 0 and b > 0:
                return a, b
            else:
                print("Both numbers must be positive integers. Please try again.")
        except ValueError:
            print("Invalid input. Please enter positive integers only.")

if __name__ == "__main__":
    gcd_alg = GCDAlgorithm()
    a, b = get_input()
    gcd = gcd_alg.compute_gcd(a, b)
    print(f"The GCD of {a} and {b} is {gcd}")

    gcd, x, y = gcd_alg.extended_gcd(a, b)
    print(f"The extended GCD results: gcd({a}, {b}) = {gcd}, x = {x}, y = {y}")