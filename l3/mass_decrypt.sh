for file in corrupted/*-aes-ctr_*; do
  echo $file
  ./decrypt.sh $file;
done
