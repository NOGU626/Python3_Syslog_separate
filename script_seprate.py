#!/bin/python3

import shutil
import re,datetime,os
stock = []
save = []
month_dic = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
device_dic = {"C4:DD:0F:4D:E0":"AP1","C4:DD:0F:0D:E0":"AP2","C4:DD:0F:3E:C0":"AP3","C4:DD:16:64:20":"AP4"}
now = datetime.datetime.now()
write_date = now.strftime('%Y-%m-%d')
now = now.strftime('%m-%d')
currnet_dir = os.path.dirname( os.path.abspath(__file__) )
file_path_name = "AirPro_Kan7.log"

with open(currnet_dir +"/"+file_path_name,'r') as f:
    lines = f.readlines()
    for i in lines:
        dateformat = ""
        mess = i.split(" ")
        dic_key = mess[5]
        pla = 0
        if(dic_key == "[50:"):
            dic_key = mess[6]
            pla = 1
        device_mac_address = device_dic[dic_key]
        if(pla ==0):
            dateformat = str(month_dic[mess[0]])+"-"+mess[1]
        else:
            dateformat = str(month_dic[mess[0]])+"-0"+mess[2]
        data = ""
        for i in range(0,len(mess)):
            if(i < len(mess)-1):
                data += mess[i] + " "
            else:
                data += mess[i] + "\n"
        if(now == dateformat):
            save.append({device_mac_address:data})
            stock.append(data)
            
for name in device_dic.values():
    write_data = []
    file = open(currnet_dir +"/"+name+"/"+write_date+"_"+name+".log", 'w')
    for data in save:
        if data.get(name):
            file.write(data.get(name))
    file.close()
        
file = open(currnet_dir +"/"+"backup"+"/"+write_date+"_backup.log", 'a')
for data in stock:
    file.write(data)
file.close()

shutil.copy2(currnet_dir +"/"+file_path_name, currnet_dir +"/bg")

with open(currnet_dir +"/AirPro_Kan7.log",'w') as f:
    f.write("")
            
    
    
