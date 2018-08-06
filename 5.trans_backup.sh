# For trans java-callgraph(static) to dot file 
#!/bin/zsh
OUT=callgraph.dot
echo "graph test {" > $OUT
#sed -E '/^C:/d; /^M:/s/M://g; s/ / -- /; s/\(*\)//1; s/\(*\)//2' callgraph.txt >> $OUT
#去掉C:开头的行,M:去掉,去掉字母.的组合 加 -- 非贪婪匹配(*)并去掉 ,$和:换成_,末尾加;
sed -E '/^C:/d; /^M:/s/M://g; s/[a-z]+\.//g; s/ / -- /; s/\([^)]*\)//g; s/[\$|:]/_/g; s/$/&;/' callgraph.txt >> $OUT
echo "}" >> $OUT
cat $OUT
#dot -Tpng callgraph.dot -o callgraph.png
dot -Tsvg callgraph.dot -o callgraph.svg

sed -E '/^C:/d; /^M:/s/M://g; s/[a-z]+\.//g; s/ / -- /; s/\([^)]*\)//g; s/[\$|:]/_/g; s/$/&;/' callgraph.txt >> sed_callgraph.txt
