# TODO

def main():
    size = get_size()
    print_obstacle(size)


def get_size():
    # wait for correct user input
    while True:
        try:
            n = int(input("Height: "))
            if n in range(1, 9):
                return n
        except ValueError:
            pass


def print_obstacle(size):
    # declare counter
    count = size
    # loop and print the correct shape
    for i in range(size):
        for j in range(size):
            if j < count - 1:
                print(" ", end="")
            elif j >= count:
                print("#", end="")
            else:
                print("#", end="")
                count -= 1
        print()


main()