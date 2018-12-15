import jieba as jb
import argparse
import csv
import json

def main():
    """
    Read from a csv file, split chinese words, map them in the format of {key: word/phrase, value: word/phrase }.
    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', help='csv file that you want to convert', required=True)
    parser.add_argument('--gram_num', required=True,
                        help='Source file encoding')

    args = parser.parse_args()
    gram_num = args.gram_num


    print(args.file)
    with open(args.file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            seg_list = list(jb.cut(row[0]))
            # print(seg_list)
            map_n_gram(seg_list, gram_num)

def map_n_gram(arr, n):
    """
    Map a list of chinese words to n-gram record.
    :param arr: Array of chinese words separated using jieba
    :param n: N-gram's N
    """
    length = len(arr)
    end = length - int(n)
    if end <= 0:
        return
    for i in range(0, end):
        for j in range(i, end):
            key = concat_arr(arr[i:j+1])
            value = concat_arr(arr[j+1:j+6])
            if brackets_closed(value):
                print(key + '\t' + value)


def concat_arr(arr):
    """
    Concatenate a array of Chinese words to a whole string.
    :return: A concatenated string
    """
    return ''.join(str(x) for x in arr)

def brackets_closed(str):
    """
    Ensure the brackets in the str, if exists, are closed.
    :param str: The string to be analyzed
    :return: Boolean
    """
    with open('./config.json') as config_file:
        config = json.load(config_file)
    brackets = config["mapper"]["brackets"]
    b_opening = set(brackets["opening"])
    b_closing = set(brackets["closing"])

    b_stack = []
    for c in str:
        if c in b_opening:
            b_stack.append(c)
        if c in b_closing:
            if len(b_stack) == 0:
                return False
            if c != b_stack[0]:
                return False
            else:
                b_stack.pop()

    return len(b_stack) == 0


if __name__ == "__main__":
    main()