path=$1
file=$(echo $path | awk -F/ '{print $2}')
original=$(echo $file | awk -F- '{print $1}')

xxd -b raw/$original.bin | awk '{$1="";print $0}' > diff_tmp1
xxd -b $path | awk '{$1="";print $0}' > diff_tmp2

colordiff -y diff_tmp1 diff_tmp2
rm diff_tmp{1,2}
