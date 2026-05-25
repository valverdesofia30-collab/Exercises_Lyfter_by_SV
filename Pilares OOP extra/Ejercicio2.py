from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    
    def __init__(self, name):
        self.name = name
    
    def get_role(self):
        return "AdminUser"
    
    def has_permission(self, permission):
            return True
    
class RegularUser(User):
    
    def __init__(self, name):
        self.name = name
        
    def get_role(self):
        return "RegularUser"
    
    def has_permission(self, permission):
        if permission in ["read"]:
            return True
        return False
    
user1 = AdminUser("Daniel")
user2 = RegularUser("Sofia")

print(user1.get_role())
print(user1.has_permission("delete"))
print(user1.has_permission("write"))
print(user1.has_permission("read"))

print(user2.get_role())
print(user2.has_permission("read"))
