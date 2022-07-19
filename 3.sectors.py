import matplotlib.pyplot as plt
fig, ax = plt.subplots()
labels = 'Homes', 'Dones'
sizes = [10, 20]
colors = ['gold', 'yellowgreen']
explode = (0, 0) # explode 1st slice and 2nd with 0.1
ax.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
ax.set_title('Demografia del poble {0:} amb edats entre {1:} i {2:}'.format('Tortella',2,5))
ax.axis('equal')
plt.savefig('{}.png'.format('tortella'), bbox_inches='tight')
plt.close(fig)
