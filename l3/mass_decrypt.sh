for file in corrupted/*-aes-ecb_delete_byte*; do
  ./decrypt.sh $file;
done
