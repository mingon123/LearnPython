import csv, re

#csv형 리스트로 바꾸기 위해 함수 정의
def opencsv(filename,enc):
    f = open(filename,'r',encoding=enc)
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close()
    return output

#csv형 리스트가 저장된 객체를 파일에 쓸 때
def writecsv(filename,enc,the_list):
    #파일명,모드,인코딩
    with open(filename,'w',encoding=enc,newline='') as f:
        a = csv.writer(f,delimiter=',')
        a.writerows(the_list)
    f.close()

#숫자로 변환
def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','',j))
            except:
                pass
    return listName