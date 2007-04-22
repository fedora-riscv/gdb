# Define this if you want to skip the strip step and preserve debug
# info.  Useful for testing.
#define __spec_install_post /usr/lib/rpm/brp-compress || :

Summary: A GNU source-level debugger for C, C++, Java and other languages.
Name: gdb

# Set version to contents of gdb/version.in.
# NOTE: the FSF gdb versions are numbered N.M for official releases, like 6.3 
# and, since January 2005, X.Y.Z.date for daily snapshots, like 6.3.50.20050112 # (daily snapshot from mailine), or 6.3.0.20040112 (head of the release branch).
Version: 6.6

# The release always contains a leading reserved number, start it at 1.
Release: 9%{?dist}

License: GPL
Group: Development/Debuggers
Source: ftp://ftp.gnu.org/gnu/gdb/gdb-6.6.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-root
URL: http://gnu.org/software/gdb/

# For our convenience
%define gdb_src gdb-6.6
%define gdb_build %{gdb_src}/build-%{_target_platform}

# Make sure we get rid of the old package gdb64, now that we have unified
# support for 32-64 bits in one single 64-bit gdb.
%ifarch ppc64
Obsoletes: gdb64
%endif

# GDB patches have the format gdb-<version>-bz<red-hat-bz-#>-<desc>.patch;
# should include the ChangeLog.RedHat change-log entry; and should be
# created using diff -u ./gdb (not gdb-6.3/gdb).

# Red Hat local patches

Patch0: gdb-6.3-rh-changelogs-20041202.patch

# Work around out-of-date dejagnu that does not have KFAIL
Patch1: gdb-6.3-rh-dummykfail-20041202.patch

# Match Red Hat's version info
Patch2: gdb-6.3-rh-testversion-20041202.patch

# Check that libunwind works - new test then fix
Patch3: gdb-6.3-rh-testlibunwind-20041202.patch
Patch4: gdb-6.3-rh-testlibunwind1fix-20041202.patch


# ------------------------------------------

# Add fixes starting at 100

# Recognize i386 signal trampolines before CFI.  Ensures that signal
# frames are identified as signal frames.
Patch101: gdb-6.3-sigx86-20040621.patch

# Use convert_from_func_ptr_addr on the solib breakpoint address;
# simplifies and makes more consistent the logic.
Patch104: gdb-6.3-ppcdotsolib-20041022.patch

# Better parse 64-bit PPC system call prologues.
Patch105: gdb-6.3-ppc64syscall-20040622.patch

# Stop a backtrace when a zero PC is encountered.
Patch106: gdb-6.3-framepczero-20040927.patch

# Pass the pc's section into the symbol search code; stops the lookup
# finding a symbol from the wrong section.
Patch108: gdb-6.3-ppc64section-20041026.patch

# Include the pc's section when doing a symbol lookup so that the
# correct symbol is found.
Patch111: gdb-6.3-ppc64displaysymbol-20041124.patch

# Fix stepping in threads
Patch112: gdb-6.3-thread-step-20041207.patch

# Threaded watchpoint support
Patch113: gdb-6.3-threaded-watchpoints-20041213.patch

# Fix to expose multiple constructors to end-user
Patch115: gdb-6.3-constructor-20041216.patch

# Fix to display base constructors from list and breakpoint commands
Patch116: gdb-6.3-linespec-20041213.patch

# Continue removing breakpoints even when failure occurs.
Patch117: gdb-6.3-removebp-20041130.patch

# Add a wrapper script to GDB that implements pstack using the
# --readnever option.
Patch118: gdb-6.3-gstack-20050411.patch

# Fix for caching thread lwps for linux
Patch119: gdb-6.3-lwp-cache-20041216.patch

# Fix to ensure types are visible
Patch120: gdb-6.3-type-fix-20041213.patch

# VSYSCALL and PIE
Patch122: gdb-6.3-test-pie-20050107.patch
Patch124: gdb-6.3-pie-20050110.patch

# Get selftest working with sep-debug-info
Patch125: gdb-6.3-test-self-20050110.patch

# Fix for non-threaded watchpoints.
Patch128: gdb-6.3-nonthreaded-wp-20050117.patch

# Add PPC .symbols to min-symtable.
Patch130: gdb-6.3-ctorline-20050120.patch

# Fix to support multiple destructors just like multiple constructors
Patch133: gdb-6.3-test-dtorfix-20050121.patch
Patch134: gdb-6.3-dtorfix-20050121.patch

# Fix to support executable moving
Patch136: gdb-6.3-test-movedir-20050125.patch

# Fix to support unwinding syscalls in ia64 corefiles
# Patch138: gdb-6.3-ia64-corefile-fix-20050127.patch

