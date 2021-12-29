import re
from typing import Text
if __name__ == '__main__':
    testCase = int(input())
    for check in range(testCase):
        if re.match(r'[789]\d{9}$',input()):
            print("YES")
        else:
            print("NO")