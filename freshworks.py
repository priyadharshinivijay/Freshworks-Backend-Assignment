#Freshworks Backend Assignment
 	#A file-based key-value data store that supports the basic CRD (create, read and delete) operations 


def timetolive(key):
	from pathlib import Path
	t_file="timelive_store.txt"
	t_path=Path(t_file)
	if t_path.exists():
		ff=open(t_path,"r")
		dd = json.load(ff)
		t=input("Want to include TimeToLive property? (y/n): ")
		if t=='y':
			sc=float(input("Enter TimeToLive in hours: "))
			sec=sc*3600
		else:
			sec=sys.maxsize*3600
		entered_time=time.time()
		tdata=[entered_time,sec]
		dd[key]=tdata
		json_time_object = json.dumps(dd)
		with open(t_path, "w") as outfile:
			outfile.write(json_time_object)
	else:
		ddict={}
		t=input("Want to include TimeToLive property? (y/n): ")
		if t=='y':
			sc=float(input("Enter TimeToLive in hours: "))
			sec=sc*3600
		else:
			sec=sys.maxsize*3600
		entered_time=time.time()
		tdata=[entered_time,sec]
		ddict[key]=tdata
		json_time_object = json.dumps(ddict)
		with open(t_path, "w") as outfile:
			outfile.write(json_time_object)


def create():
	key=input("Enter the patient id: ")
	if(len(key)>32):
		print("Key size exceeded.") #key size when exceeds 32 character.
		return()
	data=dict()
	from pathlib import Path
	file=Path(path)
	if file.exists():
		f=open(path,"r")
		d=json.load(f)
		if(os.path.getsize('data_store.txt')>1e+9):
			print("File limit exceeded.") #file size when exceeds 1GB
			return()
		if key in d:
			print("Error: Patient id already exists. Duplicates not allowed.") #when the user enters existing key
			return()
		n=int(input("Enter the no of attributes: "))
		temp={}
		for i in range(1,n+1):
			s=input("Enter attribute "+str(i) +" and value: ").split()
			temp[s[0]]=s[1]
		d[key]=temp
		json_object = json.dumps(d)
		if(sys.getsizeof(json_object)/1024 >32):
			print("Value size exceeded .") #value of the json object exceeds 16kb.
			return()
		with open(path, "w") as outfile:
			outfile.write(json_object)
		timetolive(key)		
	else:
		n=int(input("Enter no of values: "))
		temp={}
		for i in range(1,n+1):
			s=input("Enter attribute "+ str(i) +" and value: ").split(' ')
			temp[s[0]]=s[1]
		data[key]=temp
		json_object = json.dumps(data)
		with open(path, "a+") as outfile:
			outfile.write(json_object)
		timetolive(key)

def delete():
	from pathlib import Path
	file=Path(path)
	if file.exists():
		f=open(path,"r")
		d=json.load(f)
		key=input("Enter the key :")
		if key in d:
			tp="timelive_store.txt"
			tf=open(tp,"r")
			df=json.load(tf)
			if key in df:
				c_time=time.time()
				if(c_time-df[key][0]>df[key][1]):
					print("Time to live for key been expired")
				else:
					d.pop(key)
					json_object = json.dumps(d)
					with open(path, "w") as outfile:
						outfile.write(json_object)
					print("Key and value been deleted successfully!")
		else:
			print(" Key not found.")
	else:
		print("Datastore empty can't perform delete operation.") # when the datastore is empty without data.

def read():
	from pathlib import Path
	file=Path(path)
	if file.exists():
		f=open(path,"r")
		d=json.load(f)
		key=input("Enter the key :")
		if key in d:
			tp="timelive_store.txt"
			tf=open(tp,"r")
			df=json.load(tf)
			if key in df:
				c_time=time.time()
				if(c_time-df[key][0]>df[key][1]):
					print("Time to live for key been expired")
				else:
					print(d[key])
		else:
			print("Key not found")
	else:
		print("Datastore empty can't perform delete operation.")

def update():
	from pathlib import Path
	file=Path(path)
	if(file.exists()):
		f=open(path,"r")
		d=json.load(f)
		key=input("Enter the key : ")
		if key in d:
			print(d[key])
			s=input("Enter the attribute to be updated" + " and its value: ").split(' ')
			d[key][s[0]]=s[1]
			json_object=json.dumps(d)
			with open(path,"w") as outfile:
				outfile.write(json_object)
			print("Updated !")
			print(d[key])
		else:
			print("Key not found.")



import time
import sys
import json
import os
ch=input("Want to perform operations on a specified path ? (y/n): ")
if(ch=='y'):
	path=input("Enter the path : ")
else:
	path="file_store.txt"
#choice=int(input("Enter the operations to be performed in file store: \n 1.Create \n 2.Read \n 3.Delete\n 4.Update\n"))
#if(choice==1):
#	create(path)
#elif(choice==2):
#	read(path)
#elif(choice==3):
#	delete(path)
#elif(choice==4):
#	update(path)
#else:
#	print("Enter the valid choice")
