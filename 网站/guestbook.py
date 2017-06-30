# coding:utf-8
import shelve
DATA_FILE = 'guestbook.dat'
def save_data(name,comment,create_at):
     database = shelve.open(DATA_FILE)
     if 'greeting_list' not in database:
         greeting_list = []
     else:
         greeting_list = database['greeting_list']
     greeting_list.insert(0,{
         'name':name,
         'comment':comment,
         'create_at':create_at
     })
     database['greeting_list'] = greeting_list
     database.close()












