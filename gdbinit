# System-wide GDB initialization file.
python
import glob
for f in glob.iglob('%{_sysconfdir}/gdbinit.d/*.gdb'):
  gdb.execute('source %s' % f)
for f in glob.iglob('%{_sysconfdir}/gdbinit.d/*.py'):
  gdb.execute('source %s' % f)
end
