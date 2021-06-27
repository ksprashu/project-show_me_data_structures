# Finding Files
## Explanation
### Consideration
This requirement can be solved by recursion, but there is a consideration that `There are no limit to the depth of the subdirectories can be.`. This could mean that going into a recursive process will trigger a stack exceeded exception.

The default stack size is `10**3`, and while this is quite large, we could increase it to `10**6` using the function `sys.setrecursionlimit()` if we start running out of stack space.

### Solution

Using a list and adding the filtered files into the same list we are able to implement a recursive solution to go through every sub directory recursively and find files that matches the suffix filter.

The base condition is that the leaf folders will not have any more folders and will either return no file (`[]`) or the files that matches the suffix filter. This will be a list which will be added to the already existing list (`extend()`) before finally being returned back at the top of the stack.

### Complexity

The program will recurse up to the depth of the tree structure. Each time, the stack of the parent is saved while it goes down the recursion. However the data that is stored is only as much as the number of files that are already filtered at the parent level and the number of sub folders at the current level. 

Hence this is directly proportional to the number of folders and files in the file system and it has to go through all the files + folders just once. 

Hence\
Time Complexity = `O(n)`\
Space Complexity = `O(n)` 
