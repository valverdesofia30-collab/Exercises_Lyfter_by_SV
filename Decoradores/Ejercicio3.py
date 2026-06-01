from datetime import date

class User: 
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        
    @property
    def age(self):
        today = date.today()
        
        age = today.year - self.date_of_birth.year
        
        if(today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day
        ):
            
            age -= 1
            
        return age
    
def validate_adult(func):
    def wrapper(user, *args, **kwargs):
        
        if user.age < 18:
            raise ValueError("User must be at least 18 years old")
    
        return func(user)    
        
    return wrapper 
    
@validate_adult
def create_bank_account(user):
    return f"Bank account created for {user.name}"

user = User(
    "Sofia",
    date(1999, 3, 7)
)

print(create_bank_account(user))