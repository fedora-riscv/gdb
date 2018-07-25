#!/bin/sh

# Generic function to print an error message and bail out.
die ()
{
    echo $1 > /dev/stderr
    exit 1
}

# Print usage
usage ()
{
    cat <<EOF
$0 -- Generate a git repository from .patch files

Usage:
  $0 <REPOSITORY>

<REPOSITORY> is the directory where the rebase was performed.  You
need to clone the repository first.

Options are:

  -h: Print this message
EOF
    exit 0
}

test -f gdb.spec || die "This script needs to run from the same directory as gdb.spec."

test -z $1 && die "You need to specify the repository."
test "$1" = "-h" && usage

test -f _git_upstream_commit || die "Cannot find _git_upstream_commit file."
test -f _patch_order || die "Cannot find _patch_order file."

last_ancestor_commit=`cat _git_upstream_commit`

cd $1

git name-rev $last_ancestor_commit
test $? -eq 0 || die "Could not find $last_ancestor_commit in the repository $1.  Did you run 'git fetch'?"

git checkout $last_ancestor_commit
for p in `cat ../_patch_order` ; do
    git am ../$p
    test $? -eq 0 || die "Could not apply patch '$p'."
done
