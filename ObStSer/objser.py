#!/usr/bin/python
import os,sys,time,socket

#Socket is Created
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Bind The Socket With Port
s.bind(("",8888))

#data receives Drive Name 
data=s.recvfrom(20)

#device name is stored
d_name=data[0]

#data1 receives Drive Size 
data1=s.recvfrom(20)

#device size is stored
d_size=data1[0]

#Client Address is stored
cli_adr=data[1][0]

#Creating LVM By Name specified by client

os.system('lvcreate --name '+d_name+' --size '+d_size+'M drivevg')

#Format the created LVM 
os.system('mkfs.ext4 /dev/drivevg/'+d_name)

#Create Mount Point
os.system('mkdir /mnt/'+d_name)

#Mount The Drive 
os.system('mount /dev/drivevg/'+d_name+' /mnt/'+d_name)

#Installing nfs-utils for configuration
#os.system('yum install nfs-utils -y')

#Assign variable 'entry' to feed in NFS exports File
entry="/mnt/"+d_name+" "+cli_adr+"(rw,no_root_squash)"

#Feed variable 'entry' in exports file
f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()

#Start NFS Services and making service persistent

#os.system('systemctl restart nfs-server')
#os.system('systemctl enable nfs-server')

check=os.system('exportfs -r')
#print check

if check== 0 :
	s.sendto("Done",data[1])
else:
	print "Check your Code."

