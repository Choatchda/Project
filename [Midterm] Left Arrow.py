"""[Midterm] Left Arrow"""
def main():
    """solution"""
    width = int(input())
    high = int(input())
    space = high//2
    for i in range(high):
        print (("*"*width) + (" "*space))
        if i < high//2:
            space -= 1
        else:
            space += 1
main()
