# Define this if you want to skip the strip step and preserve debug
# info.  Useful for testing.
#%define __spec_install_post /usr/lib/rpm/brp-compress || :

Summary: A GNU source-level debugger for C, C++, Java and other languages.
Name: gdb

# Set version to contents of gdb/version.in.
Version: 6.3

%define gdb_src gdb-%{version}
%define gdb_build gdb-%{version}-build-%{_target_platform}

# The release always contains a leading reserved number, start it at 0.
Release: 0.0.0

License: GPL
Group: Development/Debuggers
Source: ftp://ftp.gnu.org/gnu/gdb/gdb-6.3.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-root
URL: http://gnu.org/software/gdb/

# Make sure we get rid of the old package gdb64, now that we have unified
# support for 32-64 bits in one single 64-bit gdb.
%ifarch ppc64
Obsoletes: gdb64
%endif

# GDB patches have the format gdb-<version>-<desc>-<YYYYMMDD>.patch
# and include the ChangeLog.RedHat change-log entry.

# FIXME:
# Create an empty ChangeLog.RedHat

# ------------------------------------------

# ChangeLogs patches.
#N/A: Patch0: gdb-6.1post-ChangeLog.patch
# ChangeLogs patches for doc.
#N/A: Patch2: gdb-6.1post-ChangeLog-doc.patch
####### start patches from the previous RPM.
# Silence gcc warnings.
#N/A: Patch4: gdb-6.1post-gccwarn.patch

####### end patches from the previous RPM.

# Fix watchpoint support.
#Patch5: gdb-6.1post-watchpoint-fix.patch
Patch5: broken.patch
# Thread fix.
#Patch6: gdb-6.1post-thread-fix.patch
Patch6: broken.patch
# Fix to allow using libunwind 0.97 and up.
#Patch8: gdb-6.1post-libunwind.patch
Patch8: broken.patch
# Fix to support applications calling clone directly
#Patch9: gdb-6.1post-linlwp-aug2004.patch
Patch9: broken.patch

####### Signal trampoline fixes
#Patch10: gdb-6.1post-sig-ppc-jun2004.patch
Patch10: broken.patch
Patch11: gdb-6.1post-sig-symtramp-jun2004.patch
Patch12: gdb-6.1post-sig-x86-jun2004.patch
#Merged: Patch14: gdb-6.1post-sig-infrun-sep2004.patch

####### ABI fixes and updates
#Merged: Patch18: gdb-6.1post-abi-i386unwind-nov2004.patch
#Patch19: gdb-6.1post-abi-ppccfi-nov2004.patch
Patch19: broken.patch
#Patch20: gdb-6.1post-abi-ppc64-oct2004.patch
Patch20: broken.patch
Patch21: gdb-6.1post-abi-ppc64syscall-jun2004.patch
#Patch22: gdb-6.1post-abi-wildframe-jun2004.patch
Patch22: broken.patch
#Patch23: gdb-6.1post-abi-ppc64main-aug2004.patch
Patch23: broken.patch
Patch24: gdb-6.1post-frame-zeropc-sep2004.patch
Patch25: gdb-6.1post-abi-ppcdotsolib-oct2004.patch
Patch26: gdb-6.1post-abi-ppc64fpscr-oct2004.patch
#Merged: Patch27: gdb-6.1post-abi-s390rewrite-oct2004.patch
Patch28: gdb-6.1post-abi-ppc64section-oct2004.patch
#Merged: Patch29: gdb-6.1post-op-piece-warn-oct2004.patch

###### Testsuite merge, fixes, and local RH hack
#Merged: Patch30: gdb-6.1post-test-merge-20040923.patch
# Work around out-of-date dejagnu that does not have kfail
Patch31: gdb-6.1post-test-rh-kfail.patch
# Match Red Hat version info
Patch32: gdb-6.1post-test-rh-version.patch
# Get selftest working with sep-debug-info
#Patch33: gdb-6.1post-test-self-jul2004.patch
Patch33: broken.patch
# Check that libunwind works - new test then fix
Patch34: gdb-6.1post-test-rh-libunwind.patch
Patch35: gdb-6.1post-test-rh-libunwindfix1.patch
# Generate the bigcore file from the running inferior et.al.
#Patch36: gdb-6.1post-test-bigcoresingle-sep2004.patch
Patch36: broken.patch
#Patch37: gdb-6.1post-test-bigcore64-sep2004.patch
Patch37: broken.patch
# Fix comment bug in sigstep.exp
#Patch38: gdb-6.1post-test-sigstepcomment-oct2004.patch
Patch38: broken.patch

##### VSYSCALL and PIE
Patch50: gdb-6.1post-vsyscall-jul2004.patch
#Patch51: gdb-6.1post-pie-jul2004.patch
Patch51: broken.patch
#Patch52: gdb-6.1post-test-pie-nov2004.patch
Patch52: broken.patch

##### Bigcore tweak
#Patch60: gdb-6.1post-o-largefile-jul2004.patch
Patch60: broken.patch

