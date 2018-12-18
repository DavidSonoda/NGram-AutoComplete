
gram_arr=(1 2 3 4 5)

n_gram_process() {
    num=$1
    echo "Mapping stage of ${num}-gram"
    python3 ngram_mapper.py --file video_name.csv --gram_num $num
    echo "Soring results..."
    cat video_name_stage0_gram${num}.csv | sort -t '\t' -k1,1 -k2,2 > video_name_stage0_gram${num}_sorted.csv
    echo "First reducing stage..."
    python3 ngram_reducer.py --file video_name.csv --gram_num $num
    echo "Second reducing stage..."
    cat video_name_stage1_gram${num}.csv | sort -t '\t' -k1,1 -k3,3n > video_name_stage1_gram${num}_sorted.csv
    python3 ngram_secondary_reducer.py --file video_name.csv --gram_num $num
    echo "Completing..."
    rm -r video_name_stage*
}


for t in ${gram_arr[@]}; do
    n_gram_process $t
done