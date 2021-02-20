from sonarqube import *
import json
import os
import re
from os import path
#############################init
init=open("conf.txt")
d_init=json.load(init)
print(d_init)
sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username=str(d_init["sonarqube"]["username"]), password=str(d_init["sonarqube"]["password"]))
issues1 = list(sonar.issues.search_issues(componentKeys=str(d_init["sonarqube"]["project"]), branch=str(d_init["sonarqube"]["branch"])))
################################duplicatekey 1/
'''
sq="python:S1192"
sq1="python:S125"

info="INFO"
val="AXcqnskc-n2LilEsa3ap"

sonar.issues.issue_change_severity(issue=val, severity="CRITICAL")



js=json.dumps(issues1, indent=4, sort_keys=True)
y = json.loads(js)



with open("cache-directory/duplicateKey.json","w") as f:
    for i in range(9724):
        a=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
        x = re.findall(sq, a)
        k= re.findall(sq1,a)
        #print(x)
        if x or k:
            string=(json.dumps(y[i]["key"], indent=4, sort_keys=True))
            reg=string.replace('"','')
            f.write(str(json.dumps(y[i]["key"], indent=4, sort_keys=True))+ "\n")
            sonar.issues.issue_change_severity(issue=reg, severity=info)


'''
##############################retrieve data

js=json.dumps(issues1, indent=4, sort_keys=True)
y = json.loads(js)




with open("cache-directory/data.json","w") as f:
    f.write("["+'\n')
    once=0
    for i in range(9724):
        a=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
        x = re.findall("python", a)
        k = re.findall("python:S1192",a)
        v= re.findall("python:S125",a)



        
        if x and not k and not v:
            data1=str(json.dumps(y[i]["key"], indent=4, sort_keys=True))
            data2=str(json.dumps(y[i]["message"], indent=4, sort_keys=True))
            data3=str(json.dumps(y[i]["type"], indent=4, sort_keys=True))
            

            key=json.dumps(y[i]["component"], indent=4, sort_keys=True)
            key=key.replace('"','')
            key=key.replace("\\u00e9","é")

            
            
            data4_1=(json.dumps(y[i]["textRange"]["endLine"], indent=4, sort_keys=True))
            data4_2=(json.dumps(y[i]["textRange"]["endOffset"], indent=4, sort_keys=True))
            data4_3=(json.dumps(y[i]["textRange"]["startLine"], indent=4, sort_keys=True))
            data4_4=(json.dumps(y[i]["textRange"]["startOffset"], indent=4, sort_keys=True))
            
            data1=data1.replace('"','')
            data2=data2.replace('"','')
            data3=data3.replace('"','')
            data4_1=data4_1.replace('"','')
            data4_2=data4_2.replace('"','')
            data4_3=data4_3.replace('"','')
            data4_4=data4_4.replace('"','')

            #########
            data_r=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
            data_r=data_r.replace('"','')


            ########""

            

            data5= sonar.sources.get_source_code(key=key, from_line=data4_3, to_line=data4_1)
            data5=json.dumps(data5["sources"][0][1])
            data5=data5.replace('"','')
            ######print(data1)
            data5= re.sub('</?span[^>]*>', '', data5)
            
            json_format={"key":data1,"msg":data2,"rule":data_r,"type":data3,"code":[{"endLine":data4_1,"endOffset":data4_2,"startLine":data4_3,"startOffset":data4_4},{"src":data5}]}
            
            if once==0:
                f.write(json.dumps(json_format,indent=4, sort_keys=True) )
                once=1
            else:
                f.write(","+"\n"+json.dumps(json_format,indent=4, sort_keys=True)+ "\n")
    f.write("]")




#tempfile ->fichier temporaire to mongodb
f=open("cache-directory/data.json")
data = json.load(f)
long=len(data)
with open("cache-directory/data.json",'w') as file:
    file.write(json.dumps(data,indent=4, sort_keys=True))


##############################################main sonar



#######################################sonar







js=json.dumps(issues1, indent=4, sort_keys=True)
y = json.loads(js)




'''
with open( "cache-directory/issue.json","w") as f:
    f.write(str(js))

with open( "cache-directory/test.json","w") as f:
    f.write(str(json.dumps(y[0], indent=4, sort_keys=True)))
'''
with open( "cache-directory/search.json","a") as f:
    for i in range(9724):
        a=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
        x = re.findall("python", a)
        if (x):
            f.write(str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))+ "\n")

        
       
        


print(10*"==")

########################################################""outprocess

file = open("cache-directory/search.json","r") 
Counter = 0
  
# Reading from file 
Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1
          
print("This is the number of lines in the file") 
print(Counter) 


#############################
sq="python:S1192"
sq1="python:S125"

info="INFO"





js=json.dumps(issues1, indent=4, sort_keys=True)
y = json.loads(js)

##################


with open("cache-directory/allKey.json","w") as f:
    for i in range(9724):
        a=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
        x = re.findall("python", a)
        if (x):
            f.write(str(json.dumps(y[i]["key"], indent=4, sort_keys=True))+ "\n")


######################
file = open("cache-directory/allKey.json","r") 
Counter = 0


Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1
        
print("This is the number of lines in the file") 
print(Counter) 



########################


with open("cache-directory/sortKey.json","w") as f:
    for i in range(9724):
        a=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
        val = re.findall("python", a)
        x = re.findall(sq, a)
        k=re.findall(sq1, a)
        #print(x)
        if val and not x and not k:
            f.write(str(json.dumps(y[i]["key"], indent=4, sort_keys=True))+ "\n")
############################

f=open("cache-directory/data.json")
data = json.load(f)





###############
rule=[]


for y in range(len(data)):

    k=(data[y]["rule"])
    rule.append(k)
    rule=list(dict.fromkeys(rule))

taille=[]
count=0
number=[]


with open("cache-directory/sortdata.json",'w') as f:
    test=[]
    test2=[]
    json_dict = {}
    
    for i in rule:

        u=i

        
        pls=[]

        for j in range(len(data)):

            a=str(json.dumps(data[j]["rule"], indent=4, sort_keys=True))
            x = re.findall(i, a)
           
            

            if x:
                data1=str((data[j]["code"][1]["src"]))

                pls.append(data1)

                pls=list(dict.fromkeys(pls))

            
        test.append(pls)
    for i in range(len(test)):
        ###print(i)
        tmp_dict = {}
        #f.write("==========================" + rule[i] + '\n')
        for j in range(len(test[i])):
            ###print(test[i][j])
            ###f.write(test[i][j]+ '\n')
            tmp_dict["data"] = [{"src": test[i][j]} for j in range(len(test[i]))]
        json_dict[str(rule[i])] = tmp_dict
    f.write(json.dumps(json_dict, indent=4, sort_keys=True))    