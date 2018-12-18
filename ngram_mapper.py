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
    parser.add_argument('--local', help='local mode', default=True)

    args = parser.parse_args()
    gram_num = args.gram_num

    local_mode = args.local
    mapped = open('mapped_gram' + gram_num + '.csv', "w")
    # print(args.file)
    with open(args.file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            seg_list = list(jb.cut(row[0]))
            # print(seg_list)
            map_n_gram(seg_list, gram_num, local_mode, mapped)

def map_n_gram(arr, n, local_mode, file):
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
            if not is_valid_key(key):
                continue
            value = concat_arr(arr[j+1:j+6])
            if brackets_closed(value):
                if not local_mode:
                    print(key + '\t' + value + '\t1')
                else:
                    file.write(key + '\t' + value + '\t' + '1\n')


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

    if len(b_opening) != len(b_closing):
        print('Brackets config not valid, please check config.py')
        return

    b_open_m = {}
    b_close_m = {}
    for i in range(0, len(b_opening)):
        b_open_m[brackets['opening'][i]] = i
        b_close_m[brackets['closing'][i]] = i

    b_stack = []
    for c in str:
        if c in b_opening:
            b_stack.append(c)
        if c in b_closing:
            if len(b_stack) == 0:
                return False
            elif b_close_m[c] != b_open_m[b_stack[0]]:
                return False
            elif b_close_m[c] == b_open_m[b_stack[0]]:
                b_stack.pop()

    return len(b_stack) == 0

def is_chn_char(c):
    return c >= u'\u4e00' and c <= u'\u9fff'

def is_valid_key(key):
    """
    Determines if a key is valid
    :param key:
    :return:
    """
    for c in key:
        if is_chn_char(c):
            return True
    return False

if __name__ == "__main__":
    main()