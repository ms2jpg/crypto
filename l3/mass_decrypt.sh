for file in corrupted/*-aes-cbc_*; do
  echo $file
  ./decrypt.sh $file;
done
