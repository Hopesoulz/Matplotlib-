# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18vMBBYFfx0lUG0R9OApLReTqrizKigFS
"""

import pandas as pd


data = {
    'Ism': ['Umid', 'Bobur', 'Jasur', 'Musli', 'Akmal'],
    'Age': [28, 22, 35, 32, 45],
    'City': ['Namangan', 'Buxoro', 'Fergana', 'Andijon', 'Toshkent']
}


df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


filtered_df = df[df['Age'] > 30]
print("\nYoshi 30 dan katta bo'lganlar:")
print(filtered_df)


filtered_df2 = df[(df['Age'] <= 30) & (df['City'] == 'London')]
print("\nYoshi 30 dan kichik yoki teng bo'lganlar va 'City' London bo'lganlar:")
print(filtered_df2)

import pandas as pd


data = {
    'Ism': ['Umid', 'Bobur', 'Jasur', 'Musli', 'Akmal'],
    'Age': [28, 22, 35, 32, 45],
    'City': ['Namangan', 'Buxoro', 'Fergana', 'Andijon', 'Toshkent']
}


df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


filtered_df = df[df['Age'] > 30]
print("\nYoshi 30 dan katta bo'lganlar:")
print(filtered_df)


filtered_df2 = df[(df['Age'] <= 30) & (df['City'] == 'London')]
print("\nYoshi 30 dan kichik yoki teng bo'lganlar va 'City' London bo'lganlar:")
print(filtered_df2)

"""# Новый раздел"""