# This is a sample Python script.
import os
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from datasort import sort_data
from datasort import sort_data_text


# sport and alcohol are string values in data created for now, so the coding looks different to the real values for plotting
path = "figures"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)






dat = sqlite3.connect('DataTable.db')  # data import from sql
query = dat.execute("SELECT * From DATA")  # able editing
cols = [column[0] for column in query.description]
results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)  # changing sql into panda
print(results)

df_ = results[['date', 'weather']].copy()  # dividing into several caterogries
wtb = results[['date', 'wenttobed']].copy()
wtb['wenttobed'] = pd.to_numeric(wtb['wenttobed'])
wu = results[['date', 'wokeup']].copy()
wu['wokeup'] = pd.to_numeric(wu['wokeup'])
sp = results[['date', 'sports']].copy()
ci = results[['date', 'cigarettes']].copy()
al = results[['date', 'alcohol']].copy()
sa = results[['date', 'sleephours']].copy()
da = results[['date', 'dayanswer']].copy()

k = len(results)

if k < 13:

    # creating
    df_.plot(x='date', y='weather', rot=0, kind='bar', figsize=(8, 6))
    plt.savefig('figures/weather.jpg')
    plt.show()
    wtb.plot(x='date', y='wenttobed', rot=0, kind='bar', figsize=(8, 6))
    plt.savefig('wenttobed.jpg')
    plt.show()
    wu.plot(x='date', y='wokeup', rot=0, kind='bar', figsize=(8, 6))
    plt.savefig('figures/wokeup.jpg')
    plt.show()

        # counting yes/no value in sports category (string)
    sports = sp['sports'].value_counts()
    index = ['Week 1']  # podpisanie kolumny dla indexu
    dg = pd.DataFrame({'yes': sports[0],
                   'no': sports[1]}, index=index)
    ax = dg.plot.bar(rot=0, title='Number of sport activities', figsize=(8, 6))
    plt.savefig('figures/sport.jpg')
    plt.show()
    ci.plot(x='date', y='cigarettes', rot=0, kind='bar', figsize=(8, 6))
    plt.savefig('figures/cigarettes.jpg')
    plt.show()
    alco = al['alcohol'].value_counts()
    index = ['Week 1']
    dg = pd.DataFrame({'yes': alco[0],
                     'no': alco[1]}, index=index)
    ac = dg.plot.bar(rot=0, title='Number of alcohol use', figsize=(8, 6))
    plt.savefig('figures/alcohol.jpg')
    plt.show()
    sa.plot(x='date', y='sleephours', rot=0, kind='bar', figsize=(8, 6))
    plt.savefig('figures/sleepinghours.jpg')
    plt.show()
    df_.plot(x='date', y='weather', rot=0, kind='bar', figsize=(8, 6))
    plt.savefig('figures/weather.jpg')
    plt.show()
    day = da['dayanswer'].value_counts()
    index = ['Week 1']  # podpisanie kolumny dla indexu
    dg = pd.DataFrame({day.index[0]: day[0],
                  day.index[1]: day[1]}, index=index)
    ax = dg.plot.bar(rot=0, title='Number of day answers', figsize=(8, 6))
    plt.savefig('figures/dayanswer.jpg')
    plt.show()

else:

    DF_ = sort_data(df_,'weather')
    ay = DF_.plot.bar(rot=0,title='Weather',xlabel='Weeks',ylabel='Temperature')
    plt.savefig('figures/weather.jpg')
    plt.show()
    WTB = sort_data(wtb, 'wenttobed')
    ax = WTB.plot.bar(rot=0,title='Went to bed',xlabel='Weeks',ylabel='Time')
    plt.savefig('figures/wenttobed.jpg')
    plt.show()
    WU = sort_data(wu, 'wokeup')
    az = WU.plot.bar(rot=0,title='Woke up',xlabel='Weeks',ylabel='Time')
    plt.savefig('figures/wokeup.jpg')
    plt.show()
    SP = sort_data_text(sp,'sports',1)
    ag = SP.plot.bar(rot=0,title='Sports',xlabel='Weeks',ylabel='Quantity')
    plt.savefig('figures/sports.jpg')
    plt.show()
    CI = sort_data(ci,'cigarettes')
    ah = CI.plot.bar(rot=0,title='Cigarettes',xlabel='Weeks',ylabel='Quantity')
    plt.savefig('figures/cigarettes.jpg')
    AL = sort_data_text(al,'alcohol',1)
    aj = AL.plot.bar(rot=0,title='Alcohol',xlabel='Weeks',ylabel='Quantity')
    plt.savefig('figures/alcohol.jpg')
    SA = sort_data(sa,'sleephours')
    ak = SA.plot.bar(rot=0,title='Sleep Hours',xlabel='Weeks',ylabel='Time')
    plt.savefig('figures/sleephours.jpg')
    DA = sort_data_text(da,'dayanswer',3)
    al = DA.plot.bar(rot=0,title='Day answer',xlabel='Weeks',ylabel='Answer')
    plt.savefig('figures/dayanswer.jpg')
    plt.show()




