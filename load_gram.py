import redis, argparse, csv

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', help='csv file that you want to convert', required=True)
    parser.add_argument('--gram_num', required=True,
                        help='Source file encoding')
    parser.add_argument('--local', help='local mode', default=True)
    parser.add_argument('--host', help='Host of the redis server' , default='localhost' )

    r = redis.Redis(host='localhost', port=6379, db=0)

    args = parser.parse_args()

    fn = args.file.split('.')
    key = fn[0] + '_' + args.gram_num + 'gram'
    # Load csv file for redis loading data
    with open(fn[0] + '_reduced_gram' + args.gram_num + '.' + fn[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            print(row)
            r.hset(key, row[0], row[1])


if __name__ == '__main__':
    main()