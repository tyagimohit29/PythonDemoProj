import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My wheather chart!')

# function to show the plot
plt.plot(x,y,color='green',linestyle='dotted')

plt.show()



