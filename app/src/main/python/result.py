import requests
import bs4
import numpy as np

def main(uid):
    data=[]
    student_data=[]
    student_result=[]
    student_subjects=[]
    student_credits=[]
    student_grades=[]
    extracted_data=[]
    
    url=f"http://202.53.11.226:8080/lastudentportal/online/report/onlineResultNewInner.jsp?registerno={uid}&iden=1"
    res=requests.get(url)
    soup=bs4.BeautifulSoup(res.text,'lxml')

    for i in soup.select("tr td"):
        data.append(i.getText())
    
    gradeValue={'O':10,'A':9,'B':8,'C':7,'D':6,'E':5,'F':0,'-':9}

    head=np.array([7,8,10,11,12])
    add=np.array([7,7,7,7,7])

    try:
        for i in [2,4,6]:
            student_data.append(data[i])
        sem=data[15]
        for i in range((int((len(data)-10)/7))):
            record=[data[head[0]],data[head[1]],data[head[2]],data[head[3]],data[head[4]]]
            student_result.extend([record])
            if sem==data[head[1]]:
                try:
                    if i!=0:
                        student_credits.append(int(data[head[3]]))
                except:
                    student_credits.append(' ')
            for k in gradeValue:
                if data[head[4]] == k:
                    student_grades.append(gradeValue[k])
                    
            head=head+add
    except:
        student_data.append(data[0])   
            
        
