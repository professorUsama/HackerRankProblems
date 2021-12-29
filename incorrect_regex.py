import re
if __name__ == '__main__':
    for check in range(int(input())):
        try:
            re.compile(input())
            output = True
        except re.error as e:
            output = False
            print(e)
        print(output)
