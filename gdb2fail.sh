#!/bin/sh

if test "$#" -eq 0
then
    echo Usage: $0 /mnt/redhat/dist/DIST/gdb/VERSION/test/ARCH/build.log.gz ... 1>&2
    exit 1
fi

find "$@" -path '*/gdb/*/tests/*/build.log.gz' -print | while read f
do
    echo $f 1>&2
    ver=`echo "${f}" | sed -e 's,^.*gdb/\([-0-9\.]*\)/tests/\([^/]*\)/.*$,\1,'`
    isa=`echo "${f}" | sed -e 's,^.*gdb/\([-0-9\.]*\)/tests/\([^/]*\)/.*$,\2,'`
    # begin 644 gdb-i386-redhat-linux-gnu.tar.bz2
    for t in sum log ; do
	mkdir -p tests/${ver}
	gunzip < $f | uudecode -o /dev/stdout | bunzip2 \
	    | tar xpvOf - gdb-${isa}-redhat-linux-gnu.$t \
	    > tests/gdb-${ver}-${isa}.$t
    done
    echo "${ver}"
done | sort -u | while read ver ; do
    ( cd tests && /home/cygnus/cagney/bin/do-analize-tests gdb-${ver}-*.sum )
    echo "$PWD/tests/*.html"
    ls -1 tests/*.html 1>&2
done
