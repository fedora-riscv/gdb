%define __libtoolize echo

Summary: A GNU source-level debugger for C, C++ and Fortran.
Name: gdb
Version: 5.0
Release: 7j
Copyright: GPL
Group: Development/Debuggers
#Source0: ftp://sourceware.cygnus.com/pub/gdb/releases/gdb-%{version}.tar.bz2
Source: gdb-5.0.tar.bz2 
Patch0: gdb-5.0-s390.patch
Patch1: gdb-5.0-s390-1.patch
Patch2: gdb-5.0-s390-2.patch
Buildroot: %{_tmppath}/%{name}-%{version}-root
Prereq: /sbin/install-info
ExcludeArch: sparc

%description
Gdb is a full featured, command driven debugger. Gdb allows you to
trace the execution of programs and examine their internal state at
any time.  Gdb works for C and C++ compiled with the GNU C compiler
gcc.

If you are going to develop C and/or C++ programs and use the GNU gcc
compiler, you may want to install gdb to help you debug your
programs.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure

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
* Tue Oct 23 2001 Karsten Hopp <karsten@redhat.de>
- add 2 more patches from IBM for S/390

* Mon Jun 18 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- disable libtoolize

* Sat Dec 09 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 5.0.1 patch from IBM

* Mon Nov 20 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- added dwarf patch from IBM

* Sun Nov 19 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- go back to gdb-5.0-release
- add S390 patch from IBM

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
