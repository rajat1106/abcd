import random

ifile=open("input3.txt", 'r')
ofile=open("output3.txt", 'w')
cardreader=ifile.readlines()
IR1List=[]
#PCB={'TTC': 0,'TLC':0,'TS':0,'L':0,'TLL':0,'TTL':0,'TSC':0,'P':[],'D':[],'PC':0,'DC':0,'O':[]}
TSC=0
CH=[0,0,0,0]
CHTC=[0,0,0,0]
CHTT=[0,5,5,2]
ebq=[[],[],[],[],[],[],[],[],[],[]]
ifbq=[]
ofbq=[]
LQ=[]
RQ=[]
IOQ=[]
TQ=[]
UC=0
#DC=0
linecount=0
F=''
choose=[i for i in range(29)]
drum=[]
TI=0
SI=0
PI=0
IOI=0
CH[1]=1
M=[None for i in range(300)]
DL=0
task=''
error={0:'NO ERROR',1:'OUT OF DATA',2:'LINE LIMIT EXCEEDED',3:'Time Limit Exceeded',4:'Operation Code Error',5:'Operand Error',6:'Invalid Page Fault',7:'TIME LIMIT EXCEEDED And OPERAND ERROR',8:'TIME LIMIT EXCEEDED And OPERATION CODE ERROR'}

def print_mem():
    print("                                                         Memory")
    print()
    for i in range(len(M)):
        if(i<9):
            print(" ", "00"+ str(i), M[i], " ",end ="    ")
        elif(i < 99):
            print(" ", "0"+ str(i), M[i], " ",end ="    ")
        else :
            print(" ", str(i), M[i], " ",end ="    ")

def TERMINATE(EM,PCB):
    global M
    
    ofile.write(' \n'+error[EM].upper()+'\n')
    ofile.write('JOB ID:'+str(PCB['JID'])+' ')
    ofile.write(' '+error[EM].upper()+' ')
    ofile.write('IC:'+str(PCB['IC'])+' ')
    ofile.write('IR:'+str(PCB['IR'])+'\n')
    ofile.write('TTL:'+str(PCB['TTL'])+' ')
    ofile.write('TTC:'+str(PCB['TTC'])+' ')
    ofile.write('TLL:'+str(PCB['TLL'])+' ')
    ofile.write('LLC:'+str(PCB['LLC'])+' ')
    ofile.write('\n\n')
    
    print_mem()
    
    print("\n---------------------------Program Execution Ended----------------------------\n")
    


