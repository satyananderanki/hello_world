
import json

with open("userdata.json") as data:
    userdata = json.load(data)

with open("roles.json") as ask:
    roles = json.load(ask)


class draup:
    def __init__(self, userdata):
        self.userdata = userdata

    def get_user_info(self, idno):
        x = idno
        y = 0
        for p in range(len(self.userdata)):
            if self.userdata[p]["id"] == x:
                y += 1
        if y == 1:
            for i in range(len(self.userdata)):
                if self.userdata[i]["id"] == x:
                    print(self.userdata[i].items())

        else:
            print("user doesnt exist")

    def user_count(self):
        print("The total number of users are {}".format(len(self.userdata)))

    def role_based_user_count(self, rolecount):
        self.rolecount = rolecount
        a = 0
        if rolecount in roles["role_priviledges"].keys():

            for i in range(len(self.userdata)):
                if userdata[i]["role"] == self.rolecount:
                    a += 1
            print("{} count= {}".format(self.rolecount, a))

        else:

            print("{} is a guest role".format(rolecount))

    def get_user_role(self):
        id = input("enter your id ")
        for z in range(len(self.userdata)):
            if id == self.userdata[z]["id"]:
                pq = self.userdata[z]["role"]
                print(pq)
        if "set_user_role" in roles["role_priviledges"][pq]["allowed"]:
            a = input("enter id")
            for z in range(len(self.userdata)):
                if a == self.userdata[z]["id"]:
                    print(self.userdata[z]["role"])
                else:
                    print("this is guest role")


class actiondraup:
    def __init__(self, userdata):
        self.userdata = userdata

    def add_user(self):

        id = int(raw_input("enter your id to verify"))
        for z in range(len(userdata)):

            if id == userdata[z]["id"]:
                df = userdata[z]["role"]

        if df == "subscriber" or df == "moderator":
            print("not aalowed to add user")
        elif df == "admin":

            self.userdata.append({"id": len(userdata) + 1, "name": None, "pass": None, "role": None, "desc": None})



    def edit_user(self,editor_role):
        self.editor_role = editor_role
        print(len(self.userdata))
        if self.editor_role == "admin" or self.editor_role == "moderator":
            print("you are allowed to edit")
            z = input("enter id to edit")
            for i in range(len(self.userdata)):
                if z == self.userdata[i]["id"]:
                    self.userdata[i]["name"] = raw_input("enter your name")
                    self.userdata[i]["pass"] = raw_input("enter pass")
                    self.userdata[i]["desc"] = raw_input("enter desc")

    def set_user_role(self):
        inpt = input("enter your id")
        for i in range(len(self.userdata)):
            if inpt == self.userdata[i]["id"]:
                rolechan = self.userdata[i]["role"]
                print("you are {}".format(self.userdata[i]["role"]))
        assign = raw_input("enter the role you wanted to get assigned")
        if rolechan == "subscriber" :
            print("you are not allowed to set the role")
        elif rolechan == "moderator" and assign == "admin":
            print ("you cannot be converted into {}".format(assign))
        elif rolechan == "moderator" and assign == "subscriber":
            chanid = int(input("enter your id"))
            for i in range(len(self.userdata)):
                if self.userdata[i]["id"] == chanid:
                    self.userdata[i]["role"] = assign
                    print(self.userdata[i])
        elif rolechan == "moderator" and assign == "moderator":
            chanid=int(input("enter your id"))
            for i in range(len(self.userdata)):
                if self.userdata[i]["id"] == chanid:
                    self.userdata[i]["role"] = assign
                    print(self.userdata[i])
        elif rolechan=="admin" and (assign == "moderator" or assign == "subscriber" or assign == "admin"):
            chanid = int(input("enter your id"))
            for i in range(len(self.userdata)):
                if self.userdata[i]["id"] == chanid:
                    self.userdata[i]["role"] = assign
                    print(self.userdata[i])

    def delete_user(self):
        id = int(input("enter your id"))
        for i in range(len(self.userdata)):
            if id == self.userdata[i]["id"]:
                rol = self.userdata[i]["role"]
                print("you are {}".format(userdata[i]["role"]))
        if rol == "admin":
            delid = int(raw_input("enter the id of the user you want to delete"))

            for i in range(len(self.userdata)-1):

                if delid == self.userdata[i]["id"]:
                    self.userdata.pop(i)

        else:
            print("you are not allowed to remove the user")













