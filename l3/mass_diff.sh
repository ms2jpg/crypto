for file in decrypted/*-aes-cbc_swap*; do
  echo -e "\`\`\`bash\n ./diff.sh $file\n\`\`\`\n\`\`\`diff";
  ./diff.sh $file;
  echo -e "\`\`\`";
done
