import matplotlib.pyplot as plt
import numpy as np

# Линейа
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Линейный график')
plt.legend()
plt.show()

# Столбчатая диаграмма
x = ['A', 'B', 'C']
y1 = [10, 15, 7]
y2 = [8, 12, 10]
plt.bar(x, y1, label='Группа 1')
plt.bar(x, y2, label='Группа 2')
plt.xlabel('Группа')
plt.ylabel('Значение')
plt.title('Столбчатая диаграмма')
plt.legend()
plt.show()

# Круговая
labels = ['Категория 1', 'Категория 2']
sizes = [30, 70]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Круговая диаграмма')
plt.show()

# рассеяния
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Диаграмма рассеяния')
plt.show()

# Гистограмма
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(3, 1.5, 1000)
data3 = np.random.normal(-2, 0.5, 1000)
plt.hist(data1, bins=20, alpha=0.5, label='Группа 1')
plt.hist(data2, bins=20, alpha=0.5, label='Группа 2')
plt.hist(data3, bins=20, alpha=0.5, label='Группа 3')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма')
plt.legend()
plt.show()
