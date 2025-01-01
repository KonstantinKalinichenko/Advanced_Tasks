class UserManager:
   def __init__(self):
       self.users = {}

   def add_user(self, name, level): # добавляет нового пользователя с указанным уровнем доступа или уровнем доступа по умолчанию (1)
       self.users[name] = int(level)

   def remove_user(self, name): # удаляет пользователя
       self.users.pop(name)

   def promote(self, name): # увеличивает уровень доступа пользователя на 1
       self.users[name] += 1

   def demote(self, name): # уменьшает уровень доступа на 1, если уровень доступа больше 0 (иначе ничего не происходит)
       if self.users[name] > 0:
           self.users[name] -= 1

   def get_users(self): # вернет список всех пользователей с их текущим уровнем доступа
       if self.users:
           for k, v in self.users.items():
               print(f'{k}: {v}')
       else:
           print('Не найдено')


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

res = [item.strip().split() for item in input_string]

for command in res:
    if command[0] == 'add_user':
        if len(command) == 3:
            user_manager.add_user(command[1], command[2])
        else:
            user_manager.add_user(command[1], '1')
    elif command[0] == 'remove_user':
        user_manager.remove_user(command[1])
    elif command[0] == 'promote':
        user_manager.promote(command[1])
    elif command[0] == 'demote':
        user_manager.demote(command[1])
    else:
        user_manager.get_users()