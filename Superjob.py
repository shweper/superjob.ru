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

# Административная работа, секретариат, АХО
xpath_it_adm_personal = {

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

# Транспорт, логистика, ВЭД
xpath_logistika = {
    'Авиаперевозки': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[1]/div/div/label/div/div[1]/input',
    'Автоперевозки': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[2]/div/div/label/div/div[1]/input',
    'ВЭД': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[3]/div/div/label/div/div[1]/input',

    'Железнодорожные перевозки': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[4]/div/div/label/div/div[1]/input',
    'Контейнерные перевозки': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[5]/div/div/label/div/div[1]/input',

    'Логистика': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[6]/div/div/label/div/div[1]/input',
    'Метрополитен': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[7]/div/div/label/div/div[1]/input',

    'Морские, речные перевозки': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[8]/div/div/label/div/div[1]/input',
    'Складское хозяйство': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[9]/div/div/label/div/div[1]/input',
    'Таможня': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[10]/div/div/label/div/div[1]/input',
    'Трубопроводы': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[11]/div/div/label/div/div[1]/input',

    'Другое': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[12]/div/div/label/div/div[1]/input',
    'Начало карьеры, мало опыта': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[13]/div/div/label/div/div[1]/input',
}

# Банки, инвестиции, лизинг

xpath_banki_invest = {

    'Банковская бухгалтерия': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[1]/div/div/label/div/div[1]/input',
    'Бэк-Офис': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[2]/div/div/label/div/div[1]/input',
    'Бюджетирование и планирование': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[3]/div/div/label/div/div[1]/input',
    'Валютные операции': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[4]/div/div/label/div/div[1]/input',
    #
    'Вклады': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[5]/div/div/label/div/div[1]/input',
    'Депозитарий': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[6]/div/div/label/div/div[1]/input',
    'Документарные операции': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[7]/div/div/label/div/div[1]/input',
    'Залоги и проблемная задолженность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[8]/div/div/label/div/div[1]/input',
    #
    'Ипотека': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[9]/div/div/label/div/div[1]/input',
    'Кредитование физических лиц': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[10]/div/div/label/div/div[1]/input',
    'Кредитование юридических лиц': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[11]/div/div/label/div/div[1]/input',
    #
    'Лизинг': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[12]/div/div/label/div/div[1]/input',
    'Методология, разработка и продажа корпоративных продуктов': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[13]/div/div/label/div/div[1]/input',
    #
    'Методология, разработка и продажа продуктов Private Banking': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[14]/div/div/label/div/div[1]/input',
    'Методология, разработка и продажа розничных продуктов': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[15]/div/div/label/div/div[1]/input',
    'Налоговый учёт': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[16]/div/div/label/div/div[1]/input',
    'Обслуживание банкоматов': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[17]/div/div/label/div/div[1]/input',
    'Пластиковые карты (эквайринг)': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[18]/div/div/label/div/div[1]/input',
    #
    'Продажа банковских продуктов': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[19]/div/div/label/div/div[1]/input',
    'Разработка банковских продуктов': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[20]/div/div/label/div/div[1]/input',
    'Расчёты и обработка платежей, касса': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[21]/div/div/label/div/div[1]/input',
    #
    'Риски': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[22]/div/div/label/div/div[1]/input',
    'Торговое финансирование': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[23]/div/div/label/div/div[1]/input',
    'Управление активами': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[24]/div/div/label/div/div[1]/input',
    #
    'Управление ликвидностью и балансовыми рисками': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[25]/div/div/label/div/div[1]/input',
    'Управленческая отчетность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[26]/div/div/label/div/div[1]/input',
    'Финансовая отчётность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[27]/div/div/label/div/div[1]/input',
    'Финансовый анализ и контроль': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[28]/div/div/label/div/div[1]/input',
    #
    'Ценные бумаги': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[29]/div/div/label/div/div[1]/input',
    'Другое': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[30]/div/div/label/div/div[1]/input',
    'Начало карьеры, мало опыта': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[31]/div/div/label/div/div[1]/input',
}

# Безопасность, службы охраны
xpath_ohrana= {
    'Видеонаблюдение': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[1]/div/div/label/div/div[1]/input',
    'Имущественная безопасность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[2]/div/div/label/div/div[1]/input',
    'Инкассация': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[3]/div/div/label/div/div[1]/input',

    'Информационная безопасность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[4]/div/div/label/div/div[1]/input',
    'Кинология': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[5]/div/div/label/div/div[1]/input',

    'Личная безопасность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[6]/div/div/label/div/div[1]/input',
    'Охранно-, детективная деятельность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[7]/div/div/label/div/div[1]/input',

    'Охранные службы предприятий': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[8]/div/div/label/div/div[1]/input',
    'Пожарная безопасность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[9]/div/div/label/div/div[1]/input',
    'Служба спасения': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[10]/div/div/label/div/div[1]/input',
    'ЧОП': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[11]/div/div/label/div/div[1]/input',

    'Экономическая безопасность': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[12]/div/div/label/div/div[1]/input',
    'Другое': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[13]/div/div/label/div/div[1]/input',
    'Начало карьеры, мало опыта': '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/ul/li[14]/div/div/label/div/div[1]/input',
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

# СЧИТЫВАЕМ ГОРОДА иЗ ЭКСЕЛЯ ДИНАМИЧЕСКИ

sheet = wb[lst[1]]
sheet.title

barnaul_adr = []
volgograd_adr = []
voronej_adr = []
ekaterenburg_adr = []
izevsk_adr = []
irkuts_adr = []
kazan_adr = []
kaliningrad_adr = []
kemerovo_adr = []
krasnodar_adr = []
krasnoyars_adr = []
moskow_adr = []
naber_cheln_adr = []
nizniy_novgorod_adr = []
novosib_adr = []
omsk_adr = []
orenburg_adr = []
perm_adr = []
rostov_na_dony_adr = []
ryazan_adr = []
samara_adr = []
sankt_peter_adr = []
saratov_adr = []
sochi_and_adler = []
toliatty_adr = []
tomsk_adr = []
tyla_adr = []
tumen_adr = []
ufa_adr = []
chelabinsk_adr = []
yaroslavl_adr = []
musor_exela = []
#goroda_arr = [musor_exela, barnaul_adr, volgograd_adr, voronej_adr, ekaterenburg_adr, izevsk_adr, irkuts_adr, kazan_adr, kaliningrad_adr, kemerovo_adr, krasnodar_adr, krasnoyars_adr, moskow_adr, naber_cheln_adr, nizniy_novgorod_adr, novosib_adr, omsk_adr, orenburg_adr, perm_adr, rostov_na_dony_adr, ryazan_adr, samara_adr, sankt_peter_adr, saratov_adr, sochi_and_adler, toliatty_adr, tomsk_adr, tyla_adr, tumen_adr, ufa_adr, chelabinsk_adr, yaroslavl_adr]
goroda_arr = []

kolichestvo_gorodov = 0

for cell in sheet['A']:
    kolichestvo_gorodov += 1
    print(cell.value)

for number_gorod in range(kolichestvo_gorodov):
    goroda_arr.append([])
    for cell in list(sheet.rows)[number_gorod]:
         if cell.value != None:
            goroda_arr[number_gorod].append(cell.value)

kolichestvo_adresov = []
high_number_gorod = 0
number_goroda = 0
while number_goroda < len(goroda_arr):
    max_number = len(goroda_arr[number_goroda])
    kolichestvo_adresov.append(len(goroda_arr[number_goroda]))
    if high_number_gorod< max_number:
        high_number_gorod = max_number
        number_goroda = number_goroda + 1
    else:
        number_goroda = number_goroda + 1
############### Login ########################

browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/form/div/div[3]/div/div/div/div/div[1]/label/div/div/input').send_keys(login)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/form/div/div[3]/div/div/div/div/div[2]/label/div/div[1]/input').send_keys(password)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/form/div/div[4]/div/div[1]/button').click()

############### Должность ####################
time.sleep(4)
browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/label/div/div/input').send_keys(vacancy)

############## Специализация #################

browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/button').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/button').click()




