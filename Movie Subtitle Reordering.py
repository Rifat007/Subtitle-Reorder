def numeric(num):
    #n=int(num)
    if(num>='0' and num<='9'):
        return True
    else:
        return False

def accurate_adding(hr1,hr2,mn1,mn2,sc1,sc2,increment):
    hour=hr1+hr2
    minute=mn1+mn2
    sec=sc1+sc2

    hrr=int(hour)
    mnn=int(minute)
    scc=int(sec)

    scc=scc+increment
    if(scc>=60):
        scc=scc%60
        mnn=mnn+1
        if(mnn>=60):
            mnn=mnn%60
            hrr=hrr+1
    stt="0"+str(hrr)+":"
    if(mnn>=0 and mnn<=9):
        stt=stt+"0"+str(mnn)+":"
    else:
        stt=stt+str(mnn)+":"

    if(scc>=0 and scc<=9):
        stt=stt+"0"+str(scc)
    else:
        stt=stt+str(scc)
    return stt


def accurate_deducting(hr1,hr2,mn1,mn2,sc1,sc2,decrement):
    hour=hr1+hr2
    minute=mn1+mn2
    sec=sc1+sc2

    hrr=int(hour)
    mnn=int(minute)
    scc=int(sec)

    scc=scc-decrement
    if(scc<0):
        scc=scc%60
        mnn=mnn-1
        if(mnn<0):
            mnn=mnn%60
            hrr=hrr-1
    stt="0"+str(hrr)+":"
    if(mnn>=0 and mnn<=9):
        stt=stt+"0"+str(mnn)+":"
    else:
        stt=stt+str(mnn)+":"

    if(scc>=0 and scc<=9):
        stt=stt+"0"+str(scc)
    else:
        stt=stt+str(scc)
    return stt


filepath = 'PARASITE (2019) WEB-DL Bsub by Onubade Onuronon.srt'
newfilepath = 'PARASITE1(2019) WEB-DL Bsub by Onubade Onuronon.srt'
ff=open(newfilepath,mode="w+",encoding="utf-8")
with open(filepath,mode="r", encoding="utf-8") as fp:
   line = fp.readline()
   cnt = 1
   while line:
       #print(line)
       l=len(line)
       c=0
       for i in range(0,l):
           if(line[i]==':' and numeric(line[i-2])==True and numeric(line[i-1])==True):
               c=c+1
               if(c%2==1):
                   hr1=line[i-2]
                   hr2=line[i-1]
                   mn1=line[i+1]
                   mn2=line[i+2]
                   sc1=line[i+4]
                   sc2=line[i+5]
                   #if(numeric(hr1)==True and numeric(hr2)==True):
				   incorrect=hr1+hr2+":"+mn1+mn2+":"+sc1+sc2
				   #print(hr1+hr2+":"+mn1+mn2+":"+sc1+sc2)
				   correct=accurate_deducting(hr1,hr2,mn1,mn2,sc1,sc2,8)
				   new_line=line.replace(incorrect,correct)
				   line=new_line
                       
       ff.write(line)
       line = fp.readline()
       cnt += 1
ff.close()
print("Complete")
