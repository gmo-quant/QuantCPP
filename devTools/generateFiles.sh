#!/bin/sh
# cmd arg :
#  	arg 1: the file name without postfix.
# 			it is used to generate 
# 			an template of header file
#			an template of class file
# 			an template of tester file 
#			contains the filename  

# use python ./documentTemplates.py <header> <src> <tester>
# to write content to the sets of templates files 
# 
#  	for example:
# 		$./generateFiles.sh Point
#		 
# 		it will generate three template files
#			Point.hpp
#			Point.cpp
#			PointTester.cpp

dir="${HOME}/GMO/CPP/devTools/"
templateFile="${dir}documentTemplates.py"
echo $dir
echo $HOME
if [ $1 == 'help' ]
then 
	echo "./generateFiles <Class name>" 
elif [ -f $1."cpp" ]
then
	echo "Class : $1  is already exist"
else 
	filename=$1
	echo "generating files for Class : $filename"
	src=".cpp"
	header=".hpp"
	tester="Tester.cpp"
	src_file=$filename$src
	header_file=$filename$header
	tester_file=$filename$tester
	touch $src_file
	touch $header_file
	touch $tester_file
	python $templateFile $header_file $src_file $tester_file
fi





