xd=delete_byte
for file in decrypted/*-aes-ctr_$xd*; do
  echo -e "\`\`\`bash\n ./diff.sh $file\n\`\`\`\n\`\`\`diff";
  ./diff.sh $file;
  echo -e "\`\`\`";
done
