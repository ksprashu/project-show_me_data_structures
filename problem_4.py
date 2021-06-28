"""Program to lookup whether a user belongs to a group.
"""


class Group(object):
    parent_mapping = dict()  # class instance

    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    @staticmethod
    def add_parent_mapping(child, parent):
        """Add a lookup entry of child to parent.
        """

        if child in Group.parent_mapping:
            Group.parent_mapping[child].append(parent)
        else:
            Group.parent_mapping[child] = [parent]

    def is_child(self, child):
        """Returns true if the child belongs to this group.
        """

        return Group._is_child(self.get_name(), child)

    @staticmethod
    def _is_child(parent, child):
        """Recursively lookup the child entry to find the parent.
        """
        
        # print(f'looking for parent - {parent} of child - {child} in {Group.parent_mapping}')

        # base condition - no entry for child
        if child not in Group.parent_mapping:
            return False

        # base condition - parent found in lookup
        if parent in Group.parent_mapping[child]:
            return True

        # lookup present, but there is no immediate match.
        # recursively look for the user in all its parents
        for p in Group.parent_mapping[child]:
            if Group._is_child(parent, p):
                return True
        else:
            return False  # if it falls through the loop, then no match found

    def add_group(self, group):
        self.groups.append(group)

        # add to lookup
        Group.add_parent_mapping(group.get_name(), self.name)

    def add_user(self, user):
        self.users.append(user)

        # add to lookup
        Group.add_parent_mapping(user, self.name)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    return group.is_child(user)
    # parent_group = Group.parent_mapping.get(user, None)
    # while parent_group:
    #     if parent_group == group.get_name():
    #         return True
    #     parent_group = Group.parent_mapping.get(parent_group, None)

    # return False


if __name__ == '__main__':

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # child under the bottom most group
    print()
    print('sub_child_user in sub_child group? ',
          is_user_in_group(sub_child_user, sub_child))  # True
    print('sub_child_user in child group? ',
          is_user_in_group(sub_child_user, child))  # True
    print('sub_child_user in parent group? ',
          is_user_in_group(sub_child_user, parent))  # True

    child_user = "child_user"
    child.add_user(child_user)

    # child under the intermediate group
    print()
    print('child_user in sub_child group? ',
          is_user_in_group(child_user, sub_child))  # False
    print('child_user in child group? ',
          is_user_in_group(child_user, child))  # True
    print('child_user in parent group? ',
          is_user_in_group(child_user, parent))  # True

    forked_child = Group("forked_child")
    parent.add_group(forked_child)

    # child not under a forked group, but under overall parent
    print()
    print('child_user in child group? ',
          is_user_in_group(child_user, child))  # True
    print('child_user in forked_child group? ',
          is_user_in_group(child_user, forked_child))  # False
    print('child_user in parent group? ',
          is_user_in_group(child_user, parent))  # True

    forked_child.add_user(child_user)

    # child belong to 2 parallel groups but not in the bottommost
    print()
    print('child_user in sub_child group? ',
          is_user_in_group(child_user, sub_child))  # False
    print('child_user in child group? ',
          is_user_in_group(child_user, child))  # True
    print('child_user in forked_child group? ',
          is_user_in_group(child_user, forked_child))  # True
    print('child_user in parent group? ',
          is_user_in_group(child_user, parent))  # True
