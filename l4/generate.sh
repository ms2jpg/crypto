for ((i=1;i<=3;i++)); do
  python3 bbs.py 20000 > 20k-$i.txt 2> 20k-$i.seed
done

for ((i=1;i<=1;i++)); do
  python3 bbs.py 1000000 > 1kk-$i.txt 2> 1kk-$i.seed
done