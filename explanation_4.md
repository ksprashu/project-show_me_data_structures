# Active Directory
## Explanation
On one hand, this problem could be solved by a recursive strategy where we go 
down from the provided group checking to see if the user is present in the 
group or any of it's sub groups. 

However this might not be efficient in lookup time as lookup time will be 
`O(n)` where `n` is the number of groups, 
since we haveto go through all the nodes to find the group. 

_Is there a way to build a directed graph to check for the groups that the user
belongs to rather than the other way around?_

### Assumptions
1. The name of the group and the user is unique. This is the ID of the group
and the uniqueness will be maintained. We will use the name rather than the 
group object to identify the group.
2. A user / group may belong to more than one group. Eg: a user may belong to
_administrators_ group as well as _users_ group.

In order to solve for this, whenever a user/group is added to another group,
we will create a lookup table. We can follow this lookup table until there are
no entries, which mean there are no more parents. 

Since each node could belong to multiple nodes (parents), we cannot represent 
this as a tree structure. However in the lookup, each entry will be mapped to a
list of parents.

If we don't find the matching group while traversing through this, then it
means that the user doesn't belong to that group. 

### Implementation
In order to keep the implementation cohesive / colocated with the Active Directory
class, we will implement the lookup and associated functions on the Active Directory
`Group` class itself. Since this lookup will be common to all the groups / users
we will have it as static attributes and methods on the class.

### Complexity
This solution prioritizes Time complexity over Space complexity. 

#### Time Complexity
The lookup contains all the relations that are created. Each relationship takes us
up the hierarchy to the next higher relationship. Assuming the relationship hierarchy
takes the shape of a tree, and assuming a uniform distribution of nodes and 
relationships in the tree, the worst case is to walk up the height of the tree from
the leaf node to the root. Since there are `log(n)` nodes in the path to the height, 
the worst case time complexity for each lookup is `O(log(n))`.
#### Space Complexity
Every group or user is stored as a single object. In addition, every relationship
is stored as another entry within the group. Every relationship is also stored
in the lookup table for faster access. 

The groups and users are akin to nodes on a tree and the relationships are the edges
of the tree. If `n` represents the number of users + groups in the directory, then
there are about `2n` edges for the tree on average. This is stored twice. Hence total
space used is `5n`. 

The space complexity is of the order of `O(n)`.
