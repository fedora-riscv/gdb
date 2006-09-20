#!/bin/sh

if test "$#" -eq 0
then
    echo >&2 "Usage: $0 [ /mnt/brew/packages/gdb/VERSION/DIST/data/logs/ARCH/build.log ]"
    echo >&2 "       [ /mnt/brew/scratch/USERNAME/task_TASKID/logs/ARCH/build.log ]"
    echo >&2 "       [ /mnt/brew/work/tasks/TASKID/build.log ] ..."
    exit 1
fi

if [ -d tests ];then
	if [ ! -f tests/.v2 ];then
		echo >&2 "Directory will be deleted!: tests"
		exit 1
	fi
	rm -rf tests
fi
mkdir tests
touch tests/.v2	# Marker for this temporary directory type

find "$@" -path '*/build.log' -print | while read f
do
    echo "$f" >&2
    ver=`echo "$f" | sed -n -e 's,^.*gdb/\([-0-9\.]*\)/\([^/]*\)/data/logs/\([^/]*\)/.*$,-\1,p'`
    rel=`echo "$f" | sed -n -e 's,^.*gdb/\([-0-9\.]*\)/\([^/]*\)/data/logs/\([^/]*\)/.*$,-\2,p'`
    isa=`echo "$f" | sed -n -e 's,^.*gdb/\([-0-9\.]*\)/\([^/]*\)/data/logs/\([^/]*\)/.*$,.\3,p'`
    if test -z "$ver" ; then
    ver=`echo "$f" | sed -n -e 's,^.*/scratch/.*/task_\([0-9]*\)/logs/\([^/]*\)/.*$,-\1,p'`
    fi
    if test -z "$isa" ; then
    isa=`echo "$f" | sed -n -e 's,^.*/scratch/.*/task_\([0-9]*\)/logs/\([^/]*\)/.*$,-\2,p'`
    fi
    if test -z "$ver" ; then
    ver=`echo "$f" | sed -n -e 's,^.*/work/tasks/\([0-9]*\)/.*$,-\1,p'`
    fi
    # begin 644 gdb-i386-redhat-linux-gnu.tar.bz2
    for t in sum log ; do
	if test -z "$isa" ; then
		isa=`uudecode < "$f" -o /dev/stdout | bunzip2 \
		| tar -t -f - "gdb-*-redhat-linux-gnu.$t" 2>&1 \
		| sed -n 's/^gdb-\(.*\)-redhat-linux-gnu[.].*$/-\1/p' \
		`
	fi
	line="gdb${ver}${rel}${isa}"
	uudecode < "$f" -o /dev/stdout | bunzip2 \
	    | tar -xpvvO -f - "gdb-*-redhat-linux-gnu.$t" \
	    > "tests/$line.$t"
    done
done

( cd tests && /home/cygnus/cagney/bin/do-analize-tests *.sum )

echo "$PWD/tests/*.html"
ls -1 tests/*.html 1>&2
