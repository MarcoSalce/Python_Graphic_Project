import matplotlib.pyplot as plt

#PARAMETRES GENERALS DE LA FIGURA
SMALL_SIZE = 15
MEDIUM_SIZE = 15
BIGGER_SIZE = 15
plt.rc('font', size=SMALL_SIZE) # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE) # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE) # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE) # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE) # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE) # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title


#PARAMETRES DELS SUBGRAFICS

fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,15))
fig.suptitle('Demografia Tortella')
fig.tight_layout(pad=10.0) 

# DIAGRAMA DE COLUMNES
dades = [10,40]
ind=range(2)
width = 0.35
rects1 = ax1.bar(ind, dades, width, color='r')
ax1.set_ylabel('Habitants')
ax1.set_xticks(ind)
ax1.yaxis.set_major_locator(plt.NullLocator())
ax1.set_xticklabels(('HOMES', 'DONES'))
ax1.set_yticklabels([])
for rect in rects1:
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom')
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)

# DIAGRAMA DE SECTORS

labels = 'Homes', 'Dones'
sizes = [10, 40]
colors = ['gold', 'yellowgreen']
explode = (0, 0)
ax2.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
ax2.axis('equal')


# DIAGRAMA DE BARRES

rects = ax3.barh(ind, dades, align='center',color='green', ecolor='black')
ax3.set_yticks(ind)
ax3.set_yticklabels(('HOMES', 'DONES'))
ax3.invert_yaxis()
ax3.set_xlabel('Habitants')
for i, v in enumerate(dades):
    ax3.text(v , i, str(v), color='blue', fontweight='bold')
ax3.xaxis.set_major_locator(plt.NullLocator())
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)



# GUARDAR FIGURA
plt.savefig('{}.png'.format('Tortellatots'))
plt.close(fig)