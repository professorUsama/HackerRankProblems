if __name__ == '__main__':
    word_dict = {}
    for size in range(int(input())):
        key = input()
        if key in word_dict:
            word_dict[key] += 1
        else:
            word_dict[key] = 1
    print(len(word_dict))
    for values in word_dict.values():
        print(values,end=" ")