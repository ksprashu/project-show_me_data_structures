# Finding Files
## Explanation
### Consideration
This requirement can be solved by recursion, but there is a consideration that `There are no limit to the depth of the subdirectories can be.`. This could mean that going into a recursive process will trigger a stack exceeded exception.

The default stack size is `10**3`, and while this is quite large, we could increase it to `10**6` using the function `sys.setrecursionlimit()` if we start running out of stack space.

### Solution

Using a list and adding the filtered files into the same list we are able to implement a recursive solution to go through every sub directory recursively and find files that matches the suffix filter.

The base condition is that the leaf folders will not have any more folders and will either return no file (`[]`) or the files that matches the suffix filter. This will be a list which will be added to the already existing list (`extend()`) before finally being returned back at the top of the stack.

### Time Complexity
In order to find all the files that match the suffix, the program will have to
scan through every directory and file in the folder hierarchy. Let's assume that the 
total number of directories is `d` and total number of files is `f`.

The program makes `O(d)` operations on the OS when it calls `os.listdir()` to get
the files in the folder. For each folder + file, we check whether it is a file or folder, and for the folder, we perform a suffix check. This is `O(f+d) + O(f)`
operations. Total time complexity = `O(f+d) + O(f) + O(d)` which approxmiates to 
`O(2.(f+d))`.

Assume total number of records in the file system is `n`, then the __overall time
complexity is of the order `O(n)`__.

### Space Complexity
Each time the problem reurses into a folder, it has to save the contents of the
stack to memory. We are using `O(1)` space to record each file / folder. 

In each iteration, the problem will save the names of the files that match the
filter, and discard the rest of the data. At any instant the total data that 
could be stored in the stack will be the list of all the folders that need to be
parsed. While the actual storage at the end of the program will be the filtered
files.

Each file path could occupy (say) 255 characters, or 255 bytes. Let's assume the
total number of filtered files is `f'` where `f' < f`.

Hence max space that could be used transiently is `O(n)`, and the space that
will finally be occupied at the end of the program is __of the order `O(f')`__.
