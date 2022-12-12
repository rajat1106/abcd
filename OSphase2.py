import random
ifile=open("Operating-System-Course-Project-main\\input2.txt", 'r')
ofile=open("Operating-System-Course-Project-main\\output2.txt", 'w')
ip=ifile.read()
error={0:'NO ERROR',1:'OUT OF DATA',2:'LINE LIMIT EXCEEDED',3:'Time Limit Exceeded',4:'Operation Code Error',5:'Operand Error',6:'Invalid Page Fault',7:'TIME LIMIT EXCEEDED And OPERAND ERROR',8:'TIME LIMIT EXCEEDED And OPERATION CODE ERROR'}
SI=0
TI=0
LLC=0
IC=0
M=[]
IC=0
RA=0
choose=[i for i in range(29)]
TTC=0
IR=0
TLL=0
JID=0
lst=[]
TTL=0
PTR=-1
gdc=0
PI=0
def READ():
    global lst
    global gdc
    global PTR
    global RA
    global M
    global TTC
    count=0
    #TTC+=1
    if TTC>TTL:
        TERMINATE(3)
    if lst[gdc][0]=='$END':
        TERMINATE(1)
    else:
        k=RA
        #print(lst)
        for i in lst[gdc]:
            count=count+1
            if(count>=10):
                print("Data is greater than a block")
            mp=list(i)
            while len(mp)!=4:
                mp.append(' ')
            i=''.join(mp)
            M[k]=i
            k+=1
        gdc+=1
        TTC+=1

def WRITE():
    global LLC
    global TLL
    global M
    global RA
    global PI
    LLC+=1
    if LLC>TLL:
        TERMINATE(2)
    else:
        try:
            ofile.write(''.join(M[RA:RA+M[RA:].index(None)])+'\n')
        except:
            TERMINATE(6)
def TERMINATE(EM):
    global M
    global IC
    global JID
    global IC
    global IR
    global TTC
    global LLC
    global TTL
    global TLL
    ofile.write(' '+error[EM].upper()+'\n')
    ofile.write('JOB ID:'+str(JID)+' ')
    ofile.write(' '+error[EM].upper()+' ')
    ofile.write('IC:'+str(IC)+' ')
    ofile.write('IR:'+str(IR)+'\n')
    ofile.write('TTL:'+str(TTL)+' ')
    ofile.write('TTC:'+str(TTC)+' ')
    ofile.write('TLL:'+str(TLL)+' ')
    ofile.write('LLC:'+str(LLC)+' ')
    ofile.write('\n\n')
    printMem()
    print("\n---------------------------Program Ended----------------------------\n")
    STARTEXECUTION()
    
def ALLOCATE():
    global choose
    k=random.choice(choose)
    choose.remove(k)
    return k
def printMem():
    global M
    global PTR
    #print("\n---------------------------Page Table----------------------------\n\n")
    # for i in range(M[int(PTR)],M[int(PTR)+10]):
    #     print(i, M[i],end ="    ")
    #print("\n----------------------Program and Data-----------------------\n\n")
    # for i in range(M[int(PTR)],M[int(PTR)+10]):
    #     if M[i]!=None:
    #         for j in range(M[i],M[i]+10):
    #             if M[j]!=None:
    #                 print(j,M[j],end ="    ")
    #         print()
    print("                                                         Memory")
    print()
    for i in range(len(M)):
        if(i<9):
            print(" ", "00"+ str(i), M[i], " ",end ="    ")
        elif(i < 99):
            print(" ", "0"+ str(i), M[i], " ",end ="    ")
        else :
            print(" ", str(i), M[i], " ",end ="    ")
    
    print()
def MOS():
    global SI
    global TI
    global PI
    if TI==2:
        if SI==1:
            TERMINATE(3)
        elif SI==2:
            WRITE()
            TERMINATE(3)
        elif SI==3:
            TERMINATE(0)
        elif PI==1:
            TERMINATE(3+5)
        elif PI==2:
            TERMINATE(3+4)
        elif PI==3:
            TERMINATE(3)
        else:
            TERMINATE(3)
    elif TI==0:
        if SI==1:
            READ()
        elif SI==2:
            WRITE()
        elif SI==3:
            TERMINATE(0)
        elif PI==1:
            TERMINATE(4)
        elif PI==2:
            TERMINATE(5)
        elif PI==3:
            TERMINATE(6)
    SI=0
    TI=0
    PI=0
