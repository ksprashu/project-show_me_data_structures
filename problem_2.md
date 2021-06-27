# Finding Files
## Problem
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

```
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
```

Python's `os` module will be useful—in particular, you may want to use the following resources:

`os.path.isdir(path)`\
`os.path.isfile(path)`\
`os.listdir(directory)`\
`os.path.join(...)`

Note: `os.walk()` is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use `os.walk()`.
