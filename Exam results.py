import json
import numpy as np
import matplotlib.pyplot as plt

with open("dataset/Exam results.json", "r", encoding = 'utf-8') as read_file:
    data = json.load(read_file)

n = 20

sorted_data = sorted(data, key=lambda x: x['PASSES_OVER_220'], reverse=True)

sorted_data_n = np.asarray(sorted_data[:n:])

EDU_NAME = np.array([])
PASSES_OVER_220 = np.array([])
PASSER_UNDER_160 = np.array([])
for item in sorted_data_n:
    EDU_NAME = np.append(EDU_NAME, item['EDU_NAME'])
    PASSES_OVER_220 = np.append(PASSES_OVER_220, item['PASSES_OVER_220'])
    PASSER_UNDER_160 = np.append(PASSER_UNDER_160, item['PASSER_UNDER_160'])

plt.axis([0,n+1,100,800])
PASSES_OVER_220_visual = PASSES_OVER_220
schools = list(range(1, n+1))
schools = list(map(str, schools))

plt.figure(figsize=(13,6))

plt.plot(schools, PASSER_UNDER_160)
plt.scatter(schools, PASSER_UNDER_160, color='green', s=40, marker='o')
plt.plot(schools, PASSES_OVER_220)
plt.scatter(schools, PASSES_OVER_220, color='green', s=40, marker='o')

data = {'количество учеников, получивших больше 220 баллов',
        'количество учеников, получивших меньше 160 баллов'}

plt.legend(data, loc=2)
plt.title('20 школ Москвы, с наибольшим количество учеников, набравших более 220 баллов по результатам ЕГЭ')

for i in range(n):
    print(i+1, ' - ', EDU_NAME[i])

plt.show()


