#!/usr/bin/env python3
#Course2_Using Python-to-Interact-with-theOperatingSystem_Week7-QwiklabsAssessmentLogAnalysisUsingRegularExpressions

import re
import sys
import operator
import csv

userInfoDic={}
userErrorDic={}
errorMsgDic={}

errorRegx=r"\w*ERROR ([\w \']*)"
userRegx=r'\(([\w.]*)\)'

logFile='syslog.log'
f=open(logFile)

for line in f.readlines():
  userP=re.compile(userRegx)
  user=userP.search(line)
  if "INFO" in line:
    if user.group(1) in userInfoDic.keys():
      userInfoDic[user.group(1)]+=1
    else:
      userInfoDic[user.group(1)]=1
  elif "ERROR" in line:
    if user.group(1) in userErrorDic.keys():
      userErrorDic[user.group(1)]+=1
    else:
      userErrorDic[user.group(1)]=1
f.close()


x=open(logFile)
for line in x.readlines():
  errorP=re.compile(errorRegx)
  error=errorP.search(line)
  if "INFO" in line:
    continue

  if error.group(1) in errorMsgDic.keys():
    errorMsgDic[error.group(1)]+=1
  else:
    errorMsgDic[error.group(1)]=1
x.close()

def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = [value , dict_1[key]]
       else:
               dict_3[key]=[0,value]
   return dict_3

userInfoError = mergeDictionary(userErrorDic, userInfoDic)


sortedUserInfoError= sorted(userInfoError.items(), key = operator.itemgetter(0))
sortedErrors= sorted(errorMsgDic.items(), key = operator.itemgetter(1), reverse=True)

print(sortedUserInfoError)

with open('error_message.csv', 'w',newline='') as csvfile:
  writer= csv.writer(csvfile, delimiter=',')
  writer.writerow(['Error', 'Count'])
  for err, count in sortedErrors:
    writer.writerow([err, count])

with open('user_statistics.csv', 'w',newline='') as csvfile:
  writer= csv.writer(csvfile, delimiter=',')
  writer.writerow(['Username', 'INFO', 'ERROR'])
  for user in sortedUserInfoError:
    writer.writerow([user[0],user[1][0],user[1][1]])




#print('sortedUsers: ',sortedUsers)
#print('sortedErrors: ',sortedErrors)
