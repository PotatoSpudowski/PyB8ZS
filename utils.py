def ToBipolarAmi(dataStream, lastSymbol):
    
    dataStream = list(dataStream)
    Bipolar_AMI = [0]*len(dataStream)
    for i in range(len(dataStream)):
        if dataStream[i] == '1' and lastSymbol == 1:
            Bipolar_AMI[i] = -1
            lastSymbol = -1

        elif dataStream[i] == '1' and lastSymbol == -1:
            Bipolar_AMI[i] = 1
            lastSymbol = 1

    return Bipolar_AMI


def B8ZS_Scrambler(BAMIStream, lastSymbol):

    consecZero = 0
    table = {
        "1" : [0,0,0,1,-1,0,-1,1],
        "-1" : [0,0,0,-1,1,0,1,-1]
    }

    for i in range(len(BAMIStream)):
        if BAMIStream[i] == 1:
            lastSymbol = 1
        
        elif BAMIStream[i] == -1:
            lastSymbol = -1

        elif BAMIStream[i] == 0:
            consecZero += 1

            if consecZero == 8:
                BAMIStream = BAMIStream[0:i-7] + table[str(lastSymbol)] + BAMIStream[i+1:]                  


    return BAMIStream
