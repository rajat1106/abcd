ifile=open("Operating-System-Course-Project-main\\input1.txt", 'r')
ofile=open("Operating-System-Course-Project-main\\output1.txt", 'w')
input_data=ifile.readlines()  
data=""

def READ(memory,IR): 
    global data
    end=data.find('\n') 
    start=int(IR[2:])
    p=0
    string=data[:end] 
    
    while(p<end):
        try:
            memory[start]=string[p:p+4] 
        except:
            memory[start]=string[p:end] 
        p=p+4
        start=start+1 
    data=data[end+1:] 
    
def WRITE(memory,IR): 
    start=int(IR[2:])
    put="".join(memory[start:start+10]).replace('0000','') 
    ofile.write(put)
    ofile.write('\n')
    
def TERMINATE(ofile):
    ofile.write('\n\n')
    
def MASTER_MODE(SI,memory,IR):
    if(SI==1):
        READ(memory,IR)
    elif(SI==2):
        WRITE(memory,IR)
    elif(SI==3):
        TERMINATE(ofile)
    else:
        return

        
def SLAVE_MODE(memory):
    IC=0 
    Register=0 
    TF=False  
    
    while(True):
        IR=memory[IC] 
        SI=0 
        
        if IR=='H':
            SI=3
            MASTER_MODE(SI,memory,IR)
            break
        elif IR[:2]=='GD':
            SI=1
            MASTER_MODE(SI,memory,IR)
        elif IR[:2]=='PD':
            SI=2
            MASTER_MODE(SI,memory,IR)
        elif IR[:2]=='LR':
            start=int(IR[2:])
            Register=memory[start] 
        elif IR[:2]=='SR': 
            start=int(IR[2:])
            memory[start]=Register
        elif IR[:2]=='CR':
            start=int(IR[2:])
            if memory[start]==Register: 
                TF=True
        elif IR[:2]=='BT':
            if TF==True: 
                start=int(IR[2:]) 
                IC=start-1 
        IC=IC+1 
        

def LOAD():
    global data
    memory=[] 
    job=""
    n=0
    data=""
    
    for line in input_data:
        #print(line)
        if line[:4]=='$AMJ':
            print("Starting...")
            line=line[:len(line)-1]
            print("AMJ: " + line)
        elif line[:4]=='$DTA':
            n=1
        elif line[:4]=='$END':
            SLAVE_MODE(memory)
            print("Memory: ")
            print('  '.join( memory))
            #print(memory)
            print("End.")
            print("------------------------------------------------------\n")
            
            memory=[]
            data=""
            #print("end: " +line)
            n=0
        elif n==1:
            data=data+line[:len(line)]
            #print("data: " +data)
        else:
            job=line[:len(line)-1] 
            print("JOB: "+job)
            #print(job)    
            k=0
            while(k<len(job)):
                if(job[k]=='H'): 
                    memory.append(job[k]) 
                    k=k+1
                    break
                memory.append(job[k:k+4]) 
                k=k+4
           # memory.pop()
            #print(memory)
            while(len(memory)!=100):
                memory.append('0000') 
    
            
def Main():
    LOAD()
    
Main()

ofile.close()
ifile.close()