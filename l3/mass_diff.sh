for file in decrypted/*-aes-ecb_delete_byte*; do
  echo -e "\`\`\`bash\n ./diff.sh $file\n\`\`\`\n\`\`\`diff";
  ./diff.sh $file;
  echo -e "\`\`\`";
done
