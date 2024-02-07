#!/usr/bin/env python
# coding: utf-8

# In[2]:


phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
if len(phrase_1)>len(phrase_2):
    print('Фраза 1 длиннее фразы 2')


# In[26]:


phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
if len(phrase_1)>len(phrase_2):
    print('Фраза 1 длинее фразы 2')
else:
    print('Фраза 2 длинее фразы 1')
    


# In[39]:


phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'

if len(phrase_1) > len(phrase_2):
    print('Длина фразы 1 больше длины фразы 2')
elif len(phrase_1) < len(phrase_2):
    print('Длина фразы 2 больше длины фразы 1')
else:
    print('Фразы равной длины')
    


# In[41]:


user_year=int(input('Введите год'))
if user_year%4==0:
    print('Високосный год')
else:
    print('Обычный год')


# In[46]:


user_month = int(input('Введите порядковый номер месяца (1-12): '))
user_day = int(input('Введите день: '))

if user_month == 3 and user_day >= 21 or user_month == 4 and user_day <= 19:
    print('Овен')
elif user_month == 4 and user_day >= 20 or user_month == 5 and user_day <= 20:
    print('Телец')
elif user_month == 5 and user_day >= 21 or user_month == 6 and user_day <= 21:
    print('Близнецы')
elif user_month == 6 and user_day >= 22 or user_month == 7 and user_day <= 22:
    print('Рак')
elif user_month == 7 and user_day >= 22 or user_month == 8 and user_day <= 22:
    print('Лев')
elif user_month == 8 and user_day >= 23 or user_month == 9 and user_day <= 23:
    print('Дева')
elif user_month == 9 and user_day >= 24 or user_month == 10 and user_day <= 24:
    print('Весы')
elif user_month == 10 and user_day >= 24 or user_month == 11 and user_day <= 21:
    print('Скорпион')
elif user_month == 11 and user_day >= 22 or user_month == 12 and user_day <= 21:
    print('Стрелец')
elif user_month == 12 and user_day >= 22 or user_month == 1 and user_day <= 20:
    print('Козерог')
elif user_month == 1 and user_day >= 22 or user_month == 2 and user_day <= 20:
    print('Водолей')
else:
    print('Рыбы')


# In[ ]:


width = int(input('Введите ширину товара: '))
length = int(input('Введите длину товара: '))
height = int(input('Введите высоту товара: '))

if width <= 15 and length <= 15 and height <= 15:
    print('Коробка №1')
elif width <= 200 or length <= 200 or height <= 200:
    print('Коробка для лыж')
elif 15 < width <= 50 and 15 < length <= 50 and 15 < height <= 50:
    print('Коробка №2')
else:
    print('Коробка №3')
    
    


# In[68]:


word=str(input('Введите слово:'))
if length % 2 == 1:
    print("Средняя буква:", word[length // 2])
else:
    print("Две средних буквы:", word[length // 2 - 1:length // 2 + 1])


# In[ ]:





# In[ ]:



    


# In[70]:


word = input('Введите слово из латинских букв: ')
length = len(word)

if length % 2 == 1:
    middle_index = length 
    middle_letter = word[middle_index]
    print(f"'Средняя буква:' {middle_letter}")
else:
    middle_index1 = length
    middle_index2 = length 
    middle_letters = length[middle_index1:middle_index2]
    print(f"'Две средних буквы:' {middle_letters}")


# In[84]:





# In[90]:


total_sum = 0

while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    else:
        total_sum += number

print(f"Результат: {total_sum}")


# In[105]:


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys_girls=zip(sorted(boys),sorted(girls))
print(f'Идеальная пара: {list(boys_girls)}')




# In[113]:


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys)==len(girls):
    boys_girls=zip(sorted(boys), sorted(girls))
    print(f'Идеальные пары: {list(boys_girls)}')
else:
    print('Внимание, кто-то может остаться без пары!')


# In[ ]:





# In[126]:


countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print("Средняя температура в странах:")

for country, temperatures_f in countries_temperature:
    average_temp_c = (sum(temperatures_f) / len(temperatures_f) - 32) * 5 / 9
    print(f"{country} - {average_temp_c:.1f} C")


# In[ ]:




