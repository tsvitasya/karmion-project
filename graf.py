import matplotlib.pyplot as plt
import numpy as np

# =====================================================================
# ВВОДДНЫЕ ДАННЫЕ КЛИЕНТА (Сюда подставляются реальные дата и возраст)
# =====================================================================
day = 26
month = 4
year = 1984
target_age = 42

# --- Автоматический расчет энергий системы КАРМИОН строго по Твоим формулам ---
luna_base_A = month  # Точка А (Внутреннее ядро, верх)
sj_energy = day if day <= 22 else day - 22  # Точка Б (Внутреннее ядро, левый низ)

osh_energy = abs(sj_energy - luna_base_A)
if osh_energy == 0: 
    osh_energy = 22  # Точка В (Внутреннее ядро, правый низ)

# Расчет чисел периода (Луна и Солнце года)
code_number = day * month * year
work_num = code_number if target_age <= 0 else int(code_number / target_age)
work_number_str = str(abs(work_num))
if len(work_number_str) < 4: 
    work_number_str = work_number_str + "0" * (4 - len(work_number_str))

luna_period = int(work_number_str[0]) + int(work_number_str[1])
if luna_period > 22: luna_period = int(str(luna_period)[0]) + int(str(luna_period)[1])
if luna_period == 0: luna_period = 22

solnce_period = int(work_number_str[2:4])
if solnce_period > 22: solnce_period = int(str(solnce_period)[0]) + int(str(solnce_period)[1])
if solnce_period == 0: solnce_period = 22

raw_itog = -luna_period + solnce_period
itog_period = 22 if raw_itog == 0 else abs(raw_itog)
if itog_period > 22: itog_period = int(str(itog_period)[0]) + int(str(itog_period)[1])

# --- Привязка рассчитанных энергий к 6 внешним лучам звезды ---
luch1 = day if day <= 22 else day - 22  # Луч 1 (День рождения / базовая энергия)
luch2 = luna_period                     # Луч 2 (Внутренний план периода)
luch3 = solnce_period                   # Луч 3 (Внешний план / финансы)
luch4 = itog_period                     # Луч 4 (Итоговый вектор периода)
luch5 = 7                               # Луч 5 (Ядро силы)
luch6 = 9                               # Луч 6 (Глобальный вектор)

# =====================================================================
# ГРАФИЧЕСКИЙ БЛОК: ЧИСТАЯ ЭСТЕТИКА МАТРИЦЫ
# =====================================================================
peach_bg = '#FCE6DC' # Твой нежно-розовый персиковый фон

fig, ax = plt.subplots(figsize=(8, 8), facecolor=peach_bg)
ax.set_facecolor(peach_bg)
ax.set_aspect('equal') # Идеальная защита от деформации фигуры

# Радиус для внешних лучей большой звезды Давида
r_star = 3.4

# Вычисление координат 6 внешних пиков по кругу (начиная с 12 часов)
angles = np.array([90, 30, 330, 270, 210, 150]) * (np.pi / 180)
x_luch = r_star * np.cos(angles)
y_luch = r_star * np.sin(angles)

# 1. СТРОИМ ВНЕШНЮЮ ЗВЕЗДУ ДАВИДА (Два больших сквозных треугольника)
# Первый большой треугольник (Пики: 1 -> 5 -> 3 -> 1)
x_big1 = [x_luch[0], x_luch[4], x_luch[2], x_luch[0]]
y_big1 = [y_luch[0], y_luch[4], y_luch[2], y_luch[0]]
ax.plot(x_big1, y_big1, color='#D4AF37', linewidth=3, zorder=2) # Благородное золото

# Второй большой треугольник (Пики: 4 -> 2 -> 6 -> 4)
x_big2 = [x_luch[3], x_luch[1], x_luch[5], x_luch[3]]
y_big2 = [y_luch[3], y_luch[1], y_luch[5], y_luch[3]]
ax.plot(x_big2, y_big2, color='#D4AF37', linewidth=3, zorder=2)

# Тонкие золотые лучи-направляющие из центра к вершинам для сакрального эффекта
for i in range(6):
    ax.plot([0, x_luch[i]], [0, y_luch[i]], color='#D4AF37', linestyle=':', linewidth=1, zorder=1)

# Рисуем аккуратные шоколадные кружки-подложки на 6 внешних пиках звезды
ax.scatter(x_luch, y_luch, color='#5C4033', s=550, zorder=5)

# Расставляем НАСТОЯЩИЕ рассчитанные цифры внутрь внешних кружков (Без надписей "Луч")
luch_values = [luch1, luch2, luch3, luch4, luch5, luch6]
for i in range(6):
    ax.text(x_luch[i], y_luch[i], str(luch_values[i]), color='white', ha='center', va='center', fontsize=12, fontweight='bold', zorder=6)


# 2. СТРОИМ ВНУТРЕННИЙ ТРЕУГОЛЬНИК КАРМЫ (ЯДРО)
# Компактный размер, сидит строго в центре, вершиной направлен вверх
r_core = 1.3
angles_core = np.array([90, 210, 330, 90]) * (np.pi / 180)
x_core = r_core * np.cos(angles_core)
y_core = r_core * np.sin(angles_core)

# Рисуем плотный бордовый внутренний треугольник кармы
ax.plot(x_core, y_core, color='#8B0000', linewidth=4, zorder=4)
ax.fill(x_core[:-1], y_core[:-1], color='#FFFFFF', alpha=0.4, zorder=3) # Мягкое высветление центра

# Рисуем бордовые кружки на углах ВНУТРЕННЕГО ядра для Точек А, Б, В
ax.scatter(x_core, y_core, color='#8B0000', s=450, zorder=7)

# Расставляем РЕАЛЬНЫЕ цифры кармических точек внутрь кружков ядра (Никаких букв А, Б, В!)
# Точка А (Вверху по центру ядра)
ax.text(x_core[0], y_core[0], str(luna_base_A), color='white', ha='center', va='center', fontsize=11, fontweight='bold', zorder=8)

# Точка Б (Снизу слева ядра)
ax.text(x_core[1], y_core[1], str(sj_energy), color='white', ha='center', va='center', fontsize=11, fontweight='bold', zorder=8)

# Точка В (Снизу справа ядра)
ax.text(x_core[2], y_core[2], str(osh_energy), color='white', ha='center', va='center', fontsize=11, fontweight='bold', zorder=8)


# Финальные настройки отображения
ax.set_xlim(-4.6, 4.6)
ax.set_ylim(-4.6, 4.6)
ax.axis('off') # Убираем техническую разметку, оставляем только чистую карту

print("КАРТА КЛИЕНТА СИСТЕМЫ КАРМИОН СФОРМИРОВАНА.")
plt.show()



