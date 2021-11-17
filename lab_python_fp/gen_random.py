import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        number = random.randrange(begin, end)
        yield number
        #print(number)
    pass

def main():
    data = list()
    for i in gen_random(5, 1, 3):
        data.append(i)
    print(data)
if __name__ == "__main__":
    main()