# Fix crasher in symtab
#Patch70: gdb-6.1post-symtab-bob-jul2004.patch
Patch70: broken.patch
# Add java inferior call support
#Patch71: gdb-6.1post-java-infcall-aug2004.patch
Patch71: broken.patch
# Add support for manually loaded/unloaded shlibs.
#Patch72: gdb-6.1post-unload-aug2004.patch
Patch72: broken.patch
# Fix stepping in threads
#Patch73: gdb-6.1post-thread-step-sep2004.patch
Patch73: broken.patch
# Add threaded watchpoint support
#Patch74: gdb-6.1post-threaded-watchpoints-sep2004.patch
Patch74: broken.patch
# Fix for thread_db_get_lwp
#Patch75: gdb-6.1post-thread-get-lwp-oct2004.patch
Patch75: broken.patch
# Fix for S/390 watchpoints under threads.
#Patch76: gdb-6.1post-s390-watchpoints-oct2004.patch
Patch76: broken.patch
# Fix for caching thread lwps for linux
Patch77: gdb-6.1post-lwp-cache-oct2004.patch
# Fix for allowing macros to continue after backtrace errors
Patch78: gdb-6.1post-backtrace-nov2004.patch
# Fix to expose multiple constructors to end-user
Patch79: gdb-6.1post-constructor-nov2004.patch

# Fix panic when stepping an solib call
#Patch80: gdb-6.1post-infcall-step-jul2004.patch
Patch80: broken.patch
# Fix ia64 backtrace
#Patch81: gdb-6.1post-ia64-backtrace-nov2004.patch
Patch81: broken.patch
# Add --readnever hack, and gstack script
#Patch82: gdb-6.1post-readnever-nov2004.patch
Patch82: broken.patch
Patch83: gdb-6.1post-gstack-nov2004.patch
# Add PPC register groups.
Patch84: gdb-6.1post-abi-ppcreggroups-nov2004.patch
# No longer a need to set .malloc on ppc64.
#Patch85: gdb-6.1post-abi-ppcmalloc-nov2004.patch
Patch85: broken.patch
# display and x needed to look for a section symbol.
Patch86: gdb-6.1post-abi-ppc64displaysymbol-nov2004.patch
# Continue removing breakpoints even when failure occurs.
Patch87: gdb-6.1post-remove-bp-nov2004.patch

# Add fixes starting at 100

%ifarch ia64
BuildRequires: ncurses-devel glibc-devel gcc make gzip texinfo dejagnu libunwind >= 0.96-3
%else
BuildRequires: ncurses-devel glibc-devel gcc make gzip texinfo dejagnu
%endif

%ifarch ia64
Requires: libunwind >= 0.96-3
%endif
 
Prereq: info

%description
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

%prep

# This allows the tarball name to be different from our
# version-release name.

%setup -q -n %{gdb_src}

# Apply patches defined above.

# Apply patches defined above.
#%patch0 -p1 
#%patch2 -p1 
#%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
#%patch14 -p1

#%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
#%patch27 -p1
%patch28 -p1
#%patch29 -p1

#%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1

%patch50 -p1
%patch51 -p1
%patch52 -p1

%patch60 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1

# Change the version that gets printed at GDB startup, so it is RedHat
# specific.
cat > gdb/version.in << _FOO
Red Hat Linux (%{version}-%{release}rh)
_FOO

