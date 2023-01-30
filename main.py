import matplotlib.pyplot as plt


precipitacao = [90, 134, 132, 159, 259, 180, 178, 159, 158, 100, 95, 88] # y1
temp_max = [28,31,30,30,28,28,27,28,30,31,32,33] # y2 
temp_min = [22,23,23,22,21,20,20,21,22,23,23,24] # y3
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

fig, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(meses, precipitacao, label = 'Precipitação', width=0.8, color='#F5DD88')
ax1.set_ylabel("Precipitação (mm)", fontsize=8, labelpad=10)
ax1.set_xticklabels(meses, fontsize=8)
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

ax2 = plt.twinx(ax1)
ax2.plot(meses,temp_max, label = 'Temp. Max', color='m', marker='o', linewidth=1.5, markersize=5)
ax2.plot(meses,temp_min, label = 'Temp. Min', color='g', marker='D', linewidth=1.5, markersize=5)
ax2.set_ylabel("Temp. Min/Max (°C)", fontsize=8, labelpad=10)


plt.title('Gráfico de Pluviosidade', loc='left', pad=20, fontweight='semibold')

fig.legend(loc='upper right', ncol = 3, fontsize='small', bbox_to_anchor=(0.9, 0.98))

plt.savefig("pluviosidade.png", dpi=300)
plt.show() 