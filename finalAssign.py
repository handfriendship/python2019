#-*- coding: cp949 -*-
#-*- coding: utf-8 -*-

import math
import pandas as pd
import folium
import datetime
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

df = pd.read_csv('2019.csv', encoding='CP949')

#print(df['�߻�����Ͻ�'])

#df1 = df.loc[df.�߻�����Ͻ� < 2017010200, ['�߻�����Ͻ�']] #�̰� �̿��ؼ� input���� ���� �޾� �׷��� �׸��� ��밡��
#3plt.plot()

#print(df.�߻�����Ͻ�.str[:4])

#-----------------------------
#input�� ���� ����, �Ϻ�, �ְ���, �ð��� �̷������� �׷����� �׸���
#ó���� switch-case������ '����'vs'�Ϻ�'�׷����� �����ϰ� �Ѵ�
#�ι�°�� ��(1~12)�� �Է¹ް�, ��(��~��)�� �Է¹޴´�

#���� ������(1������ ��������)
#df['D'] = df[str(df.�߻�����Ͻ�)]
#print(df['D'])




#for i in range(len(df_time)) :
#    df_time.columns.values[i] = df_time.columns.values[i] % 100

#df_datelist = df.loc[(round(df.�߻�����Ͻ�/ 10000) <= 2017010000 + i*100 + 24),
#              (round(df.�߻�����Ͻ�/ 10000) >= 2017010000 + i*100), ['�߻���']]
#print(numAcc)
#print(timeAcc)

#print(df_num_time)
#numacc = []
#for i in range(1,32) :
#    numacc.append(df.loc[(df.�߻�����Ͻ� <= 2017010000 + i*100 + 24), ['�߻���']])
#print(numacc)

#df_numacc =
#plt.plot(range[1:32], 'bo-')
#df_temp = df
#df_temp["�߻�����Ͻ�"] = df_temp["�߻�����Ͻ�"] / 10000
#print(df_temp)
print(1)
#print(df_datelist)

def getDayName(a, b) :
    dayString = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return dayString[datetime.date(2017, a, b).weekday()]

def generateWeeklyGraph(x) :
    x = round(x/100)

    week = {'Sun':0, 'Mon':-1, 'Tue':-2, 'Wed':-3, 'Thu':-4, 'Fri':-5, 'Sat':-6}
    weekKor = ['��', '��', 'ȭ', '��', '��', '��', '��']
    numAcc = []
    sumAcc = []
    offset = week[getDayName(round((x%10000)/100), round(x%100))]
    for i in range(offset, offset+7) :
        #numAcc.append(list(df.loc[round(df.�߻�����Ͻ�/ 100) == x1+i, '�߻���'].values))
        sumAcc.append(sum(list(df.loc[round(df.�߻�����Ͻ�/ 100) == x+i, '�߻���'].values)))

    plt.plot(weekKor, sumAcc, 'bo-')
    plt.xlabel('������')
    plt.ylabel('���Ƚ��')
    plt.title('���Ϻ� ���Ƚ��')
    plt.show()

def generateDailyGraph(x) :
    x = round(x/100)
    numAcc = df.loc[round(df.�߻�����Ͻ�/ 100) == x, '�߻���'].values
    timeAcc = df.loc[round(df.�߻�����Ͻ�/ 100) == x, '�߻�����Ͻ�'].values
    hourAcc = [i%100 for i in timeAcc]


    plt.plot(hourAcc, numAcc, 'bo-')
    plt.xlabel('���ð�')
    plt.ylabel('���Ƚ��')
    plt.title('�ð��뺰 ���Ƚ��')
    plt.show()

def generateMap(x) :
    location = {}
    location_arr = []
    location_arr2 = []
    latitude = (df.loc[df.�߻�����Ͻ� == x]['����']).values
    longitude = df.loc[df.�߻�����Ͻ� == x]['�浵'].values
    for i in range(len(latitude)) :
        location[latitude[i]] = longitude[i]
    for i in range(len(latitude)) :
        temp = []
        temp.append(list(location.keys())[i])
        temp.append(list(location.values())[i])
        location_arr.append(temp)

    if(len(location_arr) == 0) :
        print('There is no accident at that time')

    return ;
    #print(location)
    #print(location_arr)

    map_location = folium.Map(location=[list(location.keys())[0],
                list(location.values())[0]], zoom_start=7)

    folium.CircleMarker(location=location_arr[0], radius=100,
                        color='#3186cc', fill_color='#3186cc').add_to(map_location)
    #print('len(location_arr) : ', len(location_arr))
    for i in range(len(location_arr)) :
        folium.Marker(location_arr[i]).add_to(map_location)

    map_location.save('D:\map.html')
    #print(latitude)
    #print(longitude)
    #print(list(location.keys())[0])
    #print(list(location.values())[0])


month = int(input('���� �Է��ϼ���'))
date = int(input('��¥�� �Է��ϼ���'))
hour = int(input('�ð��� �Է��ϼ���'))
time = 2017000000 + month*10000 + date*100 + hour
generateDailyGraph(time)
generateWeeklyGraph(time)
generateMap(time)

