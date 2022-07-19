import matplotlib.pyplot as plt
dades = [10,40]
ind=range(2)
fig, ax = plt.subplots()
rects = ax.barh(ind, dades, align='center',color='green', ecolor='black')
ax.set_yticks(ind)
ax.set_yticklabels(('HOMES', 'DONES'))
ax.invert_yaxis() # labels read top-to-bottom
ax.set_xlabel('Habitants')
ax.set_title('Demografia del poble {0:} amb edats entre {1:} i {2:}'.format('Tortella',2,5))
for i, v in enumerate(dades):
    ax.text(v , i, str(v), color='blue', fontweight='bold')
ax.xaxis.set_major_locator(plt.NullLocator())
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.savefig('{}.png'.format('TortellaHoritzontal'), bbox_inches='tight')
plt.close(fig)