%define cvsdate 20021129
# Define this if you want to skip the strip step and preserve debug info.
# Useful for testing. 
#define __spec_install_post /usr/lib/rpm/brp-compress || :
Summary: A GNU source-level debugger for C, C++ and other languages.
Name: gdb
# Daily snapshot of gdb taken from FSF mainline cvs, after the 5.3 branchpoint.
Version: 5.3post
Release: 0.%{cvsdate}.18
License: GPL
Group: Development/Debuggers
Source: ftp://sources.redhat.com/pub/gdb/snapshots/current/gdb+dejagnu-20021129.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-root
URL: http://sources.redhat.com/gdb/

# gdb-5.3post-misc.patch
# misc patch from previous release, w/o the changes to lin-lwp.c, to avoid
# conflicts with the nptl changes (on i386). (Jim Blandy and Kevin Buettner).
Patch0: gdb-5.3post-misc-p1.patch
# s390 ABI patch, not yet into upstream sources.
Patch1: gdb-5.3post-s390-may2002.patch
# Patch to disable -Werror on a few files, and fix some Makefile dependencies.
# (Elena Zannoni).
Patch2: gdb-5.3post-warnings-dec2002.patch
# Separate debug info patch. (Jim Blandy and Alex Larsson).
Patch3: gdb-5.3post-dbg-dec2002.patch
# Patch to accept empty args with --args (Andreas Schwab).
Patch4: gdb-5.3post-args-jan2003.patch
# patch to lin-lwp.c to bring it in sync with sources.redhat.com version.
Patch5: gdb-5.3post-sync.patch
# patch from Jeff Johnston (jjohnstn@redhat.com) to lin-lwp.c for
# nptl support. Applied for i386 only. (Still WIP).
#Patch6: gdb-5.3post-jj-lwp.patch
#Patch6: gdb-5.3post-jj-lwp2.patch
# all the fixes for NPTL, hopefully architecture neutral.
Patch6: gdb-5.3post-all-thread-jan2003.patch
# old misc patch from Kevin Buettner and Jim Blandy for lin-lwp.c and i386
# only (applies on top of Jeff Johnston patch).
# this is now included in the big thread patch.
#Patch7: gdb-5.3post-misc-p2.patch
# patch from Jeff Johnston (jjohnstn@redhat.com) for nptl support
# (applied for i386 only).
#Patch8: gdb-5.3post-jjohnstn-thread.patch
# patch to fix the until command and add advance command (ezannoni@redhat.com).
Patch9: gdb-5.3post-until-jan2003.patch
# cumulative ChangeLogs patches.
Patch10: gdb-5.3post-ChangeLog-all.patch
# patch to ignore NOBITS .eh_frame section in debug info (ezannoni@redhat.com).
Patch11: gdb-5.3post-dwarf2-jan2003.patch
# patch to cleanup gfi engine on rerun (mludvig@suse.com).
Patch12: gdb-5.3post-cfi-jan2003.patch
# patch to fix ui out errors (ezannoni@redhat.com, kevinb@redhat.com).
Patch13: gdb-5.3post-uiout-feb2003.patch
# patch to use the correct include file in s390-nat.c (ezannoni@redhat.com).
Patch14: gdb-5.3post-s390-feb2003.patch
# patch to expedite execution of testsuite when gdb gets internal
# error (jimb@redhat.com).
Patch15: gdb-5.3post-interr-feb2003.patch
# New TLS specific tests (ezannoni@redhat.com).
Patch16: gdb-5.3post-tlstst-feb2003.patch
# various cleanups for the gdb.threads tests
# (drow@mvista.com, ezannoni@redhat.com).
Patch17: gdb-5.3post-thrtst-feb2003.patch
# Patch to deal with .debug_ranges (rth@redhat.com, ezannoni@redhat.com,
# drow@mvista.com)
Patch18: gdb-5.3post-dw2ranges-feb2003.patch
# From jjohnstn@redhat.com
Patch19: gdb-5.3post-bug81732-feb2003.patch
# Fix for mi-ptreads tests (mec@shout.net). 
Patch20: gdb-5.3post-mipthreads-feb2003.patch
# Fix for dealing with files with stabs debug info, but no line info. 
# (jjohnstn@redhat.com, ezannoni@redhat.com).
Patch21: gdb-5.3post-stabfix-feb2003.patch
# Fix for gdb core dump on disassembly. (ezannoni@redhat.com).
Patch22: gdb-5.3post-s390dis-feb2003.patch
# Fix for new kernel behavior with attach and SIGSTOP (ezannoni@redhat.com).
Patch23: gdb-5.3post-attach-feb2003.patch
# From jjohnstn@redhat.com
Patch24: gdb-5.3post-jj-lwp3.patch
# Some misc testsuite cleanups. (ezannoni@redhat.com)
Patch25: gdb-5.3post-tests-feb2003.patch
# Update copyright year in version.
Patch26: gdb-5.3post-copyright-feb2003.patch