# Tolerate DW_AT_type referencing <0>.
Patch139: gdb-6.3-dwattype0-20050201.patch

# Fix gcore for threads
Patch140: gdb-6.3-gcore-thread-20050204.patch

# Fix stepping over thread exit
Patch141: gdb-6.3-step-thread-exit-20050211.patch

# Prevent gdb from being pushed into background
Patch142: gdb-6.3-terminal-fix-20050214.patch

# Allow sibling threads to set threaded watchpoints for x86 and x86-64
Patch145: gdb-6.3-threaded-watchpoints2-20050225.patch

# Fix unexpected compiler warning messages.
Patch147: gdb-6.3-warnings-20050317.patch

# Fix printing of inherited members
Patch148: gdb-6.3-inheritance-20050324.patch

# Add vsyscall page support for ia64.
Patch149: gdb-6.3-ia64-vsyscall-20050330.patch

# Print a warning when the separate debug info's CRC doesn't match.
Patch150: gdb-6.3-test-sepcrc-20050402.patch
Patch151: gdb-6.3-sepcrc-20050402.patch

# Do not issue warning message about first page of storage for ia64 gcore
Patch153: gdb-6.3-ia64-gcore-page0-20050421.patch

# Security errata for untrusted .gdbinit
Patch157: gdb-6.3-security-errata-20050610.patch

# IA64 sigtramp prev register patch
Patch158: gdb-6.3-ia64-sigtramp-frame-20050708.patch

# IA64 sigaltstack patch
Patch159: gdb-6.3-ia64-sigaltstack-20050711.patch

# IA64 gcore speed-up patch
Patch160: gdb-6.3-ia64-gcore-speedup-20050714.patch

# Notify observers that the inferior has been created
Patch161: gdb-6.3-inferior-notification-20050721.patch

# Fix ia64 info frame bug
Patch162: gdb-6.3-ia64-info-frame-fix-20050725.patch

# Verify printing of inherited members test
Patch163: gdb-6.3-inheritancetest-20050726.patch

# Add readnever option
Patch164: gdb-6.3-readnever-20050907.patch

# Remove extraneous xfree
Patch165: gdb-6.3-xfree-20050922.patch

# Fix frame pointer for ia64 sigtramp frame
Patch166: gdb-6.3-ia64-sigtramp-fp-20050926.patch

# Fix ia64 gdb problem with user-specified SIGILL handling
Patch169: gdb-6.3-ia64-sigill-20051115.patch

# Allow option to continue backtracing past a zero pc value
Patch170: gdb-6.3-bt-past-zero-20051201.patch

# Use bigger numbers than int.
Patch176: gdb-6.3-large-core-20051206.patch

# Hard-code executable names in gstack, such that it can run with a
# corrupted or missing PATH.
Patch177: gdb-6.3-gstack-without-path-20060414.patch

# Do not let errors related with debug registers break thread debugging.
Patch178: gdb-6.3-catch-debug-registers-error-20060527.patch

# Cope with waitpid modifying status even when returning zero, as on
# ia32el.
Patch179: gdb-6.3-ia32el-fix-waitpid-20060615.patch

# Bugfix segv on the source display by ^X 1 (fixes Patch130, BZ 200048).
Patch181: gdb-6.5-bz200048-find_line_pc-segv.patch

# Bugfix object names completion (fixes Patch116, BZ 193763).
Patch185: gdb-6.3-bz193763-object-name-completion.patch

# Testcase for corrupted or missing location list information (BZ 196439).
Patch187: gdb-6.5-bz196439-valgrind-memcheck-compat-test.patch

# Fix debuginfo addresses resolving for --emit-relocs Linux kernels (BZ 203661).
Patch188: gdb-6.5-bz203661-emit-relocs.patch

# Security patch: avoid stack overflows in dwarf expression computation.
# CVE-2006-4146
Patch190: gdb-6.5-dwarf-stack-overflow.patch

# Fix gdb printf command argument using "%p" (BZ 205551).
Patch191: gdb-6.5-bz205551-printf-p.patch

# Fix attach to stopped process, supersede `gdb-6.3-attach-stop-20051011.patch'.
# Fix attachment also to a threaded stopped process (BZ 219118).
Patch193: gdb-6.5-attach-stop.patch

# Support TLS symbols (+`errno' suggestion if no pthread is found) (BZ 185337).
# FIXME: Still to be updated.
Patch194: gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch

# Fix TLS symbols resolving for objects with separate .debug file (-debuginfo).
Patch195: gdb-6.5-tls-of-separate-debuginfo.patch