def SLAVEMODE():


    print("In Slave")
    
    global M
    global RA
    global PI
    global R
    global RQ
    global SI
    global TI
    global C
    if(len(RQ)==0):
        return
    #print("RQ",RQ)
    PCB=RQ[0]
    # PCB['TTC']=0
   
    #print(PCB)
    RA=ADDRESSMAP(PCB['IC'],PCB)
    print("PCB :",PCB, "RA :",RA,"  PTR :",PCB['PTR'],"IC :",PCB['IC']); 
    if PI != 0:
        return 
    try:
        #if RA is not None:
        PCB['IR']=M[RA]

    except:
        return
    
    PCB['IC']+=1
    if PCB['IR'][:2]=='LR':
        print("IN LR")
        
        
        try:

            RA=ADDRESSMAP(int(PCB['IR'][2:]),PCB)
            if RA is None:
                PI=3
            else:
                R=M[RA]
                PCB['TTC']+=1

        except:
            PI=2

    elif PCB['IR'][:2]=='SR':
        print("IN SR")
        try:
            if M[PTR+int(PCB['IR'][2:])//10]!=None:
                RA=ADDRESSMAP(int(PCB['IR'][2:]),PCB)
            else:
                page=ALLOCATE()
                PCB['TTC']+=1
                RA=page*10
                if page<=9:
                    M[PTR+int(PCB['IR'][2:])//10]='000'+str(page)
                else:
                    M[PTR+int(PCB['IR'][2:])//10]='00' +str(page)
                M[RA+int(PCB['IR'][2:])%10]=R
                
            M[RA]=R
        except:
            #print("In sR except")
            PI=2
        PCB['TTC']+=1
        #printMem(M)
    elif PCB['IR'][:2]=='CR':
        print("IN CR")
        RA=ADDRESSMAP(int(PCB['IR'][2:]),PCB)
        if R==M[RA]:
            C=True
            print("TOGGLE FLAG SET")
        else:
            C=False
            print("TOGGLE FLAG NOT SET")
        PCB['TTC']+=1
    elif PCB['IR'][:2]=='BT':
        print("IN BT")
        if C==True:
            PCB['IC']=int(PCB['IR'][2:])
            print("BT JUMP " ,PCB['IC'])
        else:
            pass
        PCB['TTC']+=1
    elif PCB['IR'][:2]=='GD':
        print("IN GD")
        try:
            SI=1
           # print("IR:",int(IR[2:]))
        except:
            PI = 2
            SI = 0
    elif PCB['IR'][:2]=='PD':
        try:
            SI=2
            if RA is None:
                PI=3
        except:
            PI=3
    elif PCB['IR']=="H":
        print("IN H")
        SI=3
        PCB['TTC']+=1
    else:
        PI=1 
        print("IN ELSE")#opcode error
        # PCB['TTC']+=1
    if PCB['TTC']>PCB['TTL']:
        TI=2
        
        

                 
def ADDRESSMAP(IC,PCB): #for converting logical address into real address
    print(PCB)
    print(IC)
    global M
    global PI
    print(M[PCB['PTR']])
    k=IC//10#(10 is page size)
    rem=IC%10
    if(0 <= int(IC) >= 99):
        PI = 2
    if type(IC)==int:
        try:
            fr=int(M[PCB['PTR']+k][2:])
            RA=fr*10+rem
            return RA
        except:
            PI=3
    else:
        PI=2 #operand error

def ALLOCATE():
    global choose
    k=random.choice(choose)
    print("ALLOCATION ARRAY : ",choose)
    choose.remove(k)
    return k

def CHi(i):
    global IOI
    global CHTC
    global CH
    print("IN CHANNEL",i)
    if i==1:
        IOI=IOI-1
    elif i==2:
        IOI=IOI-2
    elif i==3:
        IOI=IOI-4
    CHTC[i]=0
    CH[i]=1

def MOS():
    print("IN MOS")
    global SI
    global TI
    global PI
    global IOI
    global RQ
    global TQ
    global IOQ
    if TI==2:
        if SI==1:

            j=RQ.pop(0)
            TQ.append(j)
            TERMINATE(3,j)
        elif SI==2:
            j=RQ.pop(0)
            IOQ.append(j)
            #WRITE()
            j=IOQ.pop(0)
            TQ.append(j)
            TERMINATE(3,j)
        elif SI==3:
            j=RQ.pop(0)
            TQ.append(j)
            # print(TQ)
            TERMINATE(0,j)
        elif PI==1:
            j=RQ.pop(0)
            if (len(j['O'])!=0):
                TQ.append(j)
            TERMINATE(3+5,j)
        elif PI==2:
            j=RQ.pop(0)
            if (len(j['O'])!=0):
                TQ.append(j)
            TERMINATE(3+4,j)
        elif PI==3:
            j=RQ.pop(0)
            if (len(j['O'])!=0):
                TQ.append(j)
            TERMINATE(3,j)
        else:
            j=RQ.pop(0)
            TERMINATE(3,j)
    elif TI==0 or TI==1:
        if SI==1:
            # print("RQ :",RQ)
            if(len(RQ)):
                j=RQ.pop(0)
            IOQ.append(j)
            # print("IOQ :",IOQ)
        elif SI==2:
            # print("RQ :",RQ)
            if(len(RQ)):
                j=RQ.pop(0)
            IOQ.append(j)
            # print("IOQ :",IOQ)
        elif SI==3:
            # print("RQ :",RQ)
            if(len(RQ)):
                j=RQ.pop(0)
            TQ.append(j)
            # print("TQ :",TQ)
            TERMINATE(0,j)
        elif PI==1:
            if(len(RQ)):
                j=RQ.pop(0)
            if (len(j['O'])!=0):
                TQ.append(j)
            TERMINATE(4,j)
        elif PI==2:
            if(len(RQ)):
                j=RQ.pop(0)
            if (len(j['O'])!=0):
                TQ.append(j)
            TERMINATE(5,j)
        elif PI==3:
            if(len(RQ)):
                j=RQ.pop(0)
            if (len(j['O'])!=0):
                TQ.append(j)
            TERMINATE(6,j)

    if IOI==1:
        IR1()
        # print(IOI)
    elif IOI==2:
        IR2()
    elif IOI==3:
        IR2()
        IR1()
    elif IOI==4:
        IR3()
    elif IOI==5:
        IR1()
        IR3()
    elif IOI==6:
        IR3()
        IR2()
    elif IOI==7:
        IR2()
        IR1()
        IR3()

    SI=0
    TI=0
    PI=0
    #IOI=0
    
def IR1():
    global ebq
    global linecount
    global ifbq
    global F
    global IR1List
    global IOI
    global task
    global DC
    print("IN IR1")
    
    PCB={}
    # print("IR1",IOI)
    #lst=ebq.pop(0)
    lst=[]
    if linecount<len(cardreader):
        lst.append(cardreader[linecount])
    else:
        IOI-=1
        CHTC[1]=0
        return
    # print(lst)

    val=lst[0][:-1]
    lst.pop()
    lst.append(val)
    # print(val)


    

  
    lst=[[s[i:i+4] for i in range(0,len(s),4)] for s in lst]
    
   
    
    linecount=linecount+1
    #if linecount<len(cardreader) and len(ebq)!=0 and CH[1]==0:
    CHi(1)


    
    if lst[0][0]=='$AMJ':
        
        PCB={'TTC': 0,'TLC':0,'TS':0,'L':0,'TLL':0,'TTL':0,'TSC':0,'P':[],'D':[],'PC':0,'DC':0,'DCC':0,'O':[],'IC':0,'PTR':0,'IR':""}
        # print("----------------INItialized")
        PCB['JID']=lst[0][1]
        PCB['TTL']=int(lst[0][2])
        PCB['TLL']=int(lst[0][3])
        PCB['L']=int(lst[0][3])
        PCB['LLC']=0
        PCB['TTC']=0
        # PTR=ALLOCATE()*10
        # print("Program Started Amj")
        F='P'

        IR1List.append(PCB)
        print("Buffer",lst[0])
        print("Flag status : ", F)
        #DC=0
        # ifbq.pop(0)
        # ebq.append([])
    elif lst[0][0]=='$DTA':
        F='D'
        print("Buffer",lst[0])
        print("Flag status : ", F)
        # ifbq.pop(0)
        # ebq.append([])

    elif lst[0][0]=='$END':
        LQ.append(IR1List.pop(0))
        print(" Buffer",lst[0])
        # ifbq.pop(0)
        # ebq.append([])
    # elif lst[0]=='next':
    #     IR1List.append(PCB)
    #     return
    else:
        PCB=IR1List.pop(0)
        # print("PCB",PCB)
        if F=='P':
            PCB['PC']+=1
            
            
                        
        if F=='D':
            PCB['DC']+=1
        IR1List.append(PCB)   
        ifbq.append(lst[0])
        IOI=IOI + 4
        task="IS"
        print("INPUT Full Buffer" ,ifbq)

    # print("IOI:",IOI)
    # print("",ebq)
    # print("in",ifbq)
    # #IR1List.append(PCB)
    # print("INPUT Full Buffer" ,ifbq)
   

def IS():
        global PCB
        global drum
        global ifbq
        global ebq
        global IR1List
        print("IS",len(IR1List))
        lst = ifbq[0]
        ifbq.pop(0)
        ebq.append([])
        index = len(drum)
        drum.append(lst)
        if(len(IR1List)):
            PCB=IR1List[0]
        else:
            PCB=LQ[0]
        if(F=='P'):
            PCB['P'].append(index)
        else:
            PCB['D'].append(index)
        print("DRUM : ",drum)

def OS():
      # global PCB
      global drum
      global ifbq
      global ebq
      global ofbq
      global IOI
      global IR1List
      global TQ
      print("INSIDE OS")
      
     
      PCB=TQ[0]
      print(PCB)
      # print(TQ)
      #out.append(drum[ PCB['O'].pop(0) -1])
     
      if(PCB['L']!=0):
        TQ[0]['L']-=1
        out=drum[ PCB['O'].pop(0) -1]
        ebq.pop()
        ofbq.append(out)
        if(PCB['L']==0):
            TQ.pop(0)
        # print("OFBQ : ",ofbq)
        # print("Hii")
        #TQ[0]['O'].pop(0)
      else:
        TQ.pop(0)
        # print("TQ : POPPED")
      # print("TQ final :",TQ)
      print("Out Full Buffer Queue :",ofbq)
      
      

def GD():
        
        global drum
        global TQ
        global IOQ
        global choose
        print("GD")
        PCB=IOQ.pop(0)
        try:
            # PCB=IOQ.pop(0)

            print(PCB)
            try:
                data=drum[PCB['D'][0]]
                # print("outofdata1")
                PCB['D'].pop(0)
            except:
                 # print("Out of Data")
                 TERMINATE(1,PCB)
                 return
            # print("hhh",choose)
            # print("outofdata88")
            
            page=ALLOCATE()
            RA=page*10
            # print(RA)
            # print("outofdata2")
            if page<=9:
                M[PCB['PTR']+int(PCB['IR'][2:])//10]='000'+str(page)
            else:
                M[PCB['PTR']+int(PCB['IR'][2:])//10]='00' +str(page)
                if PCB['TTC']>PCB['TTL']:
                    TI=2
                    return
                    # TQ.append(PCB)
                    #IOQ.pop(0)
                    # TERMINATE(3,PCB)
            print("outofdata3")
            if PCB['DCC']>PCB['DC']:
                TERMINATE(2,PCB)
                # print("outofdata if 1")
                # print(DC)
                # TQ.append(PCB)
                #IOQ.pop(0)
                # print("outofdata if 2")
                
                # print("outofdata if 3")
            else:
                # print("outofdata else")
                k=RA
                j=0
                print("Real Address : ", RA)
                for i in data:
                    j=j+1
                if(j>=10):
                    print("Data too long")
                for i in data:
                    mp=list(i)
                    while len(mp)!=4:
                        mp.append(' ')
                    i=''.join(mp)
                    M[k]=i
                    k+=1
                PCB['DCC']+=1
                PCB['TTC']+=2
                PCB['TSC']=0
                RQ.append(PCB)
                print("READY QUEUE : " ,RQ)
                # print("outofdata5")
        except:
            print("Operand Error")
            TERMINATE(4,PCB)

        print_mem()

def PD():
        
        
        global drum
        global TQ
        global IOQ
        global PI
        global TI
        
        print("PD")
        PCB=IOQ.pop(0)
        if PCB['TTC']>PCB['TTL']:
          TI=2
          # TQ.append(PCB)
          #IOQ.pop(0)
          #TERMINATE(3,PCB)
        if PCB['TLC']>=PCB['TLL']:
          # TQ.append(PCB)
          #IOQ.pop(0)
          TERMINATE(2,PCB)
        else:
          out=[]
          RA=ADDRESSMAP(int(PCB['IR'][2:]),PCB)
          if RA is None:
            print(RA)
            PI=3
            TERMINATE(6,PCB)  
            return
              
        
          out.append(''.join(M[RA:RA+M[RA:].index(None)]))
          drum.append(out)
          PCB['O'].append(len(drum))
          PCB['TLC']+=1
          PCB['TTC']+=1
          PCB['TSC']=0
          # print("PD : ",PCB)

          RQ.append(PCB)
          print("READY QUEUE : " ,RQ)
          print("Drum : ",drum)

          
          
def IR2():
    global ifbq
    global ebq
    global IOI
    global ofbq
    global ofbq
    global F
    global SI
    global LQ
    global IOQ
    global PCB
    global TQ
    print("IN IR2")

    if len(ofbq)!=0:
        CHi(2)
        out= ofbq.pop(0)
        ebq.append([])
        ofile.write(str(out[0]))
    else :
        IOI=IOI-2
        CHTC[2]=0
        
      
def IR3():
    print("IN IR3")
    global ifbq
    global ebq
    global IOI
    global drum
    global ofbq
    global F
    global SI
    global LQ
    global IOQ
    global PCB
    global TQ
    global task
    # print(ifbq,ebq,"task",task)
   
      

    if task=="IS":
      IS()
    elif task=="OS":
      OS()
    elif task=="LD":
      LD()
    elif task=="GD":
      GD()
    elif task=="PD":
      PD()

      
    task=""
    CHi(3)
    # print("before",ifbq,ebq,LQ,IOQ,TQ)
    if len(ebq)!=0 and len(TQ)!=0 and len(TQ[0]['O'])!=0:
      print("OUTPUT SPOOLING")
      OS()
      #IOI+=2
      CH[2]=1
      
    elif len(ifbq)!=0:
      print("INPUT SPOOLING")
      IS()
            
    elif len(LQ)!=0:
      print("LOAD")
      LD()
      RQ.append(LQ.pop(0))
      
        
    elif len(IOQ)!=0:
      print("INPUT OUTPUT")
      if(SI==1):
        GD()
      if(SI==2):
        PD()
      PCB['TSC']=0
    # print("after",ifbq,ebq,LQ,IOQ)
      
def  LD():
    global PCB
    global IOI
    global PTR
    global M
    # print("Load")
    PCB=LQ[0]
    print("PCB",PCB)
    print("DRUM : ",drum)
    LQ.pop(0)
    lst=[]
    # print(PCB['P'])
    for i in range(0,len(PCB['P'])):
        lst.append(drum[PCB['P'][i]])
        drum[PCB['P'][i]]=None
    

   

    # print(lst)
    try:
            PTR=ALLOCATE()*10
            print(PTR)
            PCB['PTR']=PTR
            k=0
            j=0
            page=ALLOCATE()
            print("Program Real Address :",page)
            p=page*10
            pte=PTR
            while(j < len(lst)):
                for i in lst[k]:
                    # print("Load",i)
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
                i=0
                j+=1
                pte+=1
                page+=1
                
            # data_card=[]
            # for i in range(0,len(PCB['D'])):
            #     data_card.append(pcb['D'][i])
                
       
    except:
        print("ERROR")
        pass
    LQ.append(PCB)
    print("LOAD QUEUE : ",LQ)
    print("DRUM : ", drum)
    print_mem()

def SIMULATION():
    
    global IOI
    global CHTT
    global SI
    
    global PI
    global TI
    global CH
    # print("SIMULATION")
    global UC
    UC+=1
    if(len(RQ)):
        PCB=RQ[0]
        if PCB['TTC']==PCB['TTL'] and PCB['TTC']!=0:
            TI=2
    # PCB['TSC']=PCB['TSC']+1
    # if PCB['TCS']==PCB['TS']:
    #     TI=1

    for i in range(1,4):
        print("FLAG :",i,CH[i])
        if CH[i]==1:
            CHTC[i]+=1
            print("Counter of channel  :",i,CHTC[i])
            UC+=1
            if CHTT[i]==CHTC[i]:
                IOI=IOI+i
                if i==3:
                    IOI=IOI+1
                if IOI==8:
                    IOI=IOI-4


c=0
def start():
    global TQ
    global IOQ
    global ifbq
    global ebq
    global LQ
    global RQ
    global IOI
    global c
    while(c<250):
        print("Universal Counter :",c)
        print("\nBefore SIMULATION : " ,c ,"IOI",IOI,"SI",SI,"PI",PI ,"TI", TI)

        SIMULATION()
        print("\nAfter SIMULATION :" ,"IOI",IOI,"SI",SI,"PI",PI ,"TI", TI)

        if SI!=0 or PI!=0 or TI!=0 or IOI!=0:
            MOS()
        else:
            SLAVEMODE()
        print("\nAfter MOS/SLAVEMODE :" ,"IOI",IOI,"SI",SI,"PI",PI ,"TI", TI)
        c+=1

        if( len(TQ)==0 and len(IOQ)==0 and len(ifbq)==0 and len(LQ)==0 and len(RQ)==0 and c>350):
            break

start()

