def countdown(countdown):
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print('Blastoff!')
    return True

if __name__ == '__main__':
    assert countdown(5) == True