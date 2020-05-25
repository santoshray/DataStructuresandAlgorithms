
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

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
    if group == None or user == None :
        return False
    if user in group.get_users():
        return True 
    else:
        for g in group.get_groups():
            return is_user_in_group(user,g)

    return False

if __name__ == '__main__':


    print("\n---Test Case 1")

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)


    child.add_group(sub_child)
    parent.add_group(child)

    print("user name:{} in group name:{} ? {}".format(sub_child_user,None,is_user_in_group("sub_child_user",None)))
    print("user name:{} in group name:{} ? {}".format(sub_child_user,"parent",is_user_in_group("sub_child_user",parent)))
    print("user name:{} in group name:{} ? {}".format(sub_child_user,"child",is_user_in_group("sub_child_user",child)))
    print("user name:{} in group name:{} ? {}".format(sub_child_user,"sub_child_user",is_user_in_group("sub_child_user",sub_child)))


    print("\n---Test Case 2---")

    group_audio_str = "audio"
    g_audio = Group(group_audio_str)

    u1 = "Santosh"
    u2 = "Manoj"
    u3 = "David"
    u4 = "Ajit"
    u5 = "Matt"
    u6 = "Mark"
    u7 = "Avinash"
    u8 = "Mario"
    group_multimedia_str = "multimedia"
    g_multimedia = Group(group_multimedia_str)
    #make audio a sub group of  multimedia Group  

    group_display_str = "display"
    g_display = Group(group_display_str)

    g_multimedia.add_group(g_audio)
    g_multimedia.add_group(g_display)


    g_audio.add_user(u1)
    g_audio.add_user(u2)
    g_audio.add_user(u3)

    g_display.add_user(u3)
    g_display.add_user(u2)
    g_display.add_user(u5)

    g_multimedia.add_user(u6)
    g_multimedia.add_user(u7)

    print("user name:{} in group name:{} ? {}".format(None,group_multimedia_str,is_user_in_group(None,g_multimedia)))
    print("user name:{} in group name:{} ? {}".format(u1,group_multimedia_str,is_user_in_group(u1,g_multimedia)))
    print("user name:{} in group name:{} ? {}".format(u2,group_display_str,is_user_in_group(u2,g_display)))
    print("user name:{} in group name:{} ? {}".format(u3,group_audio_str,is_user_in_group(u3,g_audio)))
    print("user name:{} in group name:{} ? {}".format(u3,group_multimedia_str,is_user_in_group(u3,g_multimedia)))
    print("user name:{} in group name:{} ? {}".format(u5,group_audio_str,is_user_in_group(u5,g_audio)))
    print("user name:{} in group name:{} ? {}".format(u6,group_audio_str,is_user_in_group(u6,g_audio)))
    print("user name:{} in group name:{} ? {}".format(u6,group_display_str,is_user_in_group(u6,g_display)))
    print("user name:{} in group name:{} ? {}".format(u6,group_multimedia_str,is_user_in_group(u6,g_multimedia)))
    print("user name:{} in group name:{} ? {}".format(u8,group_multimedia_str,is_user_in_group(u8,g_multimedia)))

    print("\n---Test Case 3---")

    g_business_development_str = "Business Developement"
    g_business_execution_str = "Business Execution"

    u1 = "Santosh"
    u2 = "Manoj"
    u3 = "David"
    u4 = "Ajit"
    u5 = "Matt"
    u6 = "Mark"
    u7 = "Avinash"
    u8 = "Mario"

    g_business_execution = Group(g_business_execution_str)
    g_business_development =Group(g_business_development_str)

    g_business_execution.add_user(u1)
    g_business_execution.add_user(u2)
    g_business_execution.add_user(u3)
    g_business_execution.add_user(u4)
    g_business_execution.add_user(u5)
    print("user name:{} in group name:{} ? {}".format(None,None,is_user_in_group(None,None)))

    print("user name:{} in group name:{} ? {}".format(u1,g_business_execution_str,is_user_in_group(u1,g_business_execution)))
    print("user name:{} in group name:{} ? {}".format(u2,g_business_execution_str,is_user_in_group(u2,g_business_execution)))
    print("user name:{} in group name:{} ? {}".format(u3,g_business_execution_str,is_user_in_group(u3,g_business_execution)))
    print("user name:{} in group name:{} ? {}".format(u6,g_business_execution_str,is_user_in_group(u6,g_business_execution)))
    print("user name:{} in group name:{} ? {}".format(u4,g_business_development_str,is_user_in_group(u4,g_business_development)))


