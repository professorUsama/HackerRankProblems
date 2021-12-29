if __name__ == '__main__':
    size = int(input())
    country_name = set()
    for country in range(size):
        country_name.add(input())
    print(len(country_name))