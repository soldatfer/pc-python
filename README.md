# pc

### What?
Simple implementation of the Producer Consumer problem in Python.

### Learning

By default, the core dump upon a SIGQUIT interrupt of a Python program is not stored anywhere. To change this, in a terminal run:

```
ulimit -c unlimited
```

Later, core files are created upon such crashes happening in the same terminal. To debug this:

```
gdb python <name of core dump file>
```
