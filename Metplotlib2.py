import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
max_t = [50,51,52,48,47,49,46]
min_t = [43,42,40,44,33,35,37]
avg_t = [45,48,48,46,40,42,42]

plt.plot(days,max_t, label='Max')
plt.plot(days,min_t,label='Min')
plt.plot(days,avg_t, label='AVg')

plt.xlabel('Days')
plt.ylabel('Temprature')
plt.title('Wheater')

plt.legend(loc="best", shadow=True, fontsize="small")

plt.grid()

plt.show()

