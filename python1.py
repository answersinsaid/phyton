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
    
    


# In[ ]:





# In[ ]:




