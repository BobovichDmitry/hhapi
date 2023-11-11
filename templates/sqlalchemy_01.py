from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///ormnew2.sqlite', echo=False)

Base = declarative_base()


class position_skill(Base):
    __tablename__ = 'position_skill'
    id = Column(Integer, primary_key=True)
    position_id = Column(Integer, ForeignKey('position.id'))
    skill_id = Column(Integer, ForeignKey('skill.id'))
    def __init__(self, position_id, skill_id):
        self.skill_id = skill_id
        self.position_id = position_id

    def __str__(self):
        return f'{self.position_id}  {self.skill_id}'

class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Employer(Base):
    __tablename__ = 'employer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position_id = Column(Integer, ForeignKey('position.id'))
    tel_number = Column(Integer, nullable=True)

    def __init__(self, name, tel_number, position_id):
        self.name = name
        self.tel_number = tel_number
        self.position_id = position_id

    def __str__(self):
        return f' {self.name} telnumber: {self.tel_number}'


class Position(Base):
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


# Создание таблицы
Base.metadata.create_all(engine)

# Заполняем таблицы
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# Заполняем должности
session.add_all([Position('Секретарь'), Position('Продавец'), Position('Закупщик'), Position('Системный Администратор')])

# заполняем навыки
session.add_all([Skill('Варить кофе'), Skill('Отвечать на звонки'), Skill('Пользование ПК'), Skill('Продавать'), Skill('Закупать'), Skill('Знание иностранных языков'), Skill('Python')])

# Создаем сотрудников
session.add_all([Employer('Секретарь Олга Ивановна', 89262587489, 1), Employer('Администратор Василий Петрович', 891597956547, 4), Employer('Закупщик Покупан Суперский', 89178777777, 3), Employer('Продавец Продаван Суерский', 1111116547, 2)])

session.add_all([position_skill(3,3), position_skill(4,3),position_skill(4,7),position_skill(3,5),position_skill(2,2),position_skill(2,4),position_skill(1,3),position_skill(1,2),position_skill(1,1)])

session.commit()

# 1. Все сотрудники с должностью Секретарь
secretars = session.query(Employer).filter(Employer.position_id == '1').all()
for secretar in secretars:
    print(secretar)

# 2. Вывод необходимых навыков для всех должностей
skills = session.query(position_skill).all()
for scill in skills:
    print(scill)

# 2. вакансии в регионе москва
#employer = session.query(Employer).filter(Employer.position_id == position.id).all()

# print(len(vacancies))
# print(vacancies[0].region_id)
