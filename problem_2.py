"""This program finds all files inside a directory structure that ends in ".c"
"""

import os

# import sys
# sys.setrecursionlimit(10**6)  # use this if we run into stack overflow
# import tracemalloc


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
    folder_contents = os.listdir(path)
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


# tracemalloc.start()

for f in find_files('.c', './testdir'):
    print(f)

# print('current usage {}, peak usage {}'.format(
#     *tracemalloc.get_traced_memory()))
# tracemalloc.stop()
