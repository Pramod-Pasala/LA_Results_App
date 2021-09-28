import requests
import bs4
import numpy as np

def main(uid):
    url=f"http://202.53.11.226:8080/lastudentportal/online/report/onlineResultNewInner.jsp?registerno={int(uid)}&iden=1"
    res=requests.get(url) 
    soup=bs4.BeautifulSoup(res.text,"lxml") 
    
    data=[] 
    for i in soup.select("tr td"): 
        data.append(i.getText()) 
    
    data_1=[] 
    data_2=[] 
    credits=[] 
    grade_points=[] 
    
    gradeValue={'O':10,'A':9,'B':8,'C':7,'D':6,'E':5,'F':0,'-':9} 
    head=np.array([7,8,10,11,12]) 
    add=np.array([7,7,7,7,7]) 
    
    try:
        for i in [2,4,6]:
            data_1.append(data[i]) 
        sem=data[15] 
        for i in range((int((len(data)-10)/7))):
            
            record=[data[head[0]],data[head[1]],data[head[2]],data[head[3]],data[head[4]]]
            data_2.extend([record]) 
            
            if sem==data[head[1]]: 
                try:
                    if i!=0: 
                        credits.append(int(data[head[3]]))
                except: 
                    credits.append(' ')
                    
            for k in gradeValue:
                if data[head[4]] == k:
                    grade_points.append(gradeValue[k])
                
            head=head+add 
            
        return [data_1,data_2,credits,grade_points]
    
    except:
        data_1.append(data[0])
        
        return [data_1]
    
    


                
def studentInfo(data):

    if len(data[0])==3:
        #if the student info is present in data it is diplayed
        resultDisplay(data[1])
        
        calculateGPA(data[2],data[3])
        
    else:
        #if student info not present display message
    
def resultDisplay(result):

    pass

    # method to display student result in the form of table
    
    
            
                
                
def calculateGPA(credits,grade_points): 
    
    credits=np.array(credits) 
    grade_points=np.array(grade_points) 
     

    