xxd $1 | awk '{$1="";print $0}' > diff_tmp1
xxd $2 | awk '{$1="";print $0}' > diff_tmp2

colordiff -y diff_tmp1 diff_tmp2
rm diff_tmp{1,2}

