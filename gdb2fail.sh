#!/bin/sh

if test "$#" -eq 0
then
    echo usage: $0 beehive log files
    exit 1
fi

sum=
for f in "$@"
do
    echo $f
    pid=`basename $f | sed -e 's/^[^0-9]*-\([0-9]*\)-\([^-]*\)-.*$/\1/'`
    isa=`basename $f | sed -e 's/^[^0-9]*-\([0-9]*\)-\([^-]*\)-.*$/\2/'`
    # begin 644 gdb-i386-redhat-linux-gnu.tar.bz2
    if grep '^begin [0-9]* ' $f && grep '^end$' $f
    then
	for t in sum log
	do
	    uudecode -o /dev/stdout $f | bunzip2 \
		| tar xpvOf - gdb-${isa}-redhat-linux-gnu.$t \
		> gdb-${pid}-${isa}.$t
	done
    fi
done

/home/cygnus/cagney/bin/do-analize-tests gdb-${pid}-*.sum
