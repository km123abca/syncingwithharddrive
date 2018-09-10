import os
import sys
#from dummy import *

def openfil(filnm,rwa='r'):
	if rwa=='r':
		retfnm=open(filnm,'r')
	if rwa=='w':
		retfnm=open(filnm,'w')
	if rwa=='a':
		retfnm=open(filnm,'a')
	return retfnm


def filreplace(filein,fileout):
	infil=open(filein,'r')
	oufil=open(fileout,'w+')
	for line in infil.readlines():
		oufil.write(line)
	infil.close()
	oufil.close()

def updateopenbat(filnm):
	ini=filnm[0]
	iniplus=filnm.split('_')[1]
	file_real=open('openbat.bat','r')
	filtemp=open('batfiles\\openbat2.txt','a+')

	uo_filloc=open('movefiles2where.txt','r')
	uo_filloc_x=uo_filloc.readlines()
	uo_filloc.close()
	for line in file_real.readlines():
		if "Enter file choice" in line:
			filtemp.write("echo "+ini+"."+iniplus+"\n")
			filtemp.write(line)
			filtemp.write("if %"+"fil%"+" equ "+ini+" (\n")
			filtemp.write("%"+"SystemRoot%"+"\\explorer.exe "+uo_filloc_x+"\\"+filnm+"\n")
			filtemp.write(")\n")
		else:
			filtemp.write(line)
	file_real.close()
	filtemp.close()
	filreplace('batfiles\\openbat2.txt','openbat.bat')
	os.system('batfiles\\delfile.bat openbat2.txt')


def checkbat():
	try:
		el=os.system('batfiles\\dd.bat')
	except:
		print('error yall')
	finally:
		print('no error yall')
		print(el)

def renamefiles(f,f1):
	ns_folderloc=open('files\\folderloc.txt')
	for line in ns_folderloc.readlines():
		folderloc_z=line
		break
	ns_folderloc.close()
	stat=os.system('ren \"'+folderloc_z+'\\'+f+'\" '+f1)
	if stat==0:
		return True
	else:
		return False

def rundirlister():
	os.system('batfiles\\lister.bat')

def movefils(filnm):
	proc_loc_file=open('files\\movefiles2where.txt','r')
	proc_loc=proc_loc_file.readlines()[0]
	proc_loc_file.close()

	fil2rd=open('files\\folderloc.txt','r')
	loc_mf=proc_loc+'\\'+filnm.split('_')[0]+'\\'
	loc=''
	for line in fil2rd.readlines():
		loc=line
		break
	res=os.system('batfiles\\copyfil.bat '+loc+'\\'+filnm+' '+loc_mf)
	if res==0:
		return True
	else:
		return False

def updatenmfil(loc_s_line):
	fi=open('files\\nmfil.txt','a+')
	fi.write(loc_s_line+'\n')
	fi.close()

def nospace():
	ns_fil=open('files\\filles.txt')
	ns_folderloc=open('files\\folderloc.txt')
	for line in ns_folderloc.readlines():
		folderloc_z=line
		break
	ns_folderloc.close()
	for line in ns_fil.readlines():
		line=line[0:-1]
		line_shorted=line.replace(' ','')
		os.system('ren \"'+folderloc_z+'\\'+line+'\" '+line_shorted)
	ns_fil.close()

def pave(pat):
	count=0
	for elem in pat.split('\\'):
		count+=1
		#print('now'+elem+'count='+str(count))
		
		if count<4:
			continue
		#print('now:'+elem+' count='+str(count)+' entire='+pat.split('\\')[count-1])
		#print('operating'+pat.split('\\')[count])
		os.system("batfiles\\dircreat.bat "+"\\".join(pat.split('\\')[0:count]))



