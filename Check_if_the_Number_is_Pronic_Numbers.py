import math

# function to check Pronic Number
def pronic_check(n):
    x = (int)(math.sqrt(n))

    # Checking Pronic Number by multiplying
    # consecutive numbers
    if (x * (x + 1) == n):
        return True
    else:
        return False

# Driver Code
n = 98

if (pronic_check(n) == True):
    print("YES")
else:
    print("NO")