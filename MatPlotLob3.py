import matplotlib.pyplot as plt
import numpy as np

company=['Google','Amzn','MSFT','FB']
revenue=[90,136,89,27]
profit =[40,2,34,12]

ypos = np.arange(len(company))

plt.xticks(ypos,company)
plt.ylabel('Revenue amt')
plt.title('Income Graph')
plt.barh(ypos,revenue, label="Revenue")
plt.barh(ypos,profit,label="Profit")
plt.legend()

plt.show()