# Remove the info and other generated files added by the FSF release
# process.
rm -f gdb/doc/*.info
rm -f gdb/doc/*.info-*

# ... and remove the objective-c testcases -- no objective-c
rm -fr gdb/testsuite/gdb.objc                                                                                
# ... and remove the ada testcases -- no ada support at all.
rm -fr gdb/testsuite/gdb.ada                                                                                
# FIXME: remove gdb/gdbserver/config.h from the snapshot. Suspect a bug
# in the FSF snapshot process.
rm -f gdb/gdbserver/config.h

%build

# Initially we're in the %{gdb_src} directory.
cd ..

# Identify the build directory with the version of gdb as well as the
# architecture, to allow for mutliple versions to be installed and
# built.

rm -fr %{gdb_build}
mkdir %{gdb_build}
cd %{gdb_build}

# FIXME: The configure option --enable-gdb-build-warnings=,-Werror
# below can conflict with user settings. For instance, passing a
# combination of -Wall and -O0 from the file rpmrc will always cause
# at least one warning, and stop the compilation.  The whole configury
# line needs to be cleaned up.

export CFLAGS="$RPM_OPT_FLAGS"

enable_build_warnings=""
%ifarch %{ix86} alpha ia64 ppc s390 s390x x86_64 ppc64
enable_build_warnings="--enable-gdb-build-warnings=,-Werror"
%endif

../%{gdb_src}/configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir}\
	$enable_build_warnings \
        --with-separate-debug-dir=/usr/lib/debug \
    %{_target_platform}

make
make info

# Get some information about which tools we interact with. We cannot
# invoke rpm -q from here.
# Note that binutils and glibc don't brand themselves as RedHat specific
# versions. This is very wrong. They are not the vanilla FSF ones!
%ifarch %{ix86} ppc s390 ia64
if [ -x /lib/tls/libc.so.6 ] ; then
  /lib/tls/libc.so.6
elif [ -x /lib/tls/libc.so.6.1 ] ; then
    /lib/tls/libc.so.6.1
fi
%endif
%ifarch x86_64 s390x ppc64
if  [ -x /lib64/tls/libc.so.6 ] ; then
   /lib64/tls/libc.so.6
fi
%endif

gcc -v
uname -a
ld -v

# For now do testing only on these platforms. 
%ifarch %{ix86} x86_64 s390x s390 ppc ia64 ppc64
echo ====================TESTING=========================
cd gdb/testsuite
# Need to use a single --ignore option, second use overrides first.
make -k check RUNTESTFLAGS='--ignore bigcore.exp\ attach-pie.exp\ asm-source.exp\ sigstep.exp' || :
for t in sum log; do
  ln gdb.$t gdb-%{_target_platform}.$t || :
done
tar cf - gdb-%{_target_platform}.{sum,log} \
	| bzip2 -1 \
	| uuencode gdb-%{_target_platform}.tar.bz2 \
	|| :
cd ../..
echo ====================TESTING END=====================
%endif

cd ..
# Copy the <sourcetree>/gdb/NEWS file to the directory above it.
cp $RPM_BUILD_DIR/gdb+dejagnu-%{cvsdate}/gdb/NEWS $RPM_BUILD_DIR/gdb+dejagnu-%{cvsdate}

%install
cd ../%{gdb_build}
rm -rf $RPM_BUILD_ROOT

%makeinstall

# install the gcore script in /usr/bin
cp $RPM_BUILD_DIR/gdb+dejagnu-%{cvsdate}/gdb/gdb_gcore.sh $RPM_BUILD_ROOT%{_prefix}/bin/gcore
chmod 755 $RPM_BUILD_ROOT%{_prefix}/bin/gcore

# Remove the files that are part of a gdb build but that are owned and
# provided by other packages.
# These are part of binutils

rm -rf $RPM_BUILD_ROOT/usr/share/locale/
rm -f $RPM_BUILD_ROOT%{_infodir}/bfd* 
rm -f $RPM_BUILD_ROOT%{_infodir}/standard*
rm -f $RPM_BUILD_ROOT%{_infodir}/mmalloc*
rm -f $RPM_BUILD_ROOT%{_infodir}/configure*
rm -rf $RPM_BUILD_ROOT/usr/include/  
rm -rf $RPM_BUILD_ROOT/%{_libdir}/lib{bfd*,opcodes*,iberty*,mmalloc*}

# Delete this too because the dir file will be updated at rpm install time.
# We don't want a gdb specific one overwriting the system wide one.

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
# This step is part of the installation of the RPM. Not to be confused
# with the 'make install ' of the build (rpmbuild) process.

[ -f %{_infodir}/annotate.info ]	&& /sbin/install-info %{_infodir}/annotate.info %{_infodir}/dir || :
[ -f %{_infodir}/annotate.info.gz ]	&& /sbin/install-info %{_infodir}/annotate.info.gz %{_infodir}/dir  || :
[ -f %{_infodir}/gdb.info ]		&& /sbin/install-info %{_infodir}/gdb.info %{_infodir}/dir || :
[ -f %{_infodir}/gdb.info.gz ]		&& /sbin/install-info %{_infodir}/gdb.info.gz %{_infodir}/dir  || :
[ -f %{_infodir}/gdbint.info ]         && /sbin/install-info %{_infodir}/gdbint.info %{_infodir}/dir || :
[ -f %{_infodir}/gdbint.info.gz ]      && /sbin/install-info %{_infodir}/gdbint.info.gz %{_infodir}/dir  || :
[ -f %{_infodir}/stabs.info ]		&& /sbin/install-info %{_infodir}/stabs.info %{_infodir}/dir  || :
[ -f %{_infodir}/stabs.info.gz ]	&& /sbin/install-info %{_infodir}/stabs.info.gz %{_infodir}/dir  || :

%preun
if [ $1 = 0 ]; then
	[ -f %{_infodir}/annotate.info ]	&& /sbin/install-info --delete %{_infodir}/annotate.info %{_infodir}/dir  || :
	[ -f %{_infodir}/annotate.info.gz ]	&& /sbin/install-info --delete %{_infodir}/annotate.info.gz %{_infodir}/dir  || :
	[ -f %{_infodir}/gdb.info ]		&& /sbin/install-info --delete %{_infodir}/gdb.info %{_infodir}/dir  || :
	[ -f %{_infodir}/gdb.info.gz ]		&& /sbin/install-info --delete %{_infodir}/gdb.info.gz %{_infodir}/dir  || :
	[ -f %{_infodir}/gdbint.info ]          && /sbin/install-info --delete %{_infodir}/gdbint.info %{_infodir}/dir  || :
	[ -f %{_infodir}/gdbint.info.gz ]       && /sbin/install-info --delete %{_infodir}/gdbint.info.gz %{_infodir}/dir  || :
	[ -f %{_infodir}/stabs.info ]		&& /sbin/install-info --delete %{_infodir}/stabs.info %{_infodir}/dir  || :
	[ -f %{_infodir}/stabs.info.gz ]	&& /sbin/install-info --delete %{_infodir}/stabs.info.gz %{_infodir}/dir  || :
fi

%files
%defattr(-,root,root)
%doc COPYING COPYING.LIB README NEWS
/usr/bin/*
%{_mandir}/*/*
%{_infodir}/annotate.info*
%{_infodir}/gdb.info*
%{_infodir}/gdbint.info*
%{_infodir}/stabs.info*

# don't include the files in include, they are part of binutils

