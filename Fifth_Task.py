class UserManager:
   def __init__(self):
       self.users = {}

   def add_user(self, name, level):
       """Ваш код"""

   def remove_user(self, name):
       """Ваш код"""

   def promote(self, name):
       """Ваш код"""

   def demote(self, name):
       """Ваш код"""

   def get_users(self):
       """Ваш код"""

user_manager = UserManager()
input_string = []
while True:
   try:
      line = input()
      if line == "":
         break
   except EOFError:
      break
   input_string.append(line)

for command in input_string:
   """Ваш код"""