# Fix TLS symbols resolving for shared libraries with a relative pathname.
# The testsuite needs `gdb-6.5-tls-of-separate-debuginfo.patch'.
Patch196: gdb-6.5-sharedlibrary-path.patch

# Support IPv6 for gdbserver (BZ 198365).
Patch197: gdb-6.5-bz198365-IPv6.patch

# Suggest fixing your target architecture for gdbserver(1) (BZ 190810).
# FIXME: It could be autodetected.
Patch199: gdb-6.5-bz190810-gdbserver-arch-advice.patch 

# Fix dereferencing registers for 32bit inferiors on 64bit hosts (BZ 181390).
Patch200: gdb-6.5-bz181390-memory-address-width.patch

# Fix `gcore' command for 32bit inferiors on 64bit hosts.
Patch201: gdb-6.5-gcore-i386-on-amd64.patch

# Testcase for deadlocking on last address space byte; for corrupted backtraces.
Patch211: gdb-6.5-last-address-space-byte-test.patch

# Fix "??" resolving of symbols from (non-prelinked) debuginfo packages.
Patch206: gdb-6.5-relativedebug.patch

# Fix "??" resolving of symbols from overlapping functions (nanosleep(3)).
Patch207: gdb-6.5-symbols-overlap.patch

# Improved testsuite results by the testsuite provided by the courtesy of BEA.
Patch208: gdb-6.5-BEA-testsuite.patch

# Fix readline segfault on excessively long hand-typed lines.
Patch209: gdb-6.5-readline-long-line-crash.patch
Patch213: gdb-6.5-readline-long-line-crash-test.patch

# Fix readline history for input mode commands like `command' (BZ 215816).
Patch212: gdb-6.5-bz215816-readline-from-callback.patch
Patch219: gdb-6.5-bz215816-readline-from-callback-test.patch

# Fix bogus 0x0 unwind of the thread's topmost function clone(3) (BZ 216711).
Patch214: gdb-6.5-bz216711-clone-is-outermost.patch

# Try to reduce sideeffects of skipping ppc .so libs trampolines (BZ 218379).
Patch215: gdb-6.5-bz218379-ppc-solib-trampoline-fix.patch
Patch216: gdb-6.5-bz218379-ppc-solib-trampoline-test.patch 

# Fix lockup on trampoline vs. its function lookup; unreproducible (BZ 218379).
Patch217: gdb-6.5-bz218379-solib-trampoline-lookup-lock-fix.patch

# Fix unwinding crash on older gcj(1) code (extended CFI support) (BZ 165025).
Patch221: gdb-6.5-bz165025-DW_CFA_GNU_negative_offset_extended-fix.patch
Patch222: gdb-6.5-bz165025-DW_CFA_GNU_negative_offset_extended-test.patch

# Find symbols properly at their original (included) file (BZ 109921).
Patch224: gdb-6.5-bz109921-DW_AT_decl_file-fix.patch
Patch225: gdb-6.5-bz109921-DW_AT_decl_file-test.patch

# Fix unwinding of non-CFI (w/o debuginfo) PPC code by recent GCC (BZ 140532).
Patch226: gdb-6.3-bz140532-ppcnoncfi-skip_prologue-PIC.patch
# Fix unwinding of non-debug (.eh_frame) PPC code, Andreas Schwab (BZ 140532).
Patch227: gdb-6.5-bz140532-ppc-eh_frame-regnum.patch
# Fix unwinding of debug (.debug_frame) PPC code, workaround GCC (BZ 140532).
Patch228: gdb-6.5-bz140532-ppc-debug_frame-return_address.patch
Patch229: gdb-6.5-bz140532-ppc-debug_frame-return_address-test.patch

# Fix missing testsuite .log output of testcases using get_compiler_info().
Patch230: gdb-6.5-testsuite-log.patch

# Testcase for exec() from threaded program (BZ 202689).
Patch231: gdb-6.3-bz202689-exec-from-pthread-test.patch

# Backported post gdb-6.6 release fixups.
Patch232: gdb-6.6-upstream.patch

# Testcase for PPC Power6/DFP instructions disassembly (BZ 230000).
Patch234: gdb-6.6-bz230000-power6-disassembly-test.patch

# Temporary support for shared libraries >2GB on 64bit hosts. (BZ 231832)
Patch235: gdb-6.3-bz231832-obstack-2gb.patch

# Suggest SELinux permissions problem; no assertion failure anymore (BZ 232371).
Patch236: gdb-6.6-bz232371-selinux-thread-error.patch

# Use definition of an empty structure as it is not an opaque type (BZ 233716).
Patch238: gdb-6.6-bz233716-empty-structure-override.patch

# Use the runtime variant of `libunwind-ARCH.so.7' rather than the `.so' one.
Patch244: gdb-6.6-libunwind-major-version.patch

