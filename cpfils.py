import os
import sys

from tryouts import *

def openfil(filnm,rwa='r'):
	if rwa=='r':
		retfnm=open(filnm,'r')
	if rwa=='w':
		retfnm=open(filnm,'w')
	if rwa=='a':
		retfnm=open(filnm,'a')
	return retfnm




		
	
nospace()
rundirlister()
filnms=open('files\\filles.txt','r')
nmfil=open('files\\nmfil.txt','r')
for line in filnms.readlines():
	line=line[0:-1]
	flg=True
	for s_line in nmfil:
		s_line=s_line[0:-1]
		if s_line in line:
			flg=False
			renamefiles(line,s_line+'_'+line)
			movefils(s_line+'_'+line)
			updateopenbat(s_line+'_'+line)
	if flg:
		str2out="The File "+line+" had no previous folder name associated, please enter one:"
		s_line=input(str2out)
		renamefiles(line,s_line+'_'+line)
		movefils(s_line+'_'+line)
		updateopenbat(s_line+'_'+line)
		updatenmfil(s_line)
	user_in=input('The file has been copied and openbat updated, would you like to remove the original?:(Y/N)')
	if user_in=='Y':
		removve(line)


