import sys
import os


def read_data(filename):
    data = list()
    with open(filename, 'rt') as fw:
        data = fw.readlines()
    print('read ok')
    pages = list()
    curr_page = list()
    for x in data:
        if x == '1\n':
            pages.append(curr_page)
            curr_page = list()
        else:
            curr_page.append(x)
    return pages

def add_highlist(pages):
    for page in pages:
        page.append("@highlight\n")
        page[-1], page[-2] = page[-2], page[-1]
    return pages

def main():
    filename = sys.argv[1]
    pages = read_data(filename)
#    pages = add_highlist(pages)
    for i in range(0, len(pages)):
        with open('new_data/' + str(i) + '.txt', 'wt') as fw:
            for each in pages[i]:
                fw.write(each)
                fw.write('\n')
        print("page{} ok".format(i))


os.system('mkdir new_data')
main()

