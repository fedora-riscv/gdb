#!/bin/sh

# Generate a patch that brings the most recent snapshot up-to-date

#branch=HEAD
date='-D 2004-06-07-gmt'
dir=`echo "cvs${branch}${date}" | tr ' ' '-'`
patch=gdb-`sed -n -e 's/^Version:[	 ]*\(.*\)$/\1/p' gdb.spec`

if test ! -d ${dir}/src
then
  ( mkdir -p ${dir} && cd ${dir} && cvs \
	-d :pserver:anoncvs@sources.redhat.com:/cvs/src \
	checkout ${branch} ${date} gdb )
fi

( cd ${dir}/src && cvs diff -Nu -r BASE -D `date -u +"%Y-%m-%d-gmt"` ./gdb ) | sed -e '
/^Index: .*\/version\.in$/,/^Index/ d
/^Index:/d
/^====/d
/^RCS/d
/^retrieving/d
/^diff/d
/^--- /N
/^---.* \/dev\/null/ {
  p
  d
}
/^--- \.\// {
  s/^--- \([-a-zA-Z\/\.0-9\+]*\)/--- \1.1/
  p
  d
}
' | tee $patch-sync-`date -u +%Y%m%d`

exit

# s/^--- \([-a-zA-Z\/\.0-9\+]*\)/--- \1.1/
# s/^[\+][\+][\+] \([-a-zA-Z\/\.0-9\+]*\)/+++ \1/