%changelog
* Wed Dec 01 2004 Andrew Cagney <cagney@redhat.com>	6.3-0.0
- Import GDB 6.3, get building, add all patches.

* Tue Nov 30 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.63
- When removing breakpoints, continue removing breakpoints even if an
  error occurs on the list.

* Sun Nov 28 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.62
- Bump version for RHEL4 build.

* Wed Nov 24 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.61
- For PPC-64, fix search for a symbol (wasn't specifying the section).

* Wed Nov 24 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.60
- For PPC-64, do not set malloc name to ".malloc"; no longer needed.
- For all, only define kfail when not already defined.

* Wed Nov 24 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.59
- Bump version.

* Wed Nov 24 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.58
- Add rs6000 reggroups; fixes problem of PS register being trashed
  causing mysterious branch breakpoints.

* Tue Nov 23 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.57
- Backport i386 prolog parser - better backtraces out of semop().
- Add option --readnever to suppress the reading of symbolic debug
  information.
- Add script gstack.sh, installed as gstack.
  Bugzilla 136584, 137121
- Add missing files gdb.pie/attach2.c, gdb.pie/break1.c and
  gdb.pie/Makefile.in along with testsuite/configure stuff for pie.

* Tue Nov 23 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.57
- Backport i386 prolog parser - better backtraces out of semop().
- Add option --readnever to suppress the reading of symbolic debug
  information.
- Add script gstack.sh, installed as gstack.
  Bugzilla 136584, 137121

* Mon Nov 22 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.56
- Bump up release number.

* Mon Nov 22 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.55
- Multiple ia64 backtrace fixes.  Bugzilla 125157

* Thu Nov 11 2004 Elena Zannoni <ezannoni@redhat.com>	1.200400607.54
- Bump up release number

* Thu Nov 11 2004 Elena Zannoni <ezannoni@redhat.com>	1.200400607.51
- Modify configure line to not use absolute paths. This was 
  creating problems with makeinfo/texinfo.
- Get rid of makeinfo hack.
Bugzilla 135633

* Tue Nov 09 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.50
- Bump up release number

* Tue Nov 09 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.49
- Bump up release number

* Tue Nov 09 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.48
- Expose $base, $allocate constructors and $delete, $base destructors
  for breakpoints.

* Tue Nov 09 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.47
- Enable PPC CFI.

* Mon Nov 08 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.46
- Bump up release number

* Mon Nov 08 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.45
- Bump up release number

* Fri Nov 05 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.44
- Allow macros to continue past a backtrace error

* Tue Oct 26 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.43
- Hack around broken PT_FPSCR defined in headers.
- Import latest s390 fixes.
- Disable sigstep.exp - s390 has problems.
- Use PC's symtab when looking for a symbol.
- Work around DW_OP_piece.

* Fri Oct 22 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.42
- For 64-bit PPC, convert _dl_debug_state descriptor into a code address.
- Fix --ignore option.

* Mon Oct 10 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.40
- Disable attach-pie.exp test, hangs on amd64 without auxv.
- Move pie tests to pie.

* Mon Oct 10 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.39
- Fix comment bug in sigstep.exp.

* Thu Oct 07 2004 Jeff Johnston	<jjohnstn@redhat.com>	1.200400607.38
- Do not invalidate cached thread info when resuming threads.
- Bump up release number.

* Fri Oct 01 2004 Jeff Johnston  <jjohnstn@redhat.com>	1.200400607.35
- Fix S/390 watchpoint support to work better under threading.

* Fri Oct 01 2004 Jeff Johnston  <jjohnstn@redhat.com>	1.200400607.34
- Fix thread_db_get_lwp to handle 2nd format ptids.

* Mon Sep 27 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.33
- Don't unwind past a zero PC (when normal frames).

* Mon Sep 27 2004 Jeff Johnston  <jjohnstn@redhat.com>	1.200400607.32
- Add threaded watchpoint support for x86, x86-64, and ia64.

* Mon Sep 27 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.31
- Instead of deleting bigcore.exp, use runtest --ignore.

* Thu Sep 23 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.30
- Merge in mainline testsuite up to 2004-09-23, pick up sig*.exp tests.
  Merge in mainline infrun.c, pick up all infrun.c fixes.
  Generate bigcore's corefile from the running inferior.
  Limit bigcore's corefile to max file-size.

* Thu Sep 02 2004 Jeff Johnston  <jjohnstn@redhat.com>	1.200400607.29
- Fix low-level lin-lwp code to wait specifically for any stepping
  LWP (bugzilla 130896)

* Tue Aug 31 2004 Jeff Johnston  <jjohnstn@redhat.com>	1.200400607.28
- Add test case for bugzilla 128618 fix.

* Mon Aug 30 2004 Jeff Johnston  <jjohnstn@redhat.com>	1.200400607.27
- Add support for breakpoints in manually loaded/unloaded shared libs.
  (bugzilla 128618)

* Mon Aug 30 2004 Jeff Johnston  <jjohnstn@redhat.com>	1.200400607.26
- Add java inferior call support.

* Mon Aug 30 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.25
- Convert "main" the function descriptor, into an address.

* Mon Aug 30 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.24
- Fix single-stepping when a signal is pending, was exiting program.
  -- needs kernel fix so that ptrace(PT_STEP,SIG) doesn't do a PT_CONT.
  -- sigstep.exp tests pass with this fix applied.

* Mon Aug 30 2004 Elena Zannoni <ezannoni@redhat.com>	1.200400607.23
- Delete some part of gdb-6.1post-test-rh.patch, to avoid confusing
  gdb when testing itself, and loading separate debug info.

* Fri Aug 13 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.22
- Check in gdb mainline fix for applications calling clone directly.

* Tue Aug 10 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.21
- Alter libunwind frame code to allow using libunwind 0.97 and up.

* Tue Aug 03 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.20
- Fix the ia64 libunwind test to match current output.

* Fri Jul 30 2004 Elena Zannoni <ezannoni@redhat.com>	1.200400607.19
- Fix the tests where gdb debugs itself, as to not copy
  the executable to xgdb.

* Mon Jul 26 2004 Elena Zannoni <ezannoni@redhat.com>	1.200400607.18
- Add Pie patches back in.

* Fri Jul 16 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.17
- Fix stepping over a no-debug shared-library function.
- Fix patch vsyscall patch name.

* Thu Jul 8 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.16
- Update thread code with fix from gdb HEAD

* Wed Jul 7 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.15
- disable vsyscall
- import Bob's crasher fix
- disable bigcore.exp

* Mon Jul 5 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.14
- Make large corefiles work on systems that require O_LARGEFILE.

* Tue Jun 29 2004 Elena Zannoni <ezannoni@redhat.com>	1.200400607.13
- Fix BuildRequires for libunwind on ia64.

* Mon Jun 28 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.12
- Import wild frame ID patch.  Stops GDB incorrectly matching invalid
  frame IDs.
- Disable bigcore on ia64 and amd64.

* Fri Jun 25 2004 Andrew Cagney <cagney@redhat.com>     1.200400607.11
- Fix testsuite to kill attach process (from corrinna/mainline).
- Fix build problems with vsyscall patch.

* Fri Jun 25 2004 Andrew Cagney <cagney@redhat.com>     1.200400607.10
- Fix annotate test messages.
- Recognize VSYSCALL pages.

* Thu Jun 24 2004 Jeff Johnston <jjohnstn@redhat.com>	1.200400607.9
- Fix ia64 watchpoint support.

* Wed Jun 23 2004 Andrew Cagney <cagney@redhat.com>     1.200400607.8
- Do not xfail signals on i387, convert KFAIL to FAIL and not XFAIL.

* Wed Jun 23 2004 Andrew Cagney <cagney@redhat.com>     1.200400607.7
- Fix to ppc64 unwinder - handle glibcs function within syscall
  function hack.
- Update sigbpt.exp, ena-dis-br.exp observer.exp signull.exp,
  step-test.exp and sizeof.exp, so that test names are architecture
  clean.
- Disable bigcore.exp on PowerPC 64.

* Tue Jun 22 2004 Andrew Cagney <cagney@redhat.com>     1.200400607.6
- Merge in mainline testsuite changes up to 2004-06-21.
- Re-implement 32 and 64-bit PPC signal trampolines.
- Check i386 and amd64 signal trampolines before dwarf2.
- Allow tramp-frame when there is a symbol.
- Test interaction between single-step, breakpoint and signal.
- ABI: Fix PPC64 function parameters, sizeof long-double, and enum
  return values.

* Mon Jun 21 2004 Elena Zannoni <ezannoni@redhat.com>	1.200400607.5
- Fix sed line for gz info files.

* Mon Jun 21 2004 Andrew Cagney <cagney@redhat.com>	1.200400607.4
- Tar/uuencode both the .sum and .log test results.

* Tue Jun 15 2004 Elena Zannoni <ezannoni@redhat.com>	0.200400607.3
- Remove installation of mmalloc, and its info files.
- Add hack to deal with differring info files generated by makeinfo.
- Restore release number convention.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 10 2004 Elena Zannoni <ezannoni@redhat.com>	0.200400607.2
- Fix Requires and BuildRequires for libunwind dependencies.
- Add patch to silence gcc3.4 warnings.

* Wed Jun 09 2004 Elena Zannoni <ezannoni@redhat.com>	0.200400607.1
- New import: revamp everything. Remove all patches for now.
- Update the Requires and BuildRequires sections.
- Removed stupid Ada testcases (there is no ada support in gdb yet).

* Mon May 10 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.20
- Disable PIE again.
- obsolete gdb64 only if on ppc64.

* Mon May 03 2004 Jeff Johnston <jjohnstn@redhat.com>	0.20040223.19
- Add -u parameter to build ChangeLog patch.

* Mon May 03 2004 Jeff Johnston <jjohnstn@redhat.com>	0.20040223.18
- Update thread fix made for .6 release to FSF version.

* Thu Apr 22 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.17
- Disable PIE again.

* Thu Apr 22 2004 Jeff Johnston <jjohnstn@redhat.com>	0.20040223.16
- Bump version number.

* Wed Apr 21 2004 Jeff Johnston <jjohnstn@redhat.com>	0.20040223.15
- fix ia64 info frame command
- also fix ia64 tdep file for which elf header file to include

* Tue Mar 30 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.14
- re-enable pie.

* Tue Mar 30 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.13
- Fix testsuite glitches.

* Thu Mar 24 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.12
- Fix typo.

* Thu Mar 24 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.11
- Make gdb compile w/o warnings with gcc-3.4.
- Reenable PIE support code.

* Wed Mar 23 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.10
- Bump version number

* Wed Mar 23 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.9
- temporarily disable PIE support.
- Add section to obsolete gdb64 package.

* Sun Mar 21 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.8
- Add support for debugging of PIE executables.

* Tue Mar 09 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.7
- Bump version number.

* Mon Mar 08 2004 Jeff Johnston <jjohnstn@redhat.com>	0.20040223.6
- Fix thread support to recognize new threads even when they reuse
  tids of expired threads.  Also ensure that terminal is held by gdb
  while determining if a thread-create event has occurred.

* Mon Mar 08 2004 Andrew Cagney <cagney@redhat.com>	0.20040223.5
- Sync with 6.1 branch; eliminate all amd64 patches;
  add more robust 32x64 PPC64 patches.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 2 2004 Andrew Cagney <cagney@redhat.com>	0.20040223.4
- 32x64 fixes that work with threads, replaced old
  non-thread 32x64 patch, add nat patch.

* Wed Feb 25 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.3
- Add patch for x86_64 in 32 bit mode.

* Wed Feb 25 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.2
- Remove ppc64 hacks.
- Refresh some patches.

* Wed Feb 25 2004 Elena Zannoni <ezannoni@redhat.com>	0.20040223.1
- Import new gdb snapshot from mainline FSF.
- Update patch list.

* Tue Feb 17 2004 Jeff Johnston <jjohnstn@redhat.com>	1.20031117.8
- Switch ia64-tdep.c to use new abi used by libunwind-0.95 and up.
- Fix gate area specification for ia64-linux-tdep.c.
- Fix long double support for ia64.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 08 2004 Elena Zannoni <ezannoni@redhat.com>	0.20031117.7
- Add fixes for ppc32 support on ppc64 platform, from Andrew Cagney.

* Tue Jan 06 2004 Elena Zannoni <ezannoni@redhat.com>	0.20031117.6
- Add patch to have unique binary names in the testsuite.
- Disable s390/s390x pthread.exp test (FIXME)
- Don't install any info files for the ppc platform. Let's take them
  from the ppc64 one (or we get install conflicts).
- Remove generated info files from the source tree. They are generated
  as part of the FSF snapshot process.

* Mon Nov 24 2003 Elena Zannoni <ezannoni@redhat.com>	0.20031117.5
- Add patches from old rpm for i386 support on x86_64.
- Add build dependency on libunwind for ia64.

* Fri Nov 21 2003 Jeremy Katz <katzj@redhat.com> 0.20031117.4
- more rpm tricks to get the gdb64 package happier

* Thu Nov 20 2003 Elena Zannoni <ezannoni@redhat.com>	0.20031117.3
- Add sick and twisted workaround for ppc64 architecture.

* Wed Nov 19 2003 Elena Zannoni <ezannoni@redhat.com>	0.20031117.2
- Fix typo in libunwind test.

* Tue Nov 18 2003 Elena Zannoni <ezannoni@redhat.com>	0.20031117.1
- Import new gdb snapshot from mainline FSF.
- Fix some testfiles. 
- Add fixes for gcore, and patch for libunwind support on ia64.
- Add tests to see what versions of gcc, binutils, glibc and kernel we
  are running with.

* Wed Oct 15 2003 Elena Zannoni <ezannoni@redhat.com>	0.20030710.41
- Bump up version number.

* Wed Sep 24 2003 Elena Zannoni <ezannoni@redhat.com>	0.20030710.40
- Fix problem with gcore and single threaded programs. (bugzilla 103531)

* Mon Sep 22 2003 Jeff Johnston <jjohnstn@redhat.com>	0.20030710.39
- Fix call to quit_target from quit_force.

* Sun Sep 21 2003 Andrew Cagney <cagney@redhat.com>	0.20030710.38
- Fix PPC64 push dummy call.
- Re-fix PPC64 return value (had wrong / old patch).

* Sat Sep 20 2003 Andrew Cagney <cagney@redhat.com>	0.20030710.37
- Fix PPC32 return values.

* Sat Sep 20 2003 Andrew Cagney <cagney@redhat.com>	0.20030710.36
- Rewrite ppc64 retun value methods so that they (hopefully)
match the SysV spec.
- Enable ppc64 testsuite.

* Thu Sep 18 2003 Andrew Cagney <cagney@redhat.com>	0.20030710.35
- Hack around problem "break main" vs "break .main" when there is
only a minimal ppc64 symbol table.  The former is a function descriptor
and not where you want the breakpoint to go.  Only convert descriptors
to pointers when the address is in the ".opd" section.

* Wed Sep 17 2003 Andrew Cagney <cagney@redhat.com>	0.20030710.34
- Fix ppc32 push_dummy_call.

* Tue Sep 16 2003 Andrew Cagney <cagney@redhat.com>	0.20030710.33
- Pack gdb.sum and gdb.log using uuencode and bzip.

* Tue Sep 16 2003 Jeff Johnston <jjohnstn@redhat.com>   0.20030710.32
- Catch errors when quitting so exit of gdb still occurs.

* Mon Sep 15 2003 Andrew Cagney <cagney@redhat.com>     0.20030710.31
- Fix ppc32 use_struct_convention.

* Thu Sep 11 2003 Andrew Cagney <cagney@redhat.com>     0.20030710.30
- Mods to dwarf2-frame.c to work around a lack of GCC/CFI info.

* Thu Sep 11 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.29
- Bump up version number.

* Wed Sep 10 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.28
- Fix a core dump with MI.
- Add new ChangeLog patch for mi changes.

* Thu Sep 04 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.27
- Change the name of the package to gdb64 in ppc64 case.

* Tue Aug 26 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.26
- Add testcase for separate debug info.

* Tue Aug 26 2003 Andrew Cagney <cagney@redhat.com>     0.20030710.25
- fix i386 on x86-64 TLS
- add "base-aug2003" suffix to older x86i386 patch

* Tue Aug 26 2003 Andrew Cagney <cagney@redhat.com>     0.20030710.24
- skip the ppc64 and x86-64 frame redzone.
 
* Fri Aug 22 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.23
- Relax one testcase in selftest.exp a bit.
- Accept different output as well in thread bt (platform dependent).
- Enable testsuite run for ia64, ppc, s390 and s390x. They are in
  reasonably good shape.

* Thu Aug 21 2003 Jeff Johnston  <jjohnstn@redhat.com>  0.20030710.22
- Multiple ia64 fixes.
- Fix ia64 printing of function pointers.
- Fix ia64 prologue examination to ignore predicated insns if we
  haven't found the return address yet.
- Skip dump.exp testcase for ia64

* Thu Aug 21 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.21
- Bump release number.

* Wed Aug 20 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.20
- Relax pattern in annota2.exp test.

* Wed Aug 20 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.19
- rename gdb binary to gdb64 for ppc64 platform.

* Tue Aug 19 2003 Jeff Johnston  <jjohnstn@redhat.com>  0.20030710.18
- Fix ia64 pc unwinding to include psr slot.
 
* Mon Aug 18 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.17
- Fix info installation for annotate.texi. (Bugzilla 102521)
 
* Fri Aug 15 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.16
- revamp tls tests a bit.
- Handle new output from gdb in relocate.exp

* Wed Aug 13 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.15
- Fix problem for processing of separate debug info files.

* Wed Aug 13 2003 Jeff Johnston  <jjohnstn@redhat.com>   0.20030710.14
- add ia64.inc file for testing ia64 in gdb.asm testsuite

* Fri Aug 8 2003 Andrew Cagney  <cagney@redhat.com>   0.20030710.13
- print the libthread_db library path, print when threads are enabled

* Thu Aug 7 2003 Andrew Cagney  <cagney@redhat.com>   0.20030710.12
- "cat" the test log into the build log

* Wed Aug 06 2003 Jeff Johnston  <jjohnstn@redhat.com>  0.20030710.11
- modernize ia64 gdb to use new frame model
- remove/replace deprecated interfaces used by ia64 gdb

* Wed Aug 06 2003 Andrew Cagney  <cagney@redhat.com>   0.20030710.10
- Sync to gdb-5.3.90-sync-20030806.patch.

* Wed Jul 29 2003 Andrew Cagney  <cagney@redhat.com>   0.20030710.9
- add x86-64 i386 fixes

* Tue Jul 29 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.8
- Fix some tests by xfailing the correct target triplet for RedHat.
- Remove include of config.h from pthreads.c testcases.

* Mon Jul 28 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.7
- Fix some test failures, by escaping correctly.

* Thu Jul 24 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.6
- Remove one testcase that is redundant.

* Wed Jul 23 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.5
- Bump up release number.

* Wed Jul 23 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.4
- Bring in sync with current head of gdb-6 branch.
- Remove linespec patch, because included in the new sync patch.

* Fri Jul 18 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.3
- Add patch to avoid gdb segfault with bad debug info.
- Change location of build tree to avoid conflicts with older versions
  possibly installed.

* Thu Jul 17 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.2
- Add patch to synchronize the current snapshot with the gdb-6 branch head.
- Remove some patches that are includd in such diff.
- Enable tests on AMD64 as well.

* Fri Jul 11 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20030710.1
- Import new gdb snapshot.
- Revamp gdb.spec. Get rid of patches that apply to older versions.
- Add patches for ppc64 support, kfail and make gdb more robust in copingi
  with bad debug info.

* Wed Jul 02 2003 Jeff Johnston  <jjohnstn@redhat.com>  1.20021129.39
- Fix bug with ia64 checking of hardware breakpoints.

* Mon Jun 30 2003 Elena Zannoni  <ezannoni@redhat.com>  1.20021129.38
- Add necessary function for NPTL support on x86-64.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20021129.37
* Tue Jun 03 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20021129.36
- Enable warnings for x86_64, not x86-64.
- Fix warnings from infptrace.c and dwarfread.c.
- Print error message only when reading separate debug info really
  doesn't work (jimb@redhat.com).

* Fri May 23 2003 Elena Zannoni  <ezannoni@redhat.com>  0.20021129.35
- Fixes for fetching and storing access registers on s390x (jimb@redhat.com).
  Bugzilla 91455.

* Wed May 21 2003 Jeff Johnston  <jjohnstn@redhat.com>  0.20021129.34
- Do not generate error on detach failure.  Bugzilla 90900.

* Thu May 8 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.33
- New tests for asm on s390x (jimb@redhat.com). Bugzilla 90503.
- Fixes for prologue analysis on s390x (jimb@redhat.com). Bugzilla 90506.
- bfd fix for 64-bit platforms (jimb@redhat.com).
- Disable ppc64 builds until we have a port.

* Thu May 1 2003 Jeff Johnston  <jjohnstn@redhat.com>  0.20021129.32
- Add ia64 support to the float.exp testcase.

* Thu May 1 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.31
- Clean up the tls tests some more.
- Fix problem with non US-eng locale. Bugzilla bug 88823.

* Wed Apr 30 2003 Jeff Johnston <jjohnstn@redhat.com>  0.20021129.30
- Fix ia64 prologue skipping.
- Fix ia64 line table.
- Fix setting of prev_pc in infrun.c.

* Mon Mar 31 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.29
- Include the gcore script, as gdb_gcore.sh and install it in
  /usr/bin as gcore.
- One more disassembly fix for core files. Added to
  gdb-5.3post-disasm-mar2003.patch. Bugzilla 87677.
- Enable build warnings for x86-64.

* Mon Mar 31 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.28
- Fix Java strings printing.
- Fix memory corruption in disassembly code. Bugzilla 85644.
- Testsuite fixes (jimb@redhat.com). Bugzilla 85457.
- Fixes for s390 stack handling (jimb@redhat.com). Bugzilla 85039.
- Fixes for s390 struct return (jimb@redhat.com).

* Wed Mar 26 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.27
- Fixes for disassembly of code in threaded applications. Bugzilla 87495.
- Fixes for s390 prologue analysis. (jimb@redhat.com).
  Bugzilla bugs 85251, 85214.

* Thu Mar 20 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.26
- Fix inferior function calls with void return on x86-64. Bugzilla bug 83197.
- Fix for upstream PR/699.
- Fix some problems with gdb-5.3post-thrtst-feb2003.patch.

* Wed Mar 19 2003 Jeff Johnston <jjohnstn@redhat.com>  0.20021129.25
- Fix for thread-db.c: check_event() - Bugzilla bug 86231.

* Fri Mar 14 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.24
- Fix some problems with inferior function calls on x86-64.

* Fri Mar 07 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.23
- testsuite patches. Bugzilla 85215 85028 85335.

* Thu Mar 06 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.22
- Fix testsuite problems related to having '+' in the directory name.
  Bugzilla 85031.

* Mon Mar 03 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.21
- Fix a few inferior function call problems.

* Mon Mar 03 2003 Elena Zannoni <ezannoni@redhat.com>  0.20021129.20
- Split the changelog patches in two. Cleanup messy patch section.

* Thu Feb 27 2003 Jeff Johnston <jjohnstn@redhat.com>  0.20021129.19
- Perform run-time check for tkill syscall in lin-lwp.c.

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

* Wed Aug 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.2.1-3
- Add changelogs to the previous patch

* Wed Aug 14 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.2.1-2
- Add some patches from Elena Zannoni <ezannoni@redhat.com>

* Tue Jul 23 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.2.1-1
- 5.2.1

* Mon Jul 22 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- compile on mainframe

* Mon Jul  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.2-3
- Rebuild

* Tue May  7 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.2-2
- Rebuild

* Mon Apr 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.2-1
- 5.2

* Mon Apr 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.92-1
- 5.1.92. Hopefully identical to 5.2 final

* Mon Apr 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.91-1
- 5.1.91. 5.2 expected in a week

* Thu Mar 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.90CVS-5
- Update to current

* Thu Mar 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.90CVS-4
- Update to current

* Thu Mar 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.90CVS-3
- Update to current

* Wed Mar 20 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.90CVS-2
- Update to current

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.90CVS-1
- Update to current 5.2 branch 

* Thu Jan 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.1-1
- 5.1.1
- add URL

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Dec 10 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.1-2
- Fix some thread+fpu problems

* Mon Nov 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.1-1
- 5.1

* Mon Nov 19 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.94-0.71
- 5.0.94. Almost there....

* Mon Nov 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.93-2
- Add patch from jakub@redhat.com to improve handling of DWARF

* Mon Nov 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.93-1
- 5.0.93 
- handle missing info pages in post/pre scripts

* Wed Oct 31 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.92-1
- 5.0.92

* Fri Oct 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.91rh-1
- New snapshot
- Use the 5.0.91 versioning from the snapshot

* Wed Oct 17 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-17
- New snapshot

* Thu Sep 27 2001 Trond Eivind Glomsrød <teg@redhat.com> 
- New snapshot

* Wed Sep 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-16
- New snapshot 

* Mon Aug 13 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-15
- Don't buildrequire compat-glibc (#51690)

* Thu Aug  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot, from the stable branch eventually leading to gdb 5.1

* Mon Jul 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Add texinfo to BuildRequires

* Mon Jun 25 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Fri Jun 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot
- Add ncurses-devel to buildprereq
- Remove perl from buildprereq, as gdb changed the way 
  version strings are generated

* Thu Jun 14 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Wed May 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot - this had thread fixes for curing #39070
- New way of specifying version

* Tue May  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New tarball
- Kevin's patch is now part of gdb

* Mon Apr  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add patch from kevinb@redhat.com to fix floating point + thread 
  problem (#24310)
- remove old workarounds
- new snapshot

* Thu Apr  5 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

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