BuildRequires: ncurses-devel glibc-devel gcc make gzip texinfo dejagnu
Prereq: info

%description
GDB, the GNU debugger, allows you to debug programs written in C, C++,
and other languages, by executing them in a controlled fashion and
printing their data.

%prep
# This allows the tarball name to be different from our version-release name.
%setup -q -n gdb+dejagnu-%{cvsdate}

# Apply patches defined above.
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 
%patch4 -p1 
%patch5 -p1 
%patch6 -p1 
%ifarch %{ix86}
# apply the NPTL patches only on i386.
#patch6 -p1 
#patch7 -p1 
#patch8 -p1 
%endif
%ifarch alpha ppc ia64 x86_64 s390 s390x
# apply the rest of the misc patch only.
#patch7 -p1 
%endif
%patch9 -p1 
%patch10 -p1 
%patch11 -p1 
%patch12 -p1 
%patch13 -p1 
%patch14 -p1 
%patch15 -p1 
%patch16 -p1 
%patch17 -p1 
%patch18 -p1 
%patch19 -p1 
%patch20 -p1 
%patch21 -p1 
%patch22 -p1 
%patch23 -p1 
%patch24 -p1 
%patch25 -p1 
%patch26 -p1 

# Change the version that gets printed at GDB startup, so it is RedHat
# specific.
cat > gdb/version.in << _FOO
Red Hat Linux (%{version}-%{release}rh)
_FOO

# We don't need these. We'll test with the installed versions of
# expect/dejagnu.
rm -fr dejagnu tcl expect


%build

cd ..
rm -fr build-%{_target_platform}
mkdir build-%{_target_platform}
cd build-%{_target_platform}

# FIXME: The configure option
# --enable-gdb-build-warnings=,-Werror below can conflict with
# user settings. For instance, passing a combination of -Wall and -O0
# from the file rpmrc will always cause at least one warning, and stop
# the compilation.
# The whole configury line needs to be cleaned up.

export CFLAGS="$RPM_OPT_FLAGS"

# Only i386 builds with -Werror because other platforms get host header
# files conflicts.
enable_build_warnings=""
%ifarch %{ix86} alpha ia64 ppc s390 s390x
enable_build_warnings="--enable-gdb-build-warnings=,-Werror"
%endif

$RPM_BUILD_DIR/gdb+dejagnu-%{cvsdate}/configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir}\
	$enable_build_warnings \
        --with-separate-debug-dir=/usr/lib/debug \
    %{_target_platform}

make
make info

# For now do testing only on these platforms. The testsuite on x86_64 is not
# in good shape.
# FIXME disable alpha, ia64, s390, s390x, and ppc tests for moment.
#ifarch %{ix86} alpha ppc ia64
%ifarch %{ix86} 
echo ====================TESTING=========================
cd gdb/testsuite
make -k check || :
cd ../..
echo ====================TESTING END=====================
%endif

cd ..
# Copy the <sourcetree>/gdb/NEWS file to the directory above it.
cp $RPM_BUILD_DIR/gdb+dejagnu-%{cvsdate}/gdb/NEWS $RPM_BUILD_DIR/gdb+dejagnu-%{cvsdate}

%install
cd ../build-%{_target_platform}
rm -rf $RPM_BUILD_ROOT

%makeinstall

# Remove the files that are part of a gdb build but that are owned and
# provided by other packages.
# These are part of binutils

rm -rf $RPM_BUILD_ROOT/usr/share/locale/
rm -f $RPM_BUILD_ROOT%{_infodir}/bfd* $RPM_BUILD_ROOT%{_infodir}/standard*
rm -f $RPM_BUILD_ROOT%{_infodir}/configure*
rm -rf $RPM_BUILD_ROOT/usr/include/  $RPM_BUILD_ROOT/%{_libdir}/lib{bfd*,opcodes*,iberty*}

# Delete this too because the dir file will be updated at rpm install time.
# We don't want a gdb specific one overwriting the system wide one.

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
# This step is part of the installation of the RPM. Not to be confused
# with the 'make install ' of the build (rpmbuild) process.

