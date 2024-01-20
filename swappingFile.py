def swappingFileData():
    ask1 = input("Please type in your first file name:")
    ask2 = input("Please type in your second file name:")

    with open(ask1, 'r') as a:
        data_a = a.read()

    with open(ask2, 'r') as b:
        data_b = b.read()

    with open(ask1, 'w') as a:
        a.write(data_b)

    with open(ask2, 'w') as b:
        b.write(data_a)

swappingFileData()