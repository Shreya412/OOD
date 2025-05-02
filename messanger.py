class Message:
    def __init__(self, sender, text, group=None):
        self.sender = sender
        self.text = text
        self.group = group

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = []
    def receive_msg(self, msg):
        self.inbox.append(msg)
    def show_msg(self):
        for i in self.inbox:
            print("Messages are:", i.text)

class Group:
    def __init__(self, name, admin):
        self.name = name
        self.members = [admin]

    def add_member(self, user):
        if user not in self.members:
            self.members.append(user)

    def remove_member(self, user):
        if user in self.members:
            self.members.remove(user)
        
        
class Messanger():
    def __init__(self):
        self.users = []
        self.groups = []
    def login(self, user):
        print("User added", user)
        self.users.append(user)
    def send_msg(self, sender, receiver, text):
        if sender not in self.users or receiver not in self.users:
            print("Sender or receiver not found in users")
            return
        message = Message(sender, receiver, text)
        receiver.receive_msg(message)
        print("Message sent", receiver.name, "from", sender.name)
    def add_grp(self, name, admin):
        if admin not in self.users:
            print("User not added")
            return None
        group = Group(name, admin)
        self.groups.append(group)
        print("Group",name," created by ",admin.name)
        return group
    def send_msg_grp(self, sender, group, text):
        if group not in self.groups or sender not in group.members:
            print("no group or sender.")
            return
        message = Message(sender, text, group=group.name)
        for i in group.members:
            if i != sender:
                i.receive_msg(message)
        print("msg sent to group", group.name )


    
app = Messanger()
user1 = User("Shreya")
user2 = User("Shivam")
app.login(user1)
app.login(user2)
app.send_msg(user1, user2, "Hi")
app.send_msg(user1, user2, "How r u")
app.send_msg(user2, user1, "Hello fine")

user2.show_msg()
user1.show_msg()
