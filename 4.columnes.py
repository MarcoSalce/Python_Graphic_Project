import matplotlib.pyplot as plt
dades = [10,40]
ind=range(2)
fig, ax = plt.subplots()
width = 0.35
rects1 = ax.bar(ind, dades, width, color='r')
ax.set_ylabel('Habitants') # Llegenda de eix Y.
ax.set_title('Demografia del poble {0:} amb edats entre {1:} i {2:}'.format('Tortella',2,5))
ax.set_xticks(ind)
ax.yaxis.set_major_locator(plt.NullLocator())
ax.set_xticklabels(('HOMES', 'DONES'))
ax.set_yticklabels([])
for rect in rects1:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom')
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
plt.savefig('{}.png'.format('TortellaBarres'), bbox_inches='tight')
plt.close(fig)