# Allow running `/usr/bin/gcore' with provided but inaccessible tty (BZ 229517).
Patch245: gdb-6.6-bz229517-gcore-without-terminal.patch

# Fix testcase for watchpoints in threads (for BZ 237096).
Patch246: gdb-6.6-bz237096-watchthreads-testcasefix.patch

BuildRequires: ncurses-devel glibc-devel gcc make gzip texinfo dejagnu gettext
BuildRequires: flex bison sharutils

%define multilib_64_archs sparc64 ppc64 s390x x86_64
%ifarch %{multilib_64_archs} sparc ppc
# Ensure glibc{,-devel} is installed for both multilib arches
BuildRequires: /lib/libc.so.6 /usr/lib/libc.so /lib64/libc.so.6 /usr/lib64/libc.so
%endif

%ifarch ia64
BuildRequires: libunwind-devel >= 0.99-0.1.frysk20070405cvs
Requires: libunwind >= 0.99-0.1.frysk20070405cvs
%else
BuildRequires: prelink
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

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%patch101 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch108 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch122 -p1
%patch124 -p1
%patch125 -p1
%patch128 -p1
%patch130 -p1
%patch133 -p1
%patch134 -p1
%patch136 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch145 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch153 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch169 -p1
%patch170 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch181 -p1
%patch185 -p1
%patch187 -p1
%patch188 -p1
%patch190 -p1
%patch191 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
#%patch197 -p1
%patch199 -p1
%patch200 -p1
%patch201 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch219 -p1
%patch221 -p1
%patch222 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1
%patch227 -p1
%patch228 -p1
%patch229 -p1
%patch230 -p1
%patch231 -p1
%patch232 -p1
%patch234 -p1
%patch235 -p1
%patch236 -p1
%patch238 -p1
%patch244 -p1
%patch245 -p1
%patch246 -p1

# Change the version that gets printed at GDB startup, so it is RedHat
# specific.
cat > gdb/version.in << _FOO
Red Hat Linux (%{version}-%{release}rh)
_FOO

