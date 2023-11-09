
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('hh.sqlite')

# Создаем курсор
cursor = conn.cursor()

cursor.execute('SELECT * from employer')

result = cursor.fetchall()
print(result)

for item in result:
    print(item)
    print(type(item))
print('******' * 10)
cursor.execute('SELECT * from skills where skill=?', ('Продажи',))

print(cursor.fetchall())

cursor.execute('INSERT INTO skills (skill) VALUES ("Продажи222")')
cursor.execute('INSERT INTO skills (skill) VALUES ("Продажи2222")')
cursor.execute('SELECT * from skills')
print(cursor.fetchall())

query = 'select e.name, p.name from employer e, position p where e.position = p.id'
cursor.execute(query)

print(cursor.fetchall())

query = 'select e.name as ФИО, p.name as Должность , s.skill as Навыки from skills s, key_pos_skills kp, employer e, position p where e.position = p.id and kp.position_id=p.id and kp.skills_id = s.id'

cursor.execute(query)

print(cursor.fetchall())