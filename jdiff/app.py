import pprint

def run():
    file1 = 'test1.txt'
    file2 = 'test2.txt'
    out1 = ''
    out2 = ''

    pp = pprint.PrettyPrinter(indent=2, width=80)
    with open(file1, 'r') as file_1:
        with open(file2, 'r') as file_2:
            file_1 = file_1.read()
            file_2 = file_2.read()

            out1 = pp.pformat(file_1)
            out2 = pp.pformat(file_2)

    print(out1)
    print(out2)
