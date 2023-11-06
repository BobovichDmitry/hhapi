import requests
import pprint
import re
# import random
from collections import Counter

def hhapi(vacancy):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': f'NAME:{vacancy}',
        "area": '1',
        # есть страницы т.к. данных много
        'per_page': 100,
        'page': 1,
    }
    result = requests.get(url, params=params).json()

    # params2 = {
    #    'text': 'NAME:Python',
    #    "area": '1',
    #    # есть страницы т.к. данных много
    #    'per_page': 80,
    #    'page': 1,
    # }
    # result2 = requests.get(url, params=params2).json()
    # result3 = result + result2
    # pprint.pprint(result2)

    # result = []
    # response1 = []
    # response2 = []

    # for page_num in range(0, 7):
    response1 = requests.get(url, params={'text': 'NAME:Python developer', "area": '1',
                                          # есть страницы т.к. данных много
                                          'per_page': 100,
                                          'page': 1}).json()
    # print(response)
    # result = response)
    # print(response)
    response2 = requests.get(url, params={'text': 'NAME:Python developer',
                                          "area": '1',
                                          # есть страницы т.к. данных много
                                          'per_page': 100,
                                          'page': 21}).json()
    # print(response)
    # result = response)
    # print(response)

    # result = response1 + response2
    # pprint.pprint(result)

    reqpython = 0
    reqdkango = 0
    reqflask = 0
    reqsql = 0
    salaryitogo = 0
    salarypeople = 0
    numberwithsalary = 0
    allvacancies = int(result['found'])

    # print(russian)

    # text2 = str(result['items'][1]['snippet']['requirement'])
    # words = text.split() + text2.split()
    # print(words)
    words = []

    n = 80  # не знаю как пройтись по всем вакансиям пока
    for i in range(n):
        text = str(result['items'][i]['snippet']['requirement'])
        text = re.sub('[,.)!@#$]', '', text)
        text = text.upper()
        # print(filter(lambda ch: ch not in " ?.!/;:", text))#
        words = words + text.split()
        if 'Python' in str(result['items'][i]['snippet']['requirement']):
            reqpython += 1
        if 'Jango' in str(result['items'][i]['snippet']):
            reqdkango += 1
        if 'Flask' in str(result['items'][i]['snippet']):
            reqflask += 1
        if 'SQL' in str(result['items'][i]['snippet']):
            reqsql += 1
        if result['items'][i]['salary'] != None:
            if (result['items'][i]['salary']['from']) != None and (result['items'][i]['salary']['to']) != None:
                salarypeople = ((result['items'][i]['salary']['from']) + (result['items'][i]['salary']['to'])) / 2
                #print(f'Средняя зп {salarypeople}')
                numberwithsalary += 1
                # print(result['items'][i]['salary']['from'])
                # print(result['items'][i]['salary']['to'])
            if (result['items'][i]['salary']['from']) == None and (result['items'][i]['salary']['to']) != None:
                salarypeople = (result['items'][i]['salary']['to'])
                #print(f'Верхняя планка {salarypeople}')
                numberwithsalary += 1
            if (result['items'][i]['salary']['from']) != None and (result['items'][i]['salary']['to']) == None:
                salarypeople = (result['items'][i]['salary']['from'])
                #print(f'Нижняя планка {salarypeople}')
                numberwithsalary += 1
            salaryitogo = salaryitogo + salarypeople
        # salaryitogo += result['items'][i]['salary']
        # salarypeople = 0
        # if (result['items'][i]['salary']['from']) != None and (result['items'][i]['salary']['to']) != None:
        # salarypeople = ((result['items'][i]['salary']['from']) + (result['items'][i]['salary']['to'])) / 2
        # print(result['items'][i]['salary']['from'])
        #print(result['items'][i]['snippet']['requirement'])
        #print(result['items'][i]['alternate_url'])
    # print(f'Всего {}вакансий')

    # print(numberwithsalary)
    # print(salaryitogo)
    averagesallaery =  round((salaryitogo / numberwithsalary))
    ##print(words)
    r = re.compile("[a-zA-Z]+")
    skill = [w for w in filter(r.match, words)]
    # c = Counter(skill)
    # print(sorted.skill)

    skill.sort(key=str.lower)
    #print(skill)
    # print(skill)
    skillitog = []
    for i in skill:
        if not skillitog or skillitog[-1][0] != i:
            skillitog.append([i, 1])  # a new element - append and start the count at 1
        else:
            skillitog[-1][1] += 1  # a duplicate - increment the count

    counts = ['{}*{}'.format(*l) for l in skillitog]
    skilltop10 = []
    # print(counts)
    #print(skillitog)
    for i in range(len(skillitog)):
        if skillitog[i][1] >= 5:
            skilltop10 = skilltop10 + skillitog[i]
    #print(skilltop10)

    allvacancies = int(result['found'])
    with open('output.txt', 'w', encoding="UTF-8") as f:
        f.write(f'Вакансия: {vacancy}\n')
        f.write(f'Всего вакансий: {allvacancies}\n')
        f.write(f'Средняя ЗП по вакансии: {averagesallaery}\n')
        for i in range(0, (len(skilltop10) - 1), 2):
            # print(skilltop10[0])
            percentskill = 100 * (skilltop10[i + 1] / n)
            f.write(f'{skilltop10[i]} - {percentskill}%\n')
    f.close()
    #print('____' * 20)
    #print(f'Всего вакансий {allvacancies}')
    #print(f'Средняя ЗП по вакансии {averagesallaery}')
    #print("Требования:")
    # pythonpercent = (100 * reqpython) / n

    #for i in range(0, (len(skilltop10) - 1), 2):
        # print(skilltop10[0])
     #   percentskill = 100 * (skilltop10[i + 1] / n)
     #   print(f'{skilltop10[i]} - {percentskill}%')

#hhapi("Python")