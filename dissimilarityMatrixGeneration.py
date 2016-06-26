import csv

#generate a dissimilarity matrix and save the calculated pairwise value into a csv file


with open('C:/Users/tejus/Downloads/all_data_20160217.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
import pandas as pd
df=pd.read_csv('C:/Users/tejus/Downloads/all_data_20160217.csv', sep=',')

maximums_columns = np.max(df, axis=0)
Dl_range=maximums_columns['Step.length.in.mm']
Ds_range=maximums_columns['Speed.in.mm.per.sec']

import math
def dist(dta,i,j):
   Dis_angle=math.sin(math.pi*abs(dta.loc[i,'Angle.between.2.step.lengths']-dta.loc[j,'Angle.between.2.step.lengths'])/360)**2
   Dis_length=abs(dta.loc[i,'Step.length.in.mm']-dta.loc[j,'Step.length.in.mm'])/Dl_range
   Dis_speed=abs(dta.loc[i,'Speed.in.mm.per.sec']-dta.loc[j,'Speed.in.mm.per.sec'])/Ds_range
   return (1-1/(1+Dis_angle+Dis_speed+Dis_length))

dt=df[['Angle.between.2.step.lengths','Step.length.in.mm', 'Speed.in.mm.per.sec']]# take certain columns from a dataframe

lst=df['v_name'].tolist()
import csv
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(lst)

for i in range (0, 34828):
    new=[]
    for j in range(0,i):
        new.append(dist(dt,i,j))
    with open("output.csv", "a") as fd:
        writer = csv.writer(fd)
        writer.writerow(new)



    


