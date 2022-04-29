#! /usr/bin/bash

calc()
{
	case $b in
		"+"|"-"|"*"|"/"|"%"|"**") let "k = $a $b $c";;
		*) echo "error"
		exit;;
	esac
	echo "$k"
}

while true
do
	read a b c
	if [[ "$a" == "exit" || "$b" == "exit" || "$c" == "exit" ]]
	then
		echo "bye"
		break
	elif [[ -z $a || -z $b || -z $c ]]
	then
		echo "error"
		break
	else calc  a b c
	fi
done
