"""This program finds all files inside a directory structure that ends in ".c"

  The program can be run passing in 2 command line parameters to specify the
  starting path and the suffix to look for.

  eg:
    $ python problem_2.py "/home/${USER}" ".py"

  By default it will run on the path "./testdir" and look for the suffix ".c"
"""

import os
import sys
# import tracemalloc

# sys.setrecursionlimit(10**6)  # use this if we run into stack overflow


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    filtered_files = []
    # sub_folders = []
    try:
        folder_contents = os.listdir(path)
    except FileNotFoundError:
        print(f'Invalid path - {path}')
        return []

    for f in folder_contents:
        full_path = os.path.join(path, f)
        # if it's a file and matches suffix, then save it
        if os.path.isfile(full_path) and full_path.endswith(suffix):
            filtered_files.append(full_path)
        # collect files from the sub folders recursively
        # memory usage upon recursively processing
        # current usage 3305, peak usage 19311
        if os.path.isdir(full_path):
            filtered_files.extend(find_files(suffix, full_path))
            # sub_folders.append(full_path)

    # memory usage upon collecting folders and processing
    # current usage 3793, peak usage 25564
    # for f in sub_folders:
    #     filtered_files.extend(find_files(suffix, f))

    # base condition will be when there are no more folders
    # and we return either filtered file or an empty list
    return filtered_files


if __name__ == '__main__':

    if len(sys.argv) == 3:
        path = sys.argv[1]
        suffix = sys.argv[2]

        for f in find_files(suffix, path):
            print(f)

        exit()

    # Default test case
    files = find_files('.c', './testdir')
    for f in files:
        print(f)
    print()
    # ./testdir/t1.c
    # ./testdir/subdir3/subsubdir1/b.c
    # ./testdir/subdir5/a.c
    # ./testdir/subdir1/a.c

    # Test when no file matches
    files = find_files('.py', './testdir')
    for f in files:
        print(f)
    if not files:
        print('no file match')
    print()
    # no file match

    # Test when invalid folder
    files = find_files('.py', './no_such_dir')
    for f in files:
        print(f)
    if not files:
        print('no file match')
    print()
    # Invalid path - ./no_such_dir
    # no file match

    # Test deep hierarchy
    files = find_files('.sh', '/bin')
    for f in files:
        print(f)
    if not files:
        print('no file match')
    print()
    # ...
    # <lots of data>
    # ...