# Remove the info and other generated files added by the FSF release
# process.
rm -f gdb/doc/*.info
rm -f gdb/doc/*.info-*

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

../configure						\
	--prefix=%{_prefix}				\
	--libdir=%{_libdir}				\
	--sysconfdir=%{_sysconfdir}			\
	--mandir=%{_mandir}				\
	--infodir=%{_infodir}				\
	$enable_build_warnings				\
	--with-separate-debug-dir=/usr/lib/debug	\
%ifarch ia64
	--with-libunwind				\
%else
	--without-libunwind				\
%endif
    %{_target_platform}

make -k
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
# "chng-syms.exp" for possibly avoiding Linux kernel crash - Bug 207002.
# "threadcrash.exp" is incompatible on ia64 with old kernels.
make -k check RUNTESTFLAGS='--ignore "bigcore.exp chng-syms.exp checkpoint.exp threadcrash.exp"' || :
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
cp $RPM_BUILD_DIR/%{gdb_src}/gdb/NEWS $RPM_BUILD_DIR/%{gdb_src}

%install
cd ../%{gdb_build}
rm -rf $RPM_BUILD_ROOT

%makeinstall

# install the gcore script in /usr/bin
cp $RPM_BUILD_DIR/%{gdb_src}/gdb/gdb_gcore.sh $RPM_BUILD_ROOT%{_prefix}/bin/gcore
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
* Sun Apr 22 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-9
- Allow running `/usr/bin/gcore' with provided but inaccessible tty (BZ 229517).
- Fix testcase for watchpoints in threads (for BZ 237096).
- BuildRequires now `libunwind-devel' instead of the former `libunwind'.
- Use the runtime libunwind .so.7, it requires now >= 0.99-0.1.frysk20070405cvs.

* Sat Mar 24 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-8
- Use definition of an empty structure as it is not an opaque type (BZ 233716).
- Fixed the gdb.base/attachstop.exp testcase false 2 FAILs.

* Thu Mar 15 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-7
- Suggest SELinux permissions problem; no assertion failure anymore (BZ 232371).

* Wed Mar 14 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-6
- Fix occasional dwarf2_read_address: Corrupted DWARF expression (BZ 232353).

* Mon Mar 12 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-5
- Temporary support for shared libraries >2GB on 64bit hosts. (BZ 231832)

* Sun Feb 25 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-4
- Backport + testcase for PPC Power6/DFP instructions disassembly (BZ 230000).

* Mon Feb  5 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-3
- Fix a race during attaching to dying threads; backport (BZ 209445).
- Testcase of unwinding has now marked its unsolvable cases (for BZ 140532).

* Fri Jan 26 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-2
- Backported post gdb-6.6 release PPC `show endian' fixup.
- Fix displaying of numeric char arrays as strings (BZ 224128).
- Simplified patches by merging upstream accepted ones into a single file.

* Sat Jan 20 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.6-1
- Upgrade to GDB 6.6.  Drop redundant patches, forward-port remaining ones.
- Backported post gdb-6.6 release ia64 unwinding fixups.
- Testcase for exec() from threaded program (BZ 202689).

* Mon Jan 15 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-27
- Fix the testsuite results broken in 6.5-26, stop invalid testsuite runs.

* Fri Jan 13 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-26
- Fix unwinding of non-debug (.eh_frame) PPC code, Andreas Schwab (BZ 140532).
- Fix unwinding of debug (.debug_frame) PPC code, workaround GCC (BZ 140532).
- Fix missing testsuite .log output of testcases using get_compiler_info().

* Fri Jan 12 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-25
- Fix unwinding of non-CFI (w/o debuginfo) PPC code by recent GCC (BZ 140532).

* Thu Jan 11 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-24
- Backport readline history for input mode commands like `command' (BZ 215816).

* Tue Jan  9 2007 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-23
- Find symbols properly at their original (included) file (BZ 109921).
- Remove the stuck mock(1) builds disfunctional workaround (-> mock BZ 221351).

* Sat Dec 30 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-22
- Fix unwinding crash on older gcj(1) code (extended CFI support) (BZ 165025).
- Include testcase for the readline history of input mode commands (BZ 215816).

* Sat Dec 23 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-21
- Try to reduce sideeffects of skipping ppc .so libs trampolines (BZ 218379).
- Fix lockup on trampoline vs. its function lookup; unreproducible (BZ 218379).

* Tue Dec 19 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-20
- Fix bogus 0x0 unwind of the thread's topmost function clone(3) (BZ 216711).
- Testcase for readline segfault on excessively long hand-typed lines.

* Tue Dec 12 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-19
- Fix attachment also to a threaded stopped process (BZ 219118).
- Cleanup any leftover testsuite processes as it may stuck mock(1) builds.

* Sat Nov 25 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-18
- Fix readline history for input mode commands like `command' (BZ 215816).

* Wed Nov 16 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-17
- Bugfix testcase typo of gdb-6.5-16.

* Wed Nov 16 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-16
- Provide testcase for accessing the last address space byte.

* Wed Nov  9 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-15
- Fix readline segfault on excessively long hand-typed lines.

* Sat Nov  2 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-14
- Fix "??" resolving of symbols from (non-prelinked) debuginfo packages.
- Fix "??" resolving of symbols from overlapping functions (nanosleep(3)).
- Also disable testcase "checkpoint.exp" for a possible kernel Bug 207002.
- Provided (disabled during build) threading testsuite from BEA.

* Sat Oct 14 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-13
- Fix deadlock accessing last address space byte; for corrupted backtraces.

* Sun Oct  8 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-12
- Disabled IPv6 until its user visible syntax gets stable upstream.

* Sun Oct  1 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-11
- No longer disassemble invalid i386 opcodes of movQ/movA (BZ 172034).
- Simplify the IPv6 patch for gdbserver (BZ 198365).
- Suggest fixing your target architecture for gdbserver(1) (BZ 190810).
- Fix dereferencing registers for 32bit inferiors on 64bit hosts (BZ 181390).
- Fix `gcore' command for 32bit inferiors on 64bit hosts.

* Wed Sep 27 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-10
- Support IPv6 for gdbserver (BZ 198365).
- Temporarily disable testcase "chng-syms.exp" for a possible kernel Bug 207002.

* Wed Sep 21 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-9
- Fix crash on C++ symbol failing to be demangled (BZ 206813).
- Fix attach to stopped process, supersede `gdb-6.3-attach-stop-20051011.patch'.
- Fix TLS symbols resolving for objects with separate .debug file (-debuginfo).
- Fix TLS symbols resolving for shared libraries with a relative pathname.
- Support TLS symbols (+`errno' suggestion if no pthread is found) (BZ 185337).

* Mon Sep 11 2006 Jan Kratochvil <jan.kratochvil@redhat.com> - 6.5-8
- Fix gdb printf command argument using "%p" (BZ 205551).

* Mon Sep  4 2006 Alexandre Oliva <aoliva@redhat.com> - 6.5-7
- Fix bug in patch for CVE-2006-4146. (BZ 203873, BZ 203880)

* Thu Aug 24 2006 Alexandre Oliva <aoliva@redhat.com> - 6.5-6
- Avoid overflows and underflows in dwarf expression computation stack.
(BZ 203873)

* Thu Aug 24 2006 Alexandre Oliva <aoliva@redhat.com> - 6.5-5
- Backport support for i386 nop memory instructions.
- Fix debuginfo addresses resolving for --emit-relocs Linux kernels
(BZ 203661, from Jan Kratochvil, like the remaining changes).
- Bugfix segv on the source display by ^X 1 (fixes Patch130, BZ
200048).
- Do not step into the PPC solib trampolines (BZ 200533).
- Fix exec() from threaded program, partial CVS backport (BZ 182116).
- Fix occasional failure to load shared libraries (BZ 146810).
- Bugfix object names completion (fixes Patch116, BZ 193763).
- Avoid crash of 'info threads' if stale threads exist (BZ 195429).
- Handle corrupted or missing location list information (BZ 196439).

* Thu Jul 13 2006 Alexandre Oliva <aoliva@redhat.com> - 6.5-3
- Add missing definition of multilib_64_archs for glibc-devel buildreqs.
- Backport support for .gnu.hash sections.

* Wed Jul 12 2006 Alexandre Oliva <aoliva@redhat.com> - 6.5-2
- BuildReq sharutils, prelink and, on multilib systems, 32-bit glibc-devel.
- Drop obsolete attach-stop patch.
- Fix testcases in threaded-watchpoints2 and step-thread-exit patches.
- Re-enable attach-pie.exp, asm-source.exp and sigstep.exp tests.

* Tue Jul 11 2006 Alexandre Oliva <aoliva@redhat.com> - 6.5-1
- Upgrade to GDB 6.5.  Drop redundant patches, forward-port remaining
ones.  Re-enable ada and objc testsuites.

* Thu Jun 15 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.132
- Require flex and bison at build time.
- Additional patch for BZ 175083, to cope with waitpid setting status
even when returning zero.

* Wed May 31 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.131
- Require gettext at build time.  (BZ193366)

* Sat May 27 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.130
- Rewrite patch for BZ 175270, BZ 175083 so as to catch the exception
earlier.
- Remove too-fragile testcases from patches for CFA value and "S"
augmentation.

* Wed May 17 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.129
- Add not-automatically-generated file to fopen64 patch (BZ 191948).

* Fri Apr 14 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.128
- Avoid race conditions caused by exceptions messing with signal masks.
(BZ 175270, BZ 175083, maybe BZ 172938).
- Hardcode /bin and /usr/bin paths into gstack (BZ 179829, BZ 190548).
- Build in a subdir of the source tree instead of in a sibling directory.
- Switch to versioning scheme that uses the same base revision number
for all OSes, and uses a suffix to tell the builds apart and ensure
upgradability.

* Thu Apr 13 2006 Stepan Kasal <skasal@redhat.com>    - 6.3.0.0-1.127
- Bump up release number.

* Thu Apr 13 2006 Stepan Kasal <skasal@redhat.com>    - 6.3.0.0-1.123
- Use fopen64 where available.  Fixes BZ 178796, BZ 190547.
- Use bigger numbers than int.  Fixes BZ 171783, BZ 179096.

* Wed Mar  8 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.122
- Bump up release number.

* Wed Mar  8 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.119
- Fix regression in PIE debugging (BZ 133944) (re?)introduced by the
prelink fix (BZ 175075, BZ 190545).  Improve testcase for the prelink
fix.
- Revert dwarf2 frame identifier change.

* Tue Mar  7 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.118
- Bump up release number.

* Tue Mar  7 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.115
- Change dwarf2 frame identifiers to use the actual PC instead of the
function's entry point.
- Fix FSF and GDB contact addresses in new testcases.
- Do not try to compile x86_64-only CFA testcase on 32-bit x86.
- Change prelink test to issue untested instead of warning message if
system libraries are not prelinked.

* Fri Mar  3 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.114
- Bump up release number.

* Fri Mar  3 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.111
- Add support for "S" augmentation for signal stack frames.
- Add support for CFA value expressions and encodings.
- Various improvements to the prelink test.

* Thu Feb 23 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.110
- Bump up release number.

* Thu Feb 23 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.107
- Enable gdb to debug core files and executables with mismatched
prelink base addresses.  Fixes BZ 175075, BZ 190545.

* Tue Feb 14 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.106
- Bump up release number.

* Tue Feb 14 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.103
- Adjust type-punning patch to include fix not needed upstream.

* Tue Feb 14 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.102
- Bump up release number.

* Tue Feb 14 2006 Alexandre Oliva <aoliva@redhat.com> - 6.3.0.0-1.99
- Use type-punning warning fixes as accepted upstream.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6.3.0.0-1.98.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6.3.0.0-1.98.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 16 2006 Alexandre Oliva <aoliva@redhat.com>	6.3.0.0-1.98
- Bump up release number.

* Mon Dec 19 2005 Alexandre Oliva <aoliva@redhat.com>	6.3.0.0-1.94
- Fix type-punning warnings issued by GCC 4.1.

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Thu Dec 01 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.93
- Bump up release number.

* Thu Dec 01 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.90
- Add option to allow backtracing past zero pc value.
- Bugzilla 170275

* Tue Nov 15 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.89
- Bump up release number.

* Tue Nov 15 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.86
- Fix ia64 user-specified SIGILL handling error.
- Bugzilla 165038.

* Tue Oct 18 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.85
- Bump up release number.

* Tue Oct 18 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.82
- Modify attach patch to add missing fclose.
- Bugzilla 166712

* Tue Oct 11 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.81
- Bump up release number.

* Tue Oct 11 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.78
- Support gdb attaching to a stopped process.

* Thu Sep 29 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.77
- Bump up release number.

* Thu Sep 29 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.74
- Fix up DSO read logic when process is attached.

* Mon Sep 26 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.73
- Bump up release number.

* Mon Sep 26 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.70
- Fix frame pointer calculation for ia64 sigtramp frame.

* Thu Sep 22 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.69
- Bump up release number.

* Thu Sep 22 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.66
- Remove extraneous xfree.

* Wed Sep 07 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.65
- Bump up release number.

* Wed Sep 07 2005 Jeff Johnston	<jjohnstn@redhat.com>	6.3.0.0-1.62
- Readd readnever option

* Wed Jul 27 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.61
- Bump up release number.
                                                                                
* Tue Jul 26 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.57
- Bump up release number.
                                                                                
* Tue Jul 26 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.54
- Add testcase to verify printing of inherited members
- Bugzilla 146835
                                                                                
* Mon Jul 25 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.53
- Bump up release number.
                                                                                
* Mon Jul 25 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.50
- Fix bug with info frame and cursor address on ia64.
- Add testcase to verify pseudo-registers calculated for ia64 sigtramp.
- Bugzilla 160339
                                                                                
* Fri Jul 22 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.49
- Bump up release number.
                                                                                
* Fri Jul 22 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.46
- Fix attaching to 32-bit processes on 64-bit systems.
- Bugzilla 160254
                                                                                
* Thu Jul 14 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.45
- Bump up release number.
                                                                                
* Thu Jul 14 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.42
- Add work-around to make ia64 gcore work faster.
- Bugzilla 147436

* Thu Jul 14 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.41
- Bump up release number.

* Mon Jul 11 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.38
- Fix backtracing across sigaltstack for ia64
- Bugzilla 151741

* Fri Jul 08 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.37
- Bump up release number.

* Fri Jul 08 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.35
- Build pseudo-registers properly for sigtramp frame.
- Bugzilla 160339

* Fri Jul 08 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.34
- Bump up release number.

* Thu Jul 07 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.31
- Modify security errata to include additional bfd robustness updates
- Bugzilla 158680

* Fri Jun 10 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.30
- Bump up release number.

* Fri Jun 10 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.28
- Security errata for bfd and .gdbinit file usage
- Bugzilla 158680 

* Wed May 18 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.24
- Bump up release number.

* Wed May 18 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.23
- Bump up release number.

* Wed May 18 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.22
- Specify SA_RESTART for linux-nat.c handlers and use my_waitpid
  which handles EINTR.

* Tue May 03 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.21
- Bump up release number.

* Tue May 03 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.20
- Bump up release number.

* Tue May 03 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.19
- Fix for partial die in cache error
- Bugzilla 137904

* Wed Apr 27 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.18
- Bump up release number.

* Wed Apr 27 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.17
- Bump up release number.

* Wed Apr 27 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.16
- Update ia64 sigtramp support to use libunwind and fix top-level
  rse register reads to also use libunwind.
- Bugzilla 151741

* Thu Apr 21 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.15
- Bump up release number.

* Thu Apr 21 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.14
- Bump up release number.

* Thu Apr 21 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3-0.0-1.13
- Do not issue warning message for gcore under ia64
- Bugzilla 146416

* Mon Apr 11 2005 Andrew Cagney <cagney@redhat.com>   	6.3.0.0-1.12
- Update gstack patch, handle systems that lack /proc/<pid>/tasks.

* Fri Apr 8 2005 Andrew Cagney <cagney@redhat.com>   	6.3.0.0-1.11
- Replace patch warning about DW_OP_piece with a patch that implements
  the DW_OP_piece read path.

* Sat Apr 2 2005 Andrew Cagney <cagney@redhat.com>   	6.3.0.0-1.10
- Print a warning when the separate debug info's CRC doen't match;
  test.

* Wed Mar 30 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.9
- Bump up release number.

* Wed Mar 30 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-1.7
- Add proper vsyscall page support for ia64.

* Thu Mar 24 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-1.6
- Bump up release number.

* Thu Mar 24 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-1.4
- Fix printing of inherited members of C++ classes.
- Fix for Bugzilla 146835.

* Tue Mar 22 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-1.3
- Bump up release number.

* Thu Mar 17 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-1.1
- Remove warnings that cause errors when compiled with gcc4 and -Werror.

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar 04 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.37
- Bump up release number.

* Thu Mar 03 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.35
- Add follow-fork fix from mainline sources.

* Thu Mar 03 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.34
- Bump up release number.

* Mon Feb 28 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.32
- Modify debug register handling for x86, x86-64 to be thread-specific.
- Modify threaded watchpoint code for x86, x86-64 to properly insert
  and remove watchpoints on all threads.

* Tue Feb 22 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.31
- Bump version number.

* Tue Feb 22 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.30
- Bump version number.

* Tue Feb 22 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.29
- Modify gdb-6.3-dwattype0-20050201.patch to check for a zero address
  and not zero unsnd.  Fix BE 32- vs 64-bit problem.

* Mon Feb 21 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.28
- Back port patch adding symfile-mem.o to all GNU/Linux builds.
  Fix BZ 146087.

* Wed Feb 16 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-0.27
- Bump up release number.

* Wed Feb 16 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-0.26
- Fix unload.exp testcase.

* Mon Feb 14 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-0.25
- Bump up release number.

* Mon Feb 14 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-0.24
- Fix gdb to always grab the terminal before a readline call.
- Bugzilla 147880

* Fri Feb 11 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-0.23
- Bump up release number.

* Fri Feb 11 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-0.21
- Fix gdb to handle stepping over the end of an exiting thread.
- Bugzilla 146848

* Thu Feb 10 2005 Jeff Johnston <jjohnstn@redhat.com>   6.3.0.0-0.20
- Bump up release number.

* Tue Feb 08 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.18
- Modify previous gcore patch to not use linux_proc_xfer_memory even
  for main thread.

* Mon Feb 07 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.17
- Modify previous gcore patch to only apply to ia64.

* Fri Feb 04 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.16
- Fix gcore to work properly for threaded applications
- Bugzilla 145309, 145092

* Fri Feb 04 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.15
- Tolerate DW_AT_type referencing <0> and instead of generating an
  error, treat as unknown type.
- Bugzilla 144852.

* Thu Feb  3 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.14
- Separate out test patches.

* Thu Jan 27 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.13
- Fix to allow ia64 gdb to backtrace from syscalls in a corefile.
- Bugzilla 145092.

* Wed Jan 26 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.12
- Fix to support examining files even when the executable moves
- Bugzilla 142122

* Wed Jan 26 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.11
- gdb-6.3-ppcdotsyms-20050126.patch: Backport BFD changes for reading
  synthetic symbols.  Rewrite code reading elf minimal symbols so that
  it includes synthetics.

* Fri Jan 21 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.10
- Fix to prevent resetting unwind kernel table size to invalid value
  when debugging a core file
- Bugzilla 145309

* Fri Jan 21 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.9
- When single stepping handle both back-to-back and nested signals.
- Disable .symbol patch, results in BFD errors.

* Fri Jan 21 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.8
- Support listing both in-charge and not-in-charge dtors when
  just the dtor name is given.
- Add new test case for newly added ctor/dtor functionality.

* Thu Jan 20 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.7
- Fix to allow breaking by line in both the in-charge and
  not-in-charge ctor/dtor.
- Bugzilla 117826

* Thu Jan 20 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.6
- Rebuild.

* Thu Jan 20 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.5
- Use bfd_get_synthetic_symtab to read in any synthetic symbols
  such as 64-bit PPC's ".symbol"s.

* Tue Jan 18 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.4
- Modify non-threaded watchpoint patch to use new observer.

* Mon Jan 17 2005 Jeff Johnston <jjohnstn@redhat.com>	6.3.0.0-0.3
- Fix for non-threaded watchpoints.

* Mon Jan 17 2005 Andrew Cagney <cagney@redhat.com>	6.3.0.0-0.2
- Enable PPC CFI, remove merged ppc patches.

* Wed Jan 12 2005 Elena Zannoni <ezannoni@redhat.com>   6.3.0.0-0.1
                  Andrew Cagney <cagney@redhat.com>	
                  Jeff Johnston <jjohnstn@redhat.com>	
- Various fixes to complete the import and merge.

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
