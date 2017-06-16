#!/usr/bin/python
import os,sys,time,socket

#Server IP Stored In a variable
s_ip="192.168.122.66"
#Port No. Stored In a variable
s_port=8888

#Socket is Created
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Input Drive Name From Client
drive_name=raw_input("Enter Name Of The Storage Drive :")

#Input Drive Size From Client
drive_size=raw_input("Enter Storage Device Size (in MB) :")

#Send Drive Name To Server Side
s.sendto(drive_name,(s_ip,s_port))

#Send Drive Size To Server Side
s.sendto(drive_size,(s_ip,s_port))

#Response is received from server side
res=s.recvfrom(20)

#Check the Response and mount it everything is in order or reject otherwise
if res[0]=="Done" :
	os.system('mkdir /media/'+drive_name)
	os.system('mount '+s_ip+':/mnt/'+drive_name+' /media/'+drive_name)
	
else:
	print "Cloud hasn't responded positively"
 
	

