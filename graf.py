import matplotlib.pyplot as plt
import numpy as np
import kara  # Теперь он официально связан с твоим расчетом

# Получаем данные из кара.py через нашу функцию
data = kara.get_karmion_data(target_age=42)

# Присваиваем значения для рисования
luna_base_A = data["luna_base_A"]
sj_energy = data["sj_energy"]
osh_energy = data["osh_energy"]
luch_values = [data["luch1"], data["luch2"], data["luch3"], data["luch4"], data["luch5"], data["luch6"]]

# --- ГРАФИЧЕСКИЙ БЛОК ---
peach_bg = '#FCE6DC'
fig, ax = plt.subplots(figsize=(8, 8), facecolor=peach_bg)
ax.set_facecolor(peach_bg)
ax.set_aspect('equal')

r_star = 3.4
angles = np.array([90, 30, 330, 270, 210, 150]) * (np.pi / 180)
x_luch = r_star * np.cos(angles)
y_luch = r_star * np.sin(angles)

# Звезда Давида
ax.plot([x_luch[0], x_luch[4], x_luch[2], x_luch[0]], [y_luch[0], y_luch[4], y_luch[2], y_luch[0]], color='#D4AF37', linewidth=3, zorder=2)
ax.plot([x_luch[3], x_luch[1], x_luch[5], x_luch[3]], [y_luch[3], y_luch[1], y_luch[5], y_luch[3]], color='#D4AF37', linewidth=3, zorder=2)

ax.scatter(x_luch, y_luch, color='#5C4033', s=550, zorder=5)
for i in range(6):
    ax.text(x_luch[i], y_luch[i], str(luch_values[i]), color='white', ha='center', va='center', fontsize=12, fontweight='bold', zorder=6)

# Ядро
r_core = 1.3
angles_core = np.array([90, 210, 330, 90]) * (np.pi / 180)
x_core = r_core * np.cos(angles_core)
y_core = r_core * np.sin(angles_core)

ax.plot(x_core, y_core, color='#8B0000', linewidth=4, zorder=4)
ax.fill(x_core[:-1], y_core[:-1], color='#FFFFFF', alpha=0.4, zorder=3)
ax.scatter(x_core, y_core, color='#8B0000', s=450, zorder=7)

ax.text(x_core[0], y_core[0], str(luna_base_A), color='white', ha='center', va='center', fontsize=11, fontweight='bold', zorder=8)
ax.text(x_core[1], y_core[1], str(sj_energy), color='white', ha='center', va='center', fontsize=11, fontweight='bold', zorder=8)
ax.text(x_core[2], y_core[2], str(osh_energy), color='white', ha='center', va='center', fontsize=11, fontweight='bold', zorder=8)

ax.axis('off')
plt.show()


