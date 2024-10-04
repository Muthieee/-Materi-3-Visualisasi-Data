import numpy as np
import matplotlib.pyplot as plt

# Konstanta
g = 9.8  # percepatan gravitasi (m/s^2)
h0 = 100  # ketinggian awal (misalnya 100 meter)

# Waktu jatuh hingga mencapai tanah
t_max = np.sqrt(2 * h0 / g)
print(f'Waktu jatuh hingga mencapai tanah: {t_max:.2f} detik')

# Waktu dalam rentang dari 0 sampai waktu jatuh
t = np.linspace(0, t_max, 500)

# Kecepatan sebagai fungsi waktu
v_t = g * t

# Posisi sebagai fungsi waktu
h_t = h0 - 0.5 * g * t**2

# Plot grafik kecepatan vs waktu
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.plot(t, v_t, label='Kecepatan (v)')
plt.title('Grafik Kecepatan sebagai fungsi Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan (m/s)')
plt.grid(True)
plt.legend()

# Plot grafik posisi vs waktu
plt.subplot(1, 2, 2)
plt.plot(t, h_t, label='Posisi (h)', color='orange')
plt.title('Grafik Posisi sebagai fungsi Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Ketinggian (m)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