def LOAD():
    global ip
    global SI
    global PI
    global TI
    global lst
    global M
    global LLC
    global JID
    global gdc
    global TLL
    global TTL
    global PTR
    global choose
    choose=[i for i in range(29)]
    SI=0
    PI=0
    TI=0
    LLC=0
    TLC=0
    M=[None for i in range(300)]
    end=ip.find('$END')
    lst=ip[:end+8].split('\n')
    ip=ip[end+9:]
    lst=[[s[i:i+4] for i in range(0,len(s),4)] for s in lst]
    
    # try:
    #     k=len(lst[1][2])
    #     k= k/10 + 1
    # except:
    #     pass


    listtemp=[]
    listtemp2=[]
    i1=0
    i=0
    if(len(lst[0])==0):
        exit()
    if(len(lst[1]) > 10):
        while(i<len(lst[1])):
            while(i1<=9 and i< len(lst[1])):
                listtemp.append(lst[1][i])
                i1+=1
                i+=1
            #print(listtemp)
            listtemp2.append(listtemp)
            listtemp=[]
            i1=0
        lst.pop(1)
        o=1
        for i in listtemp2:
            lst.insert(o,i)
            o+=1
    else :
        pass
   
    print("\n---------------------------Program Started----------------------------\n")
    print(lst)
    try:
        if(lst[0][0]) == "$AMJ":
            try:
                JID=int(lst[0][1])
            except:
                return
            TTL=int(lst[0][2])
            TLL=int(lst[0][3])
            PTR=ALLOCATE()*10
            print("TTL: ",TTL," TLL: ",TLL)
            print("PTR: ",PTR)
            for i in range(len(lst)):
                if lst[i][0]=='$DTA':
                    gdc=i+1
            k=1
            page=ALLOCATE()
            p=page*10
            pte=PTR
            while(lst[k][0]!='$DTA'):
                for i in lst[k]:

                    M[p]=i
                    p+=1
                if page<=9:
                    M[pte]='000'+str(page)
                else:
                    M[pte]='00' +str(page)
                try:
                    choose.remove(pte//10)
                    # print(choose)
                    # print(pte)
                except:
                    pass
                k+=1
                pte+=1
                page+=1
                
            data_card=[]
            while(lst[k][0]!='$END'):
                data_card.append(lst[k])
                k+=1
        else:
            print("AMJ not encountered")
    except:
        pass
def STARTEXECUTION():
    global M
    global JID
    M=[None for i in range(300)]
    global IC
    IC=0
    LOAD()
    EXECUTEUSERPROGRAM()
def ADDRESSMAP(VA): #for converting logical address into real address
    global PTR
    global M
    global PI
    k=VA//10#(10 is page size)
    rem=VA%10
    if(0 <= int(VA) >= 99):
        PI = 2
       
    if type(VA)==int:
        try:
            fr=int(M[PTR+k][2:])
            RA=fr*10+rem
            return RA
        except:
            PI=3
    else:
        PI=2 #operand error
def EXECUTEUSERPROGRAM():
    global PTR
    global R
    global IC
    global SI
    global IR
    global PI
    global TTL
    global TI
    global C
    global TTC
    global LLC
    TTC=0
    global M
    global RA
    RA=ADDRESSMAP(IC)
    
    if PI != 0:
        exit()
    try:
        IR=M[RA]
    except:
        exit()

    while(IR!=None):
        print("----------Round ",IC," ----------- ")
        print()
        print("IC: ",IC," RA: ",RA," IR: ",IR)
        IC+=1
        if IR[:2]=='LR':
            TTC+=1
            
            try:
                RA=ADDRESSMAP(int(IR[2:]))
                if RA is None:
                    PI=3
                else:
                    R=M[RA]
            except:
                PI=2

        elif IR[:2]=='SR':
            try:
                if M[PTR+int(IR[2:])//10]!=None:
                    RA=ADDRESSMAP(int(IR[2:]))
                else:
                    page=ALLOCATE()
                    TTC+=1
                    RA=page*10
                    if page<=9:
                        M[PTR+int(IR[2:])//10]='000'+str(page)
                    else:
                        M[PTR+int(IR[2:])//10]='00' +str(page)
                    M[RA+int(IR[2:])%10]=R
                M[RA]=R
                print("RA for SR : ",RA)
            except:
                PI=2
            TTC+=1
            #printMem(M)
        elif IR[:2]=='CR':
            try:
                RA=ADDRESSMAP(int(IR[2:]))
                if R==M[RA]:
                    C=True
                else:
                    C=False
            except:
                PI=2
            TTC+=1
        elif IR[:2]=='BT':
        
            if C==True:
                if type(IR[2:])==int:
                    PI=3
                else:
                    IC=int(IR[2:])
                
            else:
                pass


            TTC+=1
        elif IR[:2]=='GD':
            
            try:
                SI=1
                page=ALLOCATE()
                RA=page*10
                if page<=9:
                    M[PTR+int(IR[2:])//10]='000'+str(page)
                else:
                    M[PTR+int(IR[2:])//10]='00' +str(page)
                
                print("RA for GD : ",RA)
                TTC+=1
            except:
                PI = 2
                SI = 0
        elif IR[:2]=='PD':
            
            try:

                RA=ADDRESSMAP(int(IR[2:]))
                
                SI=2
                
                if RA is None:
                    PI=3
                print("RA for PD : ",RA)

            except:
                PI=3
        elif IR=='H':
            SI=3
            TTC+=1
        else:
            PI=1 #opcode error
            

        if TTC>=TTL and IR!='H':
            TI=2

        if SI!=0:
            print("SI: ",SI)
        if PI!=0:
            print("PI: ",PI)
        if TI!=0:
            print("TI: ",TI)
        if SI!=0 or PI!=0 or TI!=0:
            MOS()


        RA=ADDRESSMAP(IC)
        
        if RA is not None:
            IR=M[RA]
        print("TTC: ",TTC,"LLC: ",LLC)
STARTEXECUTION()

# import random
# ifile=open("input2.txt", 'r')
# ofile=open("outputx2.txt", 'w')
# ip=ifile.read()
# error={0:'NO ERROR',1:'OUT OF DATA',2:'LINE LIMIT EXCEEDED',3:'Time Limit Exceeded',4:'Operation Code Error',5:'Operand Error',6:'Invalid Page Fault',7:'TIME LIMIT EXCEEDED And OPERAND ERROR',8:'TIME LIMIT EXCEEDED And OPERATION CODE ERROR'}
# SI=0
# TI=0
# LLC=0
# IC=0
# M=[]
# IC=0
# RA=0
# choose=[i for i in range(29)]
# TTC=0
# IR=0
# TLL=0
# JID=0
# lst=[]
# TTL=0
# PTR=-1
# gdc=0
# PI=0
# def READ():
#     global lst
#     global gdc
#     global PTR
#     global RA
#     global M
#     global TTC
#     j=0
#     #TTC+=1
#     if TTC>TTL:
#         TERMINATE(3)
#     if lst[gdc][0]=='$END':
#         TERMINATE(1)
#     else:
#         k=RA
#         for i in lst[gdc]:
#             j=j+1
#             if(j>=10):
#                 print("Data too long")
#             mp=list(i)
#             while len(mp)!=4:
#                 mp.append(' ')
#             i=''.join(mp)
#             M[k]=i
#             k+=1
#         gdc+=1

# def WRITE():
#     global LLC
#     global TLL
#     global M
#     global RA
#     global PI
#     LLC+=1
#     if LLC>TLL:
#         TERMINATE(2)
#     else:
#         try:
#             ofile.write(''.join(M[RA:RA+M[RA:].index(None)])+'\n')
#         except:
#             TERMINATE(6)
# def TERMINATE(EM):
#     global M
#     global IC
#     global JID
#     global IC
#     global IR
#     global TTC
#     global LLC
#     global TTL
#     global TLL
#     ofile.write(' '+error[EM].upper()+'\n')
#     ofile.write('JOB ID:'+str(JID)+' ')
#     ofile.write(' '+error[EM].upper()+' ')
#     ofile.write('IC:'+str(IC)+' ')
#     ofile.write('IR:'+str(IR)+'\n')
#     ofile.write('TTL:'+str(TTL)+' ')
#     ofile.write('TTC:'+str(TTC)+' ')
#     ofile.write('TLL:'+str(TLL)+' ')
#     ofile.write('LLC:'+str(LLC)+' ')
#     ofile.write('\n\n')
#     printMem(M)
    
#     print("\n---------------------------Program Ended----------------------------\n")
    
#     STARTEXECUTION()
    
# def ALLOCATE():
#     global choose
#     k=random.choice(choose)
#     choose.remove(k)
#     return k
# def printMem(memory):
#     print("\n---------------------------Memory----------------------------\n\n")
#     for i in range(len(memory)):
#         print("(", i, memory[i], ")",end ="    ")
# def MOS():
#     global SI
#     global TI
#     global PI
#     if TI==2:
#         if SI==1:
#             TERMINATE(3)
#         elif SI==2:
#             WRITE()
#             TERMINATE(3)
#         elif SI==3:
#             TERMINATE(0)
#         elif PI==1:
#             TERMINATE(3+5)
#         elif PI==2:
#             TERMINATE(3+4)
#         elif PI==3:
#             TERMINATE(3)
#         else:
#             TERMINATE(3)
#     elif TI==0:
#         if SI==1:
#             READ()
#         elif SI==2:
#             WRITE()
#         elif SI==3:
#             TERMINATE(0)
#         elif PI==1:
#             TERMINATE(4)
#         elif PI==2:
#             TERMINATE(5)
#         elif PI==3:
#             TERMINATE(6)
#     SI=0
#     TI=0
#     PI=0
# def LOAD():
#     global ip
#     global SI
#     global PI
#     global TI
#     global lst
#     global M
#     global LLC
#     global JID
#     global gdc
#     global TLL
#     global TTL
#     global PTR
#     global choose
#     choose=[i for i in range(29)]
#     SI=0
#     PI=0
#     TI=0
#     LLC=0
#     TLC=0
#     M=[None for i in range(300)]
#     end=ip.find('$END')
#     lst=ip[:end+8].split('\n')
#     ip=ip[end+9:]
#     lst=[[s[i:i+4] for i in range(0,len(s),4)] for s in lst]
    
#     # try:
#     #     k=len(lst[1][2])
#     #     k= k/10 + 1
#     # except:
#     #     pass


#     listtemp=[]
#     listtemp2=[]
#     i1=0
#     i=0
#     if(len(lst[0])==0):
#         exit()
#     if(len(lst[1]) > 10):
#         while(i<len(lst[1])):
#             while(i1<=9 and i< len(lst[1])):
#                 listtemp.append(lst[1][i])
#                 i1+=1
#                 i+=1
#             #print(listtemp)
#             listtemp2.append(listtemp)
#             listtemp=[]
#             i1=0
#         lst.pop(1)
#         o=1
#         for i in listtemp2 :
#             lst.insert(o,i)
#             o+=1
#     else :
#         pass
   
#     print("\n---------------------------Program Started----------------------------\n")
#     print(lst)
#     try:
#         if(lst[0][0]) == "$AMJ":
#             try:
#                 JID=int(lst[0][1])
#             except:
#                 return
#             TTL=int(lst[0][2])
#             TLL=int(lst[0][3])
#             PTR=ALLOCATE()*10

#             for i in range(len(lst)):
#                 if lst[i][0]=='$DTA':
#                     gdc=i+1
#             k=1
#             page=ALLOCATE()
#             p=page*10
#             pte=PTR
#             while(lst[k][0]!='$DTA'):
#                 for i in lst[k]:

#                     M[p]=i
#                     p+=1
#                 if page<=9:
#                     M[pte]='000'+str(page)
#                 else:
#                     M[pte]='00' +str(page)
#                 try:
#                     choose.remove(pte//10)
#                     # print(choose)
#                     # print(pte)
#                 except:
#                     pass
#                 k+=1
#                 pte+=1
#                 page+=1
                
#             data_card=[]
#             while(lst[k][0]!='$END'):
#                 data_card.append(lst[k])
#                 k+=1
#         else:
#             print("AMJ not encountered")
#     except:
#         pass
# def STARTEXECUTION():
#     global M
#     global JID
#     M=[None for i in range(300)]
#     global IC
#     IC=0
#     LOAD()
#     EXECUTEUSERPROGRAM()
# def ADDRESSMAP(IC): #for converting logical address into real address
#     global PTR
#     global M
#     global PI
#     k=IC//10#(10 is page size)
#     rem=IC%10
#     if(0 <= int(IC) >= 99):
#         PI = 2
       
#     if type(IC)==int:
#         try:
#             fr=int(M[PTR+k][2:])
#             RA=fr*10+rem
#             return RA
#         except:
#             PI=3
#     else:
#         PI=2 #operand error
# def EXECUTEUSERPROGRAM():
#     global PTR
#     global R
#     global IC
#     global SI
#     global IR
#     global PI
#     global TTL
#     global TI
#     global C
#     global TTC
#     TTC=0
#     global M
#     global RA
#     RA=ADDRESSMAP(IC)
#     print("RA :",RA,"  PTR :",PTR);
    
#     if PI != 0:
#         exit()
#     try:
#         IR=M[RA]
#     except:
#         exit()
#     while(IR!=None):
#         IC+=1
#         if IR[:2]=='LR':
#             TTC+=1
#             RA=ADDRESSMAP(int(IR[2:]))
#             try:
#                 R=M[RA]
#             except:
#                 pass

#         elif IR[:2]=='SR':
#             try:
#                 if M[PTR+int(IR[2:])//10]!=None:
#                     RA=ADDRESSMAP(int(IR[2:]))
#                 else:
#                     page=ALLOCATE()
#                     TTC+=1
#                     RA=page*10
#                     if page<=9:
#                         M[PTR+int(IR[2:])//10]='000'+str(page)
#                     else:
#                         M[PTR+int(IR[2:])//10]='00' +str(page)
#                     M[RA+int(IR[2:])%10]=R
#                 M[RA]=R
#             except:
#                 PI=2
#             TTC+=1
#             #printMem(M)
#         elif IR[:2]=='CR':
#             RA=ADDRESSMAP(int(IR[2:]))
#             if R==M[RA]:
#                 C=True
#             else:
#                 C=False
#             TTC+=1
#         elif IR[:2]=='BT':
#             if C==True:
#                 IC=int(IR[2:])
#             else:
#                 pass
#             TTC+=1
#         elif IR[:2]=='GD':
#             TTC+=2
#             try:
#                 SI=1
#                 page=ALLOCATE()
#                 RA=page*10
#                 if page<=9:
#                     M[PTR+int(IR[2:])//10]='000'+str(page)
#                 else:
#                     M[PTR+int(IR[2:])//10]='00' +str(page)
                
#                # print("IR:",int(IR[2:]))
#             except:
#                 PI = 2
#                 SI = 0
#         elif IR[:2]=='PD':
#             TTC+=1
#             try:

#                 RA=ADDRESSMAP(int(IR[2:]))
                
#                 SI=2
#                 if RA is None:
#                     PI=3
#             except:
#                 PI=3
#         elif IR=='H':
#             SI=3
#             TTC+=1
#         else:
#             PI=1 #opcode error
#             TTC+=1
#         if TTC>TTL:
#             TI=2
        
#         if SI!=0 or PI!=0 or TI!=0:
#             MOS()

#         RA=ADDRESSMAP(IC)
        
#         if RA is not None:
#             IR=M[RA]
           
        
# STARTEXECUTION()
# # import random
# # ifile=open("input2.txt", 'r')
# # ofile=open("outputx2.txt", 'w')
# # ip=ifile.read()
# # error={0:'NO ERROR',1:'OUT OF DATA',2:'LINE LIMIT EXCEEDED',3:'Time Limit Exceeded',4:'Operation Code Error',5:'Operand Error',6:'Invalid Page Fault',7:'TIME LIMIT EXCEEDED And OPERAND ERROR',8:'TIME LIMIT EXCEEDED And OPERATION CODE ERROR'}
# # SI=0
# # TI=0
# # LLC=0
# # IC=0
# # M=[]
# # IC=0
# # RA=0
# # choose=[i for i in range(29)]
# # TTC=0
# # IR=0
# # TLL=0
# # JID=0
# # lst=[]
# # TTL=0
# # PTR=-1
# # gdc=0
# # PI=0
# # def READ():
# #     global lst
# #     global gdc
# #     global PTR
# #     global RA
# #     global M
# #     global TTC
# #     j=0
# #     if lst[gdc][0]=='$END':
# #         TERMINATE(1)
# #     else:
# #         k=RA
# #         for i in lst[gdc]:
# #             j=j+1
# #             if(j>=10):
# #                 print("Data too long")
# #             mp=list(i)
# #             while len(mp)!=4:
# #                 mp.append(' ')
# #             i=''.join(mp)
# #             M[k]=i
# #             k+=1
# #         gdc+=1
# #     TTC+=1
# # def WRITE():
# #     global LLC
# #     global TLL
# #     global M
# #     global RA
# #     global PI
# #     LLC+=1
# #     if LLC>TLL:
# #         TERMINATE(2)
# #     else:
# #         try:
# #             ofile.write(''.join(M[RA:RA+M[RA:].index(None)])+'\n')
# #         except:
# #             TERMINATE(6)
# # def TERMINATE(EM):
# #     global M
# #     global IC
# #     global JID
# #     global IC
# #     global IR
# #     global TTC
# #     global LLC
# #     global TTL
# #     global TLL
# #     ofile.write(' '+error[EM].upper()+'\n')
# #     ofile.write('JOB ID:'+str(JID)+' ')
# #     ofile.write(' '+error[EM].upper()+' ')
# #     ofile.write('IC:'+str(IC)+' ')
# #     ofile.write('IR:'+str(IR)+' ')
# #     ofile.write('TTC:'+str(TTC)+' ')
# #     ofile.write('LLC:'+str(LLC)+' ')
# #     ofile.write('TLL:'+str(TLL)+' ')
# #     ofile.write('TTL:'+str(TTL)+'\n')
# #     ofile.write('\n\n')
# #     printMem(M)
# #     STARTEXECUTION()
# # def ALLOCATE():
# #     global choose
# #     k=random.choice(choose)
# #     choose.remove(k)
# #     return k
# # def printMem(memory):
# #     print(memory)
# #     print()
# #     # for i in range(len(memory)):
# #     #     print(i, memory[i])
# # def MOS():
# #     global SI
# #     global TI
# #     global PI
# #     if TI==2:
# #         if SI==1:
# #             TERMINATE(3)
# #         elif SI==2:
# #             WRITE()
# #             TERMINATE(3)
# #         elif SI==3:
# #             TERMINATE(0)
# #         elif PI==1:
# #             TERMINATE(3+5)
# #         elif PI==2:
# #             TERMINATE(3+4)
# #         elif PI==3:
# #             TERMINATE(3)
# #         else:
# #             TERMINATE(3)
# #     elif TI==0:
# #         if SI==1:
# #             READ()
# #         elif SI==2:
# #             WRITE()
# #         elif SI==3:
# #             TERMINATE(0)
# #         elif PI==1:
# #             TERMINATE(4)
# #         elif PI==2:
# #             TERMINATE(5)
# #         elif PI==3:
# #             TERMINATE(6)
# #     SI=0
# #     TI=0
# #     PI=0
# # def LOAD():
# #     global ip
# #     global SI
# #     global PI
# #     global TI
# #     global lst
# #     global M
# #     global LLC
# #     global JID
# #     global gdc
# #     global TLL
# #     global TTL
# #     global PTR
# #     global choose
# #     choose=[i for i in range(29)]
# #     SI=0
# #     PI=0
# #     TI=0
# #     LLC=0
# #     TLC=0
# #     M=[0 for i in range(300)]
# #     end=ip.find('$END')
# #     lst=ip[:end+8].split('\n')
# #     print(lst)
# #     ip=ip[end+9:]
# #     lst=[[s[i:i+4] for i in range(0,len(s),4)] for s in lst]
# #     print(lst)
# #     listtemp=[]
# #     listtemp2=[]
# #     i1=0
# #     i=0
# #     print(len(lst[1]))
# #     if(len(lst[1]) > 10):
# #         while(i<len(lst[1])):
# #             while(i1<=9 and i< len(lst[1])):
# #                 listtemp.append(lst[1][i])
# #                 i1+=1
# #                 i+=1
# #             #print(listtemp)
# #             listtemp2.append(listtemp)
# #             listtemp=[]
# #             i1=0
# #         lst.pop(1)
# #         o=1
# #         for i in listtemp2 :
# #             lst.insert(o,i)
# #             o+=1
# #     else :
# #         pass

# #     print(lst)
# #     try:
# #         if(lst[0][0]) == "$AMJ":
# #             try:
# #                 JID=int(lst[0][1])
# #                 TTL=int(lst[0][2])
# #                 TLL=int(lst[0][3])
# #             except:
# #                 return

# #             PTR=ALLOCATE()*10
# #             for i in range(len(lst)):
# #                 if lst[i][0]=='$DTA':
# #                     gdc=i+1
# #             k=1
# #             while(lst[k][0]!='$DTA'):
# #                 page=ALLOCATE()
# #                 p=page*10
# #                 lim=p+10
# #                 for i in lst[k]:
# #                     M[p]=i
# #                     p+=1
                   
# #                 if page<=9:
# #                     M[PTR]='000'+str(page)
# #                 else:
# #                     M[PTR]='00' +str(page)
# #                 k+=1
# #             data_card=[]
# #             while(lst[k][0]!='$END'):
# #                 data_card.append(lst[k])
# #                 k+=1
# #         else:
# #             print("AMJ not encountered")
# #     except:
# #         pass
# # def STARTEXECUTION():
# #     global M
# #     global JID
# #     M=[None for i in range(300)]
# #     global IC
# #     IC=0
# #     LOAD()
# #     EXECUTEUSERPROGRAM()
# # def ADDRESSMAP(IC): #for converting logical address into real address
# #     global PTR
# #     global M
# #     global PI
# #     k=IC//10#(10 is page size)
# #     rem=IC%10
# #     if(0 <= int(IC) >= 99):
# #         PI = 2
# #     if type(IC)==int:
# #         try:
# #             fr=int(M[PTR+k][2:])
# #             RA=fr*10+rem
# #             return RA
# #         except:
# #             PI=3
# #     else:
# #         PI=2 #operand error
# # def EXECUTEUSERPROGRAM():
# #     global PTR
# #     global R
# #     global IC
# #     global SI
# #     global IR
# #     global PI
# #     global TTL
# #     global TI
# #     global C
# #     global TTC
# #     TTC=0
# #     global M
# #     global RA
# #     RA=ADDRESSMAP(IC)
# #     if PI != 0:
# #         exit()
# #     try:
# #         IR=M[RA]
# #     except:
# #         exit()
# #     while(IR!=None):
# #         IC+=1
# #         if IR[:2]=='LR':
# #             TTC+=1
# #             RA=ADDRESSMAP(int(IR[2:]))
# #             try:
# #                 R=M[RA]
# #             except:
# #                 pass
# #         elif IR[:2]=='SR':
# #             try:
# #                 if M[PTR+int(IR[2:])//10]!=None:
# #                     RA=ADDRESSMAP(int(IR[2:]))
# #                 else:
# #                     page=ALLOCATE()
# #                     TTC+=1
# #                     RA=page*10
# #                     if page<=9:
# #                         M[PTR+int(IR[2:])//10]='100'+str(page)
# #                     else:
# #                         M[PTR+int(IR[2:])//10]='10' +str(page)
# #                 M[RA+int(IR[2:])%10]=R
# #             except:
# #                 PI=2
# #             TTC+=1
# #         elif IR[:2]=='CR':
# #             RA=ADDRESSMAP(int(IR[2:]))
# #             if R==M[RA]:
# #                 C=True
# #             else:
# #                 C=False
# #             TTC+=1
# #         elif IR[:2]=='BT':
# #             if C==True:
# #                 IC=int(IR[2:])
# #             else:
# #                 pass
# #             TTC+=1
# #         elif IR[:2]=='GD':
# #             try:
# #                 SI=1
# #                 page=ALLOCATE()
# #                 RA=page*10
# #                 if page<=9:
# #                     M[PTR+int(IR[2:])//10]='100'+str(page)
# #                 else:
# #                     M[PTR+int(IR[2:])//10]='10' +str(page)
# #                 TTC+=1
# #             except:
# #                 PI = 2
# #                 SI = 0
# #         elif IR[:2]=='PD':
# #             try:
# #                 RA=ADDRESSMAP(int(IR[2:]))
# #                 SI=2
# #                 if RA is not None:
# #                     TTC+=1
# #             except:
# #                 PI=2
# #         elif IR=='H':
# #             SI=3
# #             TTC+=1
# #         else:
# #             PI=1 #opcode error
# #         if TTC>TTL:
# #             TI=2
# #         if SI!=0 or PI!=0 or TI!=0:
# #             MOS()
# #         RA=ADDRESSMAP(IC)
# #         if RA is not None:
# #             IR=M[RA]

# # STARTEXECUTION()