############# Занятость #################### НУЖНО СДЕЛАТЬ

browser.find_element_by_xpath('//*[@id="detailInfo.workType.id-input"]').click()
browser.find_element_by_xpath('//*[@id="detailInfo.workType.id-input"]').send_keys(grafik + Keys.ENTER)
############# Уровень дохода ###############

browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[7]/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/label/div/div[2]/input').send_keys(zp_ot)
browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[7]/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[2]/label/div/div[2]/input').send_keys(zp_do)

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
'''
yslovia = opisanie.partition('Условия:')
# print(x[1])
obiaznosti = yslovia[2].partition('Обязанности:')

lst_obiaznosti = list(obiaznosti)
lstobi = lst_obiaznosti[0].split('\n', 1)
del lstobi[0]

trebovania = obiaznosti[2].partition('Требования:')
lst_trebovania = list(trebovania)
lst_treb = lst_trebovania[1].split('\n', 1)
# print(obiaznosti[0], trebovania[0], trebovania[2])
print(lst_treb)
print(obiaznosti) #условия
print(yslovia) #
treb0 = lst_trebovania[0].split('\n', 1)
'''
#Вытаскиваем Условия
frag_opisanie = opisanie.partition('Условия:')
frag_opisanie = frag_opisanie[2].partition('Обязанности:')
frag_opisanie = frag_opisanie[0].split('\n', 1)
del frag_opisanie[0]
yslovia = frag_opisanie[0]

#Вытаскиваем Обязанности
frag_opisanie = opisanie.partition('Обязанности:')
frag_opisanie = frag_opisanie[2].partition('Требования:')
frag_opisanie = frag_opisanie[0].split('\n', 1)
del frag_opisanie[0]
obiaznosti = frag_opisanie[0]

#Вытаскиваем Требования
frag_opisanie = opisanie.partition('Требования:')
frag_opisanie = frag_opisanie[2].partition('\n \n')
frag_opisanie = frag_opisanie[0].split('\n', 1)
del frag_opisanie[0]
trebovania = frag_opisanie[0]

#Вытаскиваем шапку
frag_opisanie = opisanie.partition('Условия:')
shapka = frag_opisanie[0]
print(frag_opisanie)

#Вытаскиваем подвал
frag_opisanie = opisanie.partition('\n \n')
podval = frag_opisanie[2]

#Заполняем описание
linii = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[10]/div/div/div[2]/div/div[1]/div/div/div/div[2]')
linii.find_element_by_tag_name('b').send_keys(Keys.ARROW_UP + Keys.ENTER)
lst_linii = linii.find_elements_by_tag_name('li')
linii.find_element_by_tag_name('p').send_keys(Keys.LEFT_CONTROL + 'b' + Keys.LEFT_CONTROL + (shapka + Keys.BACKSPACE))
lst_linii[0].send_keys(obiaznosti + Keys.BACKSPACE + Keys.DELETE)
lst_linii[2].send_keys(trebovania + Keys.DELETE)
lst_linii[4].send_keys(yslovia + Keys.BACKSPACE + Keys.DELETE)
linii.send_keys('\n\n' + Keys.LEFT_CONTROL + 'b' + Keys.LEFT_CONTROL + podval)



#Заполняем города
#ля теста iter_gorod
iter_gorod = 1
adr_bar = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[4]/div/div[1]/div/div/div[3]/div/div[1]/label/div/div/input')
random_adres = random.randint(1, kolichestvo_adresov[iter_gorod]-1)
print('random adres = ', random_adres)
adr_bar.send_keys(goroda_arr[iter_gorod][0])
adr_bar = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/form/div/div[1]/div/div/div[4]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/label/div/div/input')
adr_bar.send_keys(goroda_arr[iter_gorod][random_adres])
# print(tr22)
# obz.send_keys(tr22)
# obz.send_keys(Keys.ENTER + Keys.ENTER + tr2)
lastp = browser.find_elements_by_tag_name('p')[-1]
# div.send_keys(Keys.SHIFT + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN)
# div.send_keys(Keys.LEFT_CONTROL + 'b')
driver.switch_to.default_content()


time.sleep(10)
browser.quit()