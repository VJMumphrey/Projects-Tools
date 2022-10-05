#!/usr/bin/bash

# runs tools and documents the results
# each tool should have its own header for easy searching
# header format = "toolname:"

# setup args
file_name=$1
touch results.txt
results=results.txt


# setup

# args, results
newline () {
	echo -e "\n" >> $results
}

# args, headername results
header () {
	local header_name=$1
	local result_file=$2
	if [ $header_name == "file" ]; then
		echo -e "$header_name:\n" > $result_file
	else
		echo -e "$header_name:\n" >> $result_file
	fi

}

# script flow
# file command
header "file" $results
file $file_name >> $results	
newline $results

# shasums
header "shasums" $results

# sha1 
echo "sha1-" >> $results
sha1sum $file_name >> $results
newline $results

# sha256
echo "sha256-" >> $results
sha256sum $file_name >> $results
newline $results

# sha512
echo "sha512-" >> $results
sha512sum $file_name >> $results
newline $results

# strings
header "strings" $results
strings $file_name >> $results
newline $results

# ldd
header "ldd" $results
ldd $file_name >> $results
newline $results

# nm
header "nm" $results
nm $file_name >> $results
newline $results

# objdump
header "objdump" $results
objdump -M intel -d $file_name >> $results
newline $results

# readelf
header "readelf" $results
readelf -a $file_name >> $results
newline $results

# detect packers

# upx
header "upx" $results
strings $file_name | grep "upx" >> $results
newline $results

