import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parametre t'nin aralığı ve çözünürlüğü
t = np.linspace(0, 1, 100)

# Fonksiyonlar
x = np.cumsum(np.cos(t**2) * (t[1] - t[0]))  # dx = cos(t^2) dt'nin integrali
y = np.cumsum(np.sin(t**2) * (t[1] - t[0]))  # dy = sin(t^2) dt'nin integrali
kappa = 2 * t  # Eğrilik

# Verileri bir DataFrame'e kaydet
data = pd.DataFrame({
    't': t,
    'x': x,
    'y': y,
    'kappa': kappa
})

# Veriyi Excel dosyasına yaz
excel_file = 'curve_and_curvature.xlsx'
data.to_excel(excel_file, index=False)
print(f"Veriler '{excel_file}' dosyasına kaydedildi.")

# Grafik çizimi
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# Eğri çizimi
axs[0].plot(x, y, label='Eğri: (x(t), y(t))')
axs[0].set_title('Eğri Çizimi')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].legend()
axs[0].grid()

# Eğrilik grafiği
axs[1].plot(t, kappa, label='Eğrilik: κ(t) = 2t', color='r')
axs[1].set_title('Eğrilik Fonksiyonu')
axs[1].set_xlabel('t')
axs[1].set_ylabel('κ(t)')
axs[1].legend()
axs[1].grid()

plt.tight_layout()
plt.show()