[ -f %{_infodir}/gdb.info ]		&& /sbin/install-info %{_infodir}/gdb.info %{_infodir}/dir || :
[ -f %{_infodir}/gdb.info.gz ]		&& /sbin/install-info %{_infodir}/gdb.info.gz %{_infodir}/dir  || :
[ -f %{_infodir}/gdbint.info ]         && /sbin/install-info %{_infodir}/gdbint.info %{_infodir}/dir || :
[ -f %{_infodir}/gdbint.info.gz ]      && /sbin/install-info %{_infodir}/gdbint.info.gz %{_infodir}/dir  || :
[ -f %{_infodir}/mmalloc.info ]		&& /sbin/install-info %{_infodir}/mmalloc.info %{_infodir}/dir || :
[ -f %{_infodir}/mmalloc.info.gz ]	&& /sbin/install-info %{_infodir}/mmalloc.info.gz %{_infodir}/dir  || :
[ -f %{_infodir}/stabs.info ]		&& /sbin/install-info %{_infodir}/stabs.info %{_infodir}/dir  || :
[ -f %{_infodir}/stabs.info.gz ]	&& /sbin/install-info %{_infodir}/stabs.info.gz %{_infodir}/dir  || :

%preun
if [ $1 = 0 ]; then
	[ -f %{_infodir}/gdb.info ]		&& /sbin/install-info --delete %{_infodir}/gdb.info %{_infodir}/dir  || :
	[ -f %{_infodir}/gdb.info.gz ]		&& /sbin/install-info --delete %{_infodir}/gdb.info.gz %{_infodir}/dir  || :
	[ -f %{_infodir}/gdbint.info ]          && /sbin/install-info --delete %{_infodir}/gdbint.info %{_infodir}/dir  || :
	[ -f %{_infodir}/gdbint.info.gz ]       && /sbin/install-info --delete %{_infodir}/gdbint.info.gz %{_infodir}/dir  || :
	[ -f %{_infodir}/mmalloc.info ]		&& /sbin/install-info --delete %{_infodir}/mmalloc.info %{_infodir}/dir  || :
	[ -f %{_infodir}/mmalloc.info.gz ]	&& /sbin/install-info --delete %{_infodir}/mmalloc.info.gz %{_infodir}/dir  || :
	[ -f %{_infodir}/stabs.info ]		&& /sbin/install-info --delete %{_infodir}/stabs.info %{_infodir}/dir  || :
	[ -f %{_infodir}/stabs.info.gz ]	&& /sbin/install-info --delete %{_infodir}/stabs.info.gz %{_infodir}/dir  || :
fi

%files
%defattr(-,root,root)
%doc COPYING COPYING.LIB README NEWS
/usr/bin/*
%{_libdir}/libmmalloc.a*
%{_mandir}/*/*
%{_infodir}/gdb.info*
%{_infodir}/gdbint.info*
%{_infodir}/stabs.info*
%{_infodir}/mmalloc.info*

# don't include the files in include, they are part of binutils

%changelog
* Mon Feb 24 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.18
- Update copyright year printed in version.

* Mon Feb 24 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.17
- Refresh build.

* Mon Feb 24 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.16
- Add some testsuite cleanups, to avoid spurious test failures.

* Fri Feb 21 2003 Jeff Johnston <jjohnstn@redhat.com>  0.20021129.15
- Add patch to handle thread exiting when LD_ASSUME_KERNEL=2.4.1 which
  fixes Bugzilla bug 84217.

* Fri Feb 21 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.14
- New patch to fix disassembly on s390. Bugzilla bug 84286.
- New patch for attach/ptrace fix. Bugzilla bug 84220.
- Reenable tests for x86.

* Thu Feb 20 2003 Jeff Johnston <jjohnstn@redhat.com>  0.20021129.13
- Add patch for mixed stabs with dwarf2 - bugzilla bug 84253.

* Wed Feb 12 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.12
- Disable tests also for x86.

* Tue Feb 11 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.11
- Add patch for mi threads tests.
- Add patch for dwarf2 debug_ranges section.
- Add patch for detach bug.

* Mon Feb 10 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.10
- Add patch for testsuite auto answering internal error queries.
- Add new TLS tests.
- Add cleanup patches for thread tests.

* Mon Feb 03 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.9
- Add new patch for thread support. Apply on all arches.
- Do not apply old patches, but leave them around for now.
- Add new patch for dwarf2 debug info reading.
- Add new patch for dwarf2 cfi engine cleanup.
- Add new patch for uiout problems.
- Add new patch for s390 build.
- Disable tests on all platforms but x86.

* Mon Jan 27 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.8
- Move all the changelog entries to a single patch.
- Add tests to the args patch.
- Add new patch for until command fix (bugzilla Bug 19890).
- s390 and s390x can be built with -Werror.
- Run make check for s390 and s390x too.
- Include an updated version of the thread nptl patch (still WIP).

* Wed Jan 15 2003 Phil Knirsch <pknirsch@redhat.com> 0.20021129.7
- Apply the 2nd misc patch for s390 and s390x, too.

* Tue Jan 14 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.6
- Add patches for NPTL support, to be applied on i386 only.
  (this is still WIP)
- Split old misc patch in two parts.
- Temporarily disable testsuite run on alpha.

* Sun Jan 12 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.5
- Add patch for --args with zero-length arguments. Fix for bug 79833.

* Tue Dec 17 2002 Elliot Lee <sopwith@redhat.com> 0.20021129.4
- The define directive to rpm is significant even if the line it is 
  in happens to start with a '#' character. Fixed.

* Fri Dec 13 2002 Elena Zannoni <ezannoni@redhat.com>  0.20021129.3
- Merge previous patches for warnings into a single one.
- Add changelogs to patches.
- Add, but don't use, a macro to avoid stripping.

* Fri Dec  6 2002 Elena Zannoni <ezannoni@redhat.com>
- Add patch to allow debugging of executables with debug info stored
  in separate files.
- Add patch for Makefile dependencies and disable warnings for
  building thread-db.c.
- Re-enable building with -Werror for alpha, ia64, ppc.

* Mon Dec  2 2002 Elena Zannoni <ezannoni@redhat.com>
- Don't pass to gdb an empty build warnings flag, or that will disable warnings
  completely. We want to build using gdb's standard warnings instead.

* Mon Dec  2 2002 Elena Zannoni <ezannoni@redhat.com>
- Don't do testing for x86_64.

* Sun Dec  1 2002 Elena Zannoni <ezannoni@redhat.com>
- x86_64 doesn't build with Werror yet.
- Add patch for alpha.
- Alpha doesn't build with -Werror either.
- Add patch for ia64.
- Add patch for ppc.
- Drop ia64 from -Werror list.
- Drop ppc from -Werror list.

* Sun Dec  1 2002 Elena Zannoni <ezannoni@redhat.com>
- Add dejagnu to the build requirements.
- Enable make check.
- Add enable-gdb-build-warnings to the configure flags.

* Fri Nov 29 2002 Elena Zannoni <ezannoni@redhat.com>
- Import new upstream sources.
- Change version and release strings.
- Upgrade patches.
- Build gdb/gdbserver as well.
- Define and use 'cvsdate'.
- Do %%setup specifying the source directory name. 
- Don't cd up one dir before removing tcl and friends.
- Change the configure command to allow for the new source tree name.
- Ditto for the copy of NEWS.
- Add some comments.

* Mon Nov 25 2002 Elena Zannoni <ezannoni@redhat.com> 5.2.1-5
General revamp.
- Add patch for gdb/doc/Makefile.in. Part of fix for bug 77615.
- Add patch for mmalloc/Makefile.in. Part of fix for bug 77615.
- Change string printed in version.in to <version>-<release>rh.
- Move the deletion of dejagnu, expect, tcl to the prep section,
  from the build section.
- Add build directory housekeeping to build section.
- Use macros for configure parameters.
- Do the build in a separate directory.
- Prepare for testing, but not enable it yet.
- Correctly copy the NEWS file to the top level directory, for the doc
  section to find it.
- Cd to build directory before doing install.
- Use makeinstall macro, w/o options.
- Remove workaround for broken gdb info files. Part of fix for bug 77615.
- Remove share/locale directory, it is in binutils.
- Remove info/dir file.
- Clarify meaning of post-install section.
- Add gdbint info files to post-install, pre-uninstall and files sections.
  Part of fix for bugs 77615, 76423.
- Add libmmalloc.a to package.

* Fri Aug 23 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- added mainframe patch from developerworks

* Wed Aug 21 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.2.1-3
- Add changelogs to the previous patch

* Wed Aug 14 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.2.1-2
- Add some patches from Elena Zannoni <ezannoni@redhat.com>

* Tue Jul 23 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.2.1-1
- 5.2.1

