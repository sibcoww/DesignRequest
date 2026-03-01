from database import DatabaseManager
import sqlite3

# create test db
print('creating debug db')
db = DatabaseManager('debug.db')
# clear table
conn = sqlite3.connect('debug.db'); c = conn.cursor(); c.execute('DELETE FROM design_requests'); conn.commit(); conn.close()
# add two
print('adding first')
db.add_request('Клиент1','','Веб-дизайн','Desc1','2026-03-01')
print('adding second')
db.add_request('Клиент2','','Дизайн логотипа','Desc2','2026-03-01')
# show all
print('all', db.get_all_requests())
# update status second
res = db.update_status(2,'В работе')
print('update status result', res)
print('all after', db.get_all_requests())
print('filter new', db.filter_by_status('Новая'))
print('filter in progress', db.filter_by_status('В работе'))
