%define snapdate 20010316

Summary: A GNU source-level debugger for C, C++ and Fortran.
Name: gdb
Version: 5.0rh
Release: 5
Copyright: GPL
Patch0: gdb-alpha.patch
Group: Development/Debuggers
Source: ftp://sources.redhat.com/pub/gdb/snapshots/gdb+dejagnu-%{snapdate}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: perl 
%ifnarch ia64
BuildPrereq: compat-glibc
%endif
Prereq: info

%description
Gdb is a full featured, command driven debugger. Gdb allows you to
trace the execution of programs and examine their internal state at
any time.  Gdb works for C and C++ compiled with the GNU C compiler
gcc.

If you are going to develop C and/or C++ programs and use the GNU gcc
compiler, you may want to install gdb to help you debug your
programs.

%prep
%setup -q -n gdb+dejagnu-%{snapdate}
%patch0 -p1 -b .alpha


perl -pi -e "s/^VERSION.*$/VERSION=5\.0rh-%{release} Red Hat Linux 7\.1/" gdb/Makefile.in

%build
%ifarch ia64
export CFLAGS="$RPM_OPT_FLAGS"
%else
export CFLAGS="-I/usr/i386-glibc21-linux/include $RPM_OPT_FLAGS"
%endif
rm -fr dejagnu tcl expect 
./configure --prefix=/usr --sysconfdir=/etc --mandir=/usr/share/man --infodir=/usr/share/info \
    %{_arch}-redhat-linux

make
make info
cp gdb/NEWS .

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall infodir=$RPM_BUILD_ROOT/${_infodir} prefix=$RPM_BUILD_ROOT/usr


#make install-info infodir=$RPM_BUILD_ROOT/${_infodir}
# The above is broken, do this for now:
mkdir -p $RPM_BUILD_ROOT/%{_infodir}
cp `find -name "*.info*"` $RPM_BUILD_ROOT/%{_infodir}



rm -f $RPM_BUILD_ROOT%{_infodir}/dir $RPM_BUILD_ROOT%{_infodir}/dir.info* 

#These are part of binutils

rm -f $RPM_BUILD_ROOT%{_infodir}/bfd* $RPM_BUILD_ROOT%{_infodir}/standard*
rm -rf $RPM_BUILD_ROOT/usr/include/  $RPM_BUILD_ROOT/usr/lib/lib{bfd*,opcodes*}

gzip -9f $RPM_BUILD_ROOT%{_infodir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/gdb.info %{_infodir}/dir
/sbin/install-info %{_infodir}/gdbint.info.gz %{_infodir}/dir
/sbin/install-info %{_infodir}/mmalloc.info.gz %{_infodir}/dir
/sbin/install-info %{_infodir}/stabs.info.gz %{_infodir}/dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/gdb.info.gz %{_infodir}/dir
    /sbin/install-info --delete %{_infodir}/gdbint.info.gz %{_infodir}/dir
    /sbin/install-info --delete %{_infodir}/mmalloc.info.gz %{_infodir}/dir
    /sbin/install-info --delete %{_infodir}/stabs.info.gz %{_infodir}/dir
fi

%files
%defattr(-,root,root)
%doc COPYING COPYING.LIB README NEWS
/usr/bin/*
%{_mandir}/*/*
%{_infodir}/gdb.info*
%{_infodir}/gdbint.info*
%{_infodir}/stabs.info*
%{_infodir}/mmalloc.info*

# don't include the files in include, they are part of binutils


%changelog
* Sat Mar 17 2001 Bill Nottingham <notting@redhat.com>
- on ia64, there are no old headers :)

* Fri Mar 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- build with old headers, new compiler

* Wed Mar 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Feb 26 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot which should fix some more IA64 problems (#29151)
- remove IA64 patch, it's now integrated

* Wed Feb 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- add IA64 and Alpha patches from Kevin Buettner <kevinb@redhat.com>
- use perl instead of patch for fixing the version string

* Tue Feb 20 2001 Trond Eivind Glomsrød <teg@redhat.com>
- don't use kgcc anymore
- mark it as our own version
- new snapshot

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Link with ncurses 5.x even though we're using kgcc.
  No need to drag in requirements on ncurses4 (Bug #24445)

* Fri Jan 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Thu Dec 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Dec 04 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot
- new alpha patch - it now compiles everywhere. Finally.

* Fri Dec 01 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Nov 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new CVS snapshot
- disable the patches
- don't use %%configure, as it confuses the autoconf script
- enable SPARC, disable Alpha


* Wed Aug 09 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added patch from GDB team for C++ symbol handling

* Mon Jul 25 2000 Trond Eivind Glomsrød <teg@redhat.com>
- upgrade to CVS snapshot
- excludearch SPARC, build on IA61

* Wed Jul 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul 02 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Fri Jun 08 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%configure, %%makeinstall, %%{_infodir}, %%{_mandir},
  and %%{_tmppath}
- the install scripts  for info are broken(they don't care about
  you specify in the installstep), work around that.
- don't build for IA64

* Mon May 22 2000 Trond Eivind Glomsrød <teg@redhat.com>
- upgraded to 5.0 - dump all patches. Reapply later if needed.
- added the NEWS file to the %%doc files
- don't delete files which doesn't get installed (readline, texinfo)
- let build system handle stripping and gzipping
- don't delete libmmalloc
- apply patch from jakub@redhat.com to make it build on SPARC

* Fri Apr 28 2000 Matt Wilson <msw@redhat.com>
- rebuilt against new ncurses

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Tue Feb  8 2000 Jakub Jelinek <jakub@redhat.com>
- fix core file handling on i386 with glibc 2.1.3 headers

* Fri Jan 14 2000 Jakub Jelinek <jakub@redhat.com>
- fix reading registers from core on sparc.
- hack around build problems on i386 with glibc 2.1.3 headers

* Thu Oct 7 1999 Jim Kingdon
- List files to install in /usr/info specifically (so we don't pick up
things like info.info from GDB snapshots).

* Thu Oct 7 1999 Jim Kingdon
- Update GDB to 19991004 snapshot.  This eliminates the need for the
sigtramp, sparc, xref, and threads patches.  Update sparcmin patch.

* Mon Aug 23 1999 Jim Kingdon
- Omit readline manpage.

* Tue Aug 7 1999 Jim Kingdon
- Remove H.J. Lu's patches (they had been commented out).
- Add sigtramp patch (from gdb.cygnus.com) and threads patch (adapted
from code fusion CD-ROM).

* Wed Apr 14 1999 Jeff Johnson <jbj@redhat.com>
- merge H.J. Lu's patches into 4.18.

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- updated the kern22 patch with stuff from davem

* Thu Apr  1 1999 Jeff Johnson <jbj@redhat.com>
- sparc with 2.2 kernels no longer uses sunos ptrace (davem)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Mon Mar  8 1999 Jeff Johnson <jbj@redhat.com>
- Sparc fiddles for Red Hat 6.0.