* Mon Jul 22 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- compile on mainframe

* Mon Jul  8 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.2-3
- Rebuild

* Tue May  7 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.2-2
- Rebuild

* Mon Apr 29 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.2-1
- 5.2

* Mon Apr 29 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.1.92-1
- 5.1.92. Hopefully identical to 5.2 final

* Mon Apr 22 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.1.91-1
- 5.1.91. 5.2 expected in a week

* Thu Mar 28 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.1.90CVS-5
- Update to current

* Thu Mar 28 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.1.90CVS-4
- Update to current

* Thu Mar 28 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.1.90CVS-3
- Update to current

* Wed Mar 20 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.1.90CVS-2
- Update to current

* Wed Mar 13 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.1.90CVS-1
- Update to current 5.2 branch 

* Thu Jan 24 2002 Trond Eivind Glomsr�d <teg@redhat.com> 5.1.1-1
- 5.1.1
- add URL

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Dec 10 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.1-2
- Fix some thread+fpu problems

* Mon Nov 26 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.1-1
- 5.1

* Mon Nov 19 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.0.94-0.71
- 5.0.94. Almost there....

* Mon Nov 12 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.0.93-2
- Add patch from jakub@redhat.com to improve handling of DWARF

* Mon Nov 12 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.0.93-1
- 5.0.93 
- handle missing info pages in post/pre scripts

* Wed Oct 31 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.0.92-1
- 5.0.92

* Fri Oct 26 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.0.91rh-1
- New snapshot
- Use the 5.0.91 versioning from the snapshot

* Wed Oct 17 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.0rh-17
- New snapshot

* Thu Sep 27 2001 Trond Eivind Glomsr�d <teg@redhat.com> 
- New snapshot

* Wed Sep 12 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.0rh-16
- New snapshot 

* Mon Aug 13 2001 Trond Eivind Glomsr�d <teg@redhat.com> 5.0rh-15
- Don't buildrequire compat-glibc (#51690)

* Thu Aug  9 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- New snapshot, from the stable branch eventually leading to gdb 5.1

* Mon Jul 30 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- s/Copyright/License/
- Add texinfo to BuildRequires

* Mon Jun 25 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- New snapshot

* Fri Jun 15 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- New snapshot
- Add ncurses-devel to buildprereq
- Remove perl from buildprereq, as gdb changed the way 
  version strings are generated

* Thu Jun 14 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- New snapshot

* Wed May 16 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- New snapshot - this had thread fixes for curing #39070
- New way of specifying version

* Tue May  1 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- New tarball
- Kevin's patch is now part of gdb

* Mon Apr  9 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- Add patch from kevinb@redhat.com to fix floating point + thread 
  problem (#24310)
- remove old workarounds
- new snapshot

* Thu Apr  5 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- New snapshot

* Sat Mar 17 2001 Bill Nottingham <notting@redhat.com>
- on ia64, there are no old headers :)

* Fri Mar 16 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- build with old headers, new compiler

* Wed Mar 16 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- new snapshot

* Mon Feb 26 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- new snapshot which should fix some more IA64 problems (#29151)
- remove IA64 patch, it's now integrated

* Wed Feb 21 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- add IA64 and Alpha patches from Kevin Buettner <kevinb@redhat.com>
- use perl instead of patch for fixing the version string

* Tue Feb 20 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- don't use kgcc anymore
- mark it as our own version
- new snapshot

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Link with ncurses 5.x even though we're using kgcc.
  No need to drag in requirements on ncurses4 (Bug #24445)

* Fri Jan 19 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- new snapshot

* Thu Dec 20 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- new snapshot

* Mon Dec 04 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- new snapshot
- new alpha patch - it now compiles everywhere. Finally.

* Fri Dec 01 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- new snapshot

* Mon Nov 20 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- new CVS snapshot
- disable the patches
- don't use %%configure, as it confuses the autoconf script
- enable SPARC, disable Alpha


* Wed Aug 09 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- added patch from GDB team for C++ symbol handling

* Mon Jul 25 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- upgrade to CVS snapshot
- excludearch SPARC, build on IA61

* Wed Jul 19 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- rebuild

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul 02 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- rebuild

* Fri Jun 08 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- use %%configure, %%makeinstall, %%{_infodir}, %%{_mandir},
  and %%{_tmppath}
- the install scripts  for info are broken(they don't care about
  you specify in the installstep), work around that.
- don't build for IA64

* Mon May 22 2000 Trond Eivind Glomsr�d <teg@redhat.com>
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
