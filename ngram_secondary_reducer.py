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
    fn = args.file.split('.')

    with open(fn[0] + '_reduced_gram' + gram_num + '.csv', 'w') as reduced:
        with open(fn[0] + '_stage1_gram' + gram_num + '_sorted.' + fn[1]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            last_key = ''
            last_value = []

            for row in csv_reader:
                # print(row)
                if len(row) < 3:
                    continue
                key = row[0]

                value = {
                    'text': row[1],
                    'freq': int(row[2])
                }
                if key == last_key:
                    # Reduce value
                    last_value.append(value)
                else:
                    if not local_mode:
                        print(last_key + '\t' + json.dumps(last_value))
                    else:
                        reduced.write(last_key + '\t' + json.dumps(last_value, ensure_ascii=False) + '\n')
                    last_value = []
                    last_value.append(value)
                    last_key = key


if __name__ == '__main__':
    main()