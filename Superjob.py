import time
import selenium
from selenium import webdriver
from openpyxl import load_workbook
import random
import xlrd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

################### Xpath Для специализации ################################

xpath_rubriks = {
    'IT, Интернет, связь, телеком': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/div/button',
    'Административная работа, секретариат, АХО': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/div/button',

    'Банки, инвестиции, лизинг': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[3]/div/div/button',
    'Безопасность, службы охраны': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[4]/div/div/button',
    'Бухгалтерия, финансы, аудит': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[5]/div/div/button',

    'Дизайн': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[6]/div/div/button',
    'Домашний персонал': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[7]/div/div/button',
    'Закупки, снабжение': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[8]/div/div/button',
    'Искусство, культура, развлечения': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[9]/div/div/button',
    'Кадры, управление персоналом': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[10]/div/div/button',
    'Консалтинг, стратегическое развитие': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[11]/div/div/button',
    'Маркетинг, реклама, PR': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[12]/div/div/button',
    'Медицина, фармацевтика, ветеринария': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[13]/div/div/button',

    'Наука, образование, повышение квалификации': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[14]/div/div/button',
    'Некоммерческие организации, волонтерство': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[15]/div/div/button',
    'Продажи': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[16]/div/div/button',

    'Промышленность, производство': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[17]/div/div/button',
    'Рабочий персонал': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[18]/div/div/button',

    'СМИ, издательства': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[19]/div/div/button',
    'Сельское хозяйство': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[20]/div/div/button',

    'Спорт, фитнес, салоны красоты, SPA': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[21]/div/div/button',
    'Страхование': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[22]/div/div/button',

    'Строительство, проектирование, недвижимость': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[23]/div/div/button',
    'Сырье': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[24]/div/div/button',

    'Топ-персонал': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[25]/div/div/button',
    'Транспорт, логистика, ВЭД': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[26]/div/div/button',
    'Туризм, гостиницы, общественное питание': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[27]/div/div/button',
    'Услуги, ремонт, сервисное обслуживание': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[28]/div/div/button',
    'Юриспруденция': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/ul/li[29]/div/div/button',
}

################### Xpath Для подрубрик ################################

# IT / Интернет / Телеком
xpath_it_ithernet = {

    'CRM-системы': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[1]/div/div/label/div/div[1]/input',
    'Web, UI, UX дизайн': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[2]/div/div/label/div/div[1]/input',
    'Web-верстка': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[3]/div/div/label/div/div[1]/input',
    'Администрирование баз данных': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[4]/div/div/label/div/div[1]/input',
    #
    'Аналитика': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[5]/div/div/label/div/div[1]/input',
    'Внедрение и сопровождение ПО': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[6]/div/div/label/div/div[1]/input',
    'Защита информации': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[7]/div/div/label/div/div[1]/input',
    'Игровое ПО / Геймдевелопмент': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[8]/div/div/label/div/div[1]/input',
    #
    'Инжиниринг': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[9]/div/div/label/div/div[1]/input',
    'Интернет, создание и поддержка сайтов': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[10]/div/div/label/div/div[1]/input',
    'Киберспорт': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[11]/div/div/label/div/div[1]/input',
    #
    'Компьютерная анимация и мультимедиа': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[12]/div/div/label/div/div[1]/input',
    'Контент': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[13]/div/div/label/div/div[1]/input',
    #
    'Мобильная разработка': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[14]/div/div/label/div/div[1]/input',
    'Оптимизация, SEO': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[15]/div/div/label/div/div[1]/input',
    'Передача данных и доступ в интернет': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[16]/div/div/label/div/div[1]/input',
    'Разработка и сопровождение банковского ПО': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[17]/div/div/label/div/div[1]/input',
    'Разработка, программирование': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[18]/div/div/label/div/div[1]/input',
    #
    'Сетевые технологии': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[19]/div/div/label/div/div[1]/input',
    'Системная интеграция': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[20]/div/div/label/div/div[1]/input',
    'Системное администрирование': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[21]/div/div/label/div/div[1]/input',
    #
    'Системы автоматизированного проектирования (САПР)': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[22]/div/div/label/div/div[1]/input',
    'Системы управления предприятием (ERP)': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[23]/div/div/label/div/div[1]/input',
    'Сотовые, беспроводные технологии': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[24]/div/div/label/div/div[1]/input',
    #
    'Телекоммуникации и связь': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[25]/div/div/label/div/div[1]/input',
    'Тестирование, QA': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[26]/div/div/label/div/div[1]/input',
    'Техническая документация': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[27]/div/div/label/div/div[1]/input',
    'Техническая поддержка': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[28]/div/div/label/div/div[1]/input',
    #
    'Управление продуктом': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[29]/div/div/label/div/div[1]/input',
    'Управление проектами': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[30]/div/div/label/div/div[1]/input',
    #
    'Электронная коммерция': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[31]/div/div/label/div/div[1]/input',
    'Электронный документооборот': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[32]/div/div/label/div/div[1]/input',
    'Юзабилити': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[33]/div/div/label/div/div[1]/input',
    'Другое': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[34]/div/div/label/div/div[1]/input',
    'Начало карьеры, мало опыта': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[35]/div/div/label/div/div[1]/input',
}

# IT / Интернет / Телеком
xpath_it_ithernet = {

    'Архивное дело': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[1]/div/div/label/div/div[1]/input',
    'АХО': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[2]/div/div/label/div/div[1]/input',
    'Делопроизводство, ввод данных, систематизация': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[3]/div/div/label/div/div[1]/input',
    'Диспетчерская служба': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[4]/div/div/label/div/div[1]/input',
    #
    'Курьерская служба': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[5]/div/div/label/div/div[1]/input',
    'Переводы': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[6]/div/div/label/div/div[1]/input',
    'Секретариат, ресепшн, офис-менеджмент': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[7]/div/div/label/div/div[1]/input',
    'Другое': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[8]/div/div/label/div/div[1]/input',
    'Начало карьеры, мало опыта': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[9]/div/div/label/div/div[1]/input',
}


################### считываем данные с excel ################################

wb = xlrd.open_workbook('./DATA.xlsx')
sheet_xlr = wb.sheet_by_name('Вакансии')
a = 2
rows_sheet = sheet_xlr.nrows
# print(rows_sheet)


wb = load_workbook('./DATA.xlsx')
lst = (wb.sheetnames)

sheet = wb[lst[0]]
sheet.title
error_string = 1056

# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.

error_string = 1060
i = random.randint(3, rows_sheet)
################### заводим содержимое в переменные ################################
# print(a)
vacancy = (sheet.cell(row=i, column=1).value)
zp_ot = (sheet.cell(row=i, column=2).value)
zp_do = (sheet.cell(row=i, column=3).value)
opyt = (sheet.cell(row=i, column=4).value)
opisanie = (sheet.cell(row=i, column=5).value)
grafik = (sheet.cell(row=i, column=6).value)
company = (sheet.cell(row=i, column=7).value)
opis_company = (sheet.cell(row=i, column=8).value)
company1 = (sheet.cell(row=i, column=9).value)
opis_company1 = (sheet.cell(row=i, column=10).value)
company2 = (sheet.cell(row=i, column=11).value)
opis_company2 = (sheet.cell(row=i, column=12).value)
company3 = (sheet.cell(row=i, column=13).value)
opis_company3 = (sheet.cell(row=i, column=14).value)
company4 = (sheet.cell(row=i, column=15).value)
opis_company4 = (sheet.cell(row=i, column=16).value)
nazvanie = (sheet.cell(row=i, column=17).value)
auto = (sheet.cell(row=i, column=18).value)
# print(vacancy)
error_string = 1099
###############    autorith  ###############

sheet = wb[lst[2]]
sheet.title
login = (sheet.cell(row=1, column=2).value)
password = (sheet.cell(row=2, column=2).value)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
driver = browser

browser.get('https://nn.superjob.ru/hr/vacancy/create/')

############### Login ########################

browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/form/div/div[3]/div/div/div/div/div[1]/label/div/div/input').send_keys(login)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/form/div/div[3]/div/div/div/div/div[2]/label/div/div[1]/input').send_keys(password)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/form/div/div[4]/div/div[1]/button').click()

############### Должность ####################
time.sleep(4)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/label/div/div/input').send_keys(vacancy)

############## Специализация #################

browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/button/span/span/span').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/button').click()



############## Город #########################
p = 1
while p <= 7:
    try:
        browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/ul/li['+str(p)+']/span/span[2]/button').click()
    except:
        print("Больше нет автоматически подставленых городов")
    p+=1
gorod = "Тула"
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[4]/div/div[1]/div/div/div[3]/div/div[1]/label/div/div/input').send_keys(gorod)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[4]/div/div[1]/div/div/div[3]/div/div[1]/label/div/div/input').send_keys(Keys.ARROW_DOWN + Keys.ENTER)

############## Адрес ########################

adres = "ул. Ленина"
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[4]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/label/div/div/input').send_keys(gorod + ' ' + adres)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[4]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/label/div/div/input').send_keys(Keys.ARROW_DOWN + Keys.ENTER)

############# Метро ########################



############# Занятость #################### НУЖНО СДЕЛАТЬ

browser.find_element_by_xpath('//*[@id="detailInfo.workType.id-input"]').click()
browser.find_element_by_xpath('//*[@id="detailInfo.workType.id-input"]').send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)

############# Уровень дохода ###############

browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[6]/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/label/div/div[2]/input').send_keys(zp_ot)
browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[6]/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[2]/label/div/div[2]/input').send_keys(zp_do)

############ Опыт работы ###################
try:
    if opyt == 'не имеет значения':
        browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[8]/div/div[2]/button[1]').click()
    elif opyt == '1 год':
        browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[8]/div/div[2]/button[3]').click()
    elif opyt == '3 года':
        browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[8]/div/div[2]/button[4]').click()
    elif opyt == '6 лет':
        browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[8]/div/div[2]/button[5]').click()
    elif opyt == 'без опыта':
        browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[8]/div/div[2]/button[2]').click()
except:
    print('Выбраный опыт работы уже стоит')

############ Описание вакансии #############

yslovia = opisanie.partition('Условия:')
# print(x[1])
obiaznosti = yslovia[2].partition('Обязанности:')

lst_obiaznosti = list(obiaznosti)
lstobi = lst_obiaznosti[0].split('\n', 1)
del lstobi[0]

trebovania = obiaznosti[2].partition('Требования:')
lst_trebovania = list(trebovania)
lst_treb = lst_trebovania[2].split('\n', 1)
# print(obiaznosti[0], trebovania[0], trebovania[2])
print(lst_trebovania)
treb0 = lst_trebovania[0].split('\n', 1)
# del treb0[0]

#iframe = browser.find_elements_by_xpath('//*[@id="description_ifr"]')[0]
#driver.switch_to.default_content()
#driver.switch_to.frame(iframe)

div = browser.find_elements_by_tag_name('p')[0]
print("YSLOVIE!!!!!!!!!!!!!\n", yslovia, "\n", yslovia[0])
div.send_keys(Keys.ARROW_UP + Keys.ENTER)
div1 = browser.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[9]/div/div/div[2]/div/div[1]/div/div/div/div[2]')[0]
div1.send_keys(" " + (Keys.LEFT_CONTROL + "b"))
div1.send_keys(yslovia[0])
browser.find_elements_by_tag_name('strong')[0].send_keys(Keys.ENTER)
ysl = browser.find_elements_by_tag_name('ul')[0]
print(lst_obiaznosti)
print(lst_obiaznosti[0])
print(lstobi)
ysl.send_keys(treb0)  # То что после ОБЯЗАННОСТИ
ysl.send_keys(Keys.BACKSPACE)
trb = browser.find_elements_by_tag_name('ul')[1]

tr = lst_treb[1].split("\n \n", 1)
tr1 = tr[0]
tr2 = tr[1]
trb.send_keys(tr1)  # То что после ТРЕБОВАНИЯ
obz = browser.find_elements_by_tag_name('ul')[2]
obz.send_keys(lstobi)  # То что после УСЛОВИЯ
obz.send_keys(Keys.BACKSPACE)
trsplit = tr2.split(' ', 2)
tr21 = trsplit[0] + ' ' + trsplit[1]
tr22 = trsplit[2]
obz.send_keys(Keys.ENTER + Keys.ENTER)
lastp = browser.find_elements_by_tag_name('p')[-1]
lastp.send_keys(Keys.LEFT_CONTROL + "b" + tr21)
# print(tr21)
# print(tr22)
# obz.send_keys(tr21)
lastp.send_keys(' ' + Keys.LEFT_CONTROL + "b")
lastp.send_keys(tr22)

# print(tr22)
# obz.send_keys(tr22)
# obz.send_keys(Keys.ENTER + Keys.ENTER + tr2)
lastp = browser.find_elements_by_tag_name('p')[-1]
# div.send_keys(Keys.SHIFT + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN)
# div.send_keys(Keys.LEFT_CONTROL + 'b')
driver.switch_to.default_content()


time.sleep(10)
browser.quit()