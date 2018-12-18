python3 ngram_mapper.py --file video_name.csv --gram_num 2
cat mapped_gram2.csv | sort --field-separator='\t' --key=1,2 > sorted_mapped.csv
python3 ngram_reducer.py --file sorted_mapped.csv --gram_num 2