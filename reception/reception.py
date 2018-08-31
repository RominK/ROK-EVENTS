# Using with closes the file and
#  splitlines to ensure that my entries do not have '\n'
with open("vip_list.txt", "r") as f:
    vip_list = f.read().splitlines()
with open("ordinary_list.txt", "r") as f2:
    ordinary_list = f2.read().splitlines()

    # print(vip_list)

def registration_checker(name):
    registered = True
    registered_users = []
    if vip_list and ordinary_list:
        for vip in vip_list:
            if name.lower() in vip.lower():#using lower so that even if a user types name in any case it will still be found.
                registered_users.append(vip + " " + "VIP")
                # return vip + " " + "VIP"
            else:
                registered = False
        for ordinary in ordinary_list:
            if name.lower() in ordinary.lower():
                registered_users.append(ordinary + " " + "Ordinary")
                # return ordinary + " " + "Ordinary"
            else:
                registered=False
        return registered_users
    
    else:
        return "There are no registered_users in the system"
    return name + " " + "Not Registered"
        