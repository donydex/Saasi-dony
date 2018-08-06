# For trans java-callgraph(static) to".dot" file 
#!/bin/zsh
OUT=$1".dot"
rm $OUT
echo $OUT
#digraph for directed & graph for undirected
echo "" > $OUT
echo "Before:\n"
wc -l $OUT
wc -l $1".txt"
echo "digraph test {" > $OUT
#sed -E '/^C:/d; /^M:/s/M://g; s/ / -- /; s/\(*\)//1; s/\(*\)//2' callgraph".txt" >> $OUT
#去掉C:开头的行,M:去掉,去掉字母.的组合 加 -- 非贪婪匹配(*)并去掉 ,$和:换成_,末尾加;
sed -E '/^C:/d; /^M:/s/M://g; s/[a-z]+\.//g; s/ / -> /; s/\([^)]*\)//g; s/[\$|:]/_/g; s/$/&;/'\
   $1".txt" >> $OUT
#echo "A -> B;" >> $OUT
echo "}" >> $OUT
#cat $OUT
echo "After:\n"
wc -l $OUT
wc -l $1".txt"
#SVG and PNG are different
dot -Tpng $1".dot" -o $1".png"
#dot -Tsvg $1".dot" -o $1".svg"
# >> means append > means write
sed -E '/^C:/d; /^M:/s/M://g; s/[a-z]+\.//g; s/ / -> /; s/\([^)]*\)//g; s/[\$|:]/_/g; s/$/&;/'\
    $1".txt" > "sed_"$1".txt"
