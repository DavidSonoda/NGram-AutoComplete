import csv, json, argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', help='csv file that you want to convert', required=True)
    parser.add_argument('--gram_num', required=True,
                        help='Source file encoding')
    parser.add_argument('--local', help='local mode', default=True)

    args = parser.parse_args()
    gram_num = args.gram_num
    local_mode = args.local

    with open('mapped_tmp_gram' + gram_num + '.csv', 'w') as mapped:
        with open(args.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            last_key = ''
            last_value = 0

            for row in csv_reader:
                # print(row)
                key = '\t'.join([row[i] for i in range(0,2)])
                value = int(row[2])
                if key == last_key:
                    last_value = value + last_value
                else:
                    if not local_mode:
                        print(last_key + '\t' + str(last_value))
                    else:
                        mapped.write(last_key + '\t' + str(last_value) + '\n')
                    last_value = value
                    last_key = key


if __name__ == '__main__':
    main()