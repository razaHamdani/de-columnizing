INPUT_FILE_NAME = "input_decol2.txt"


def removeSpecialChars(line):
    textToSend = ''
    start = 0
    end = len(line)
    
    plusRangeToCut = [i for i in range(len(line)) if line.startswith("+", i)]
    lineRangeToCut = [i for i in range(len(line)) if line.startswith("|", i)] 
    noOfPluses = len(plusRangeToCut)
    noOfLines = len(lineRangeToCut)
    if noOfPluses == 4:
        end = plusRangeToCut[2]
        start = plusRangeToCut[1]
    elif noOfLines == 4:
        end = lineRangeToCut[2]
        start = lineRangeToCut[1]
    elif noOfPluses == 2:
        if noOfLines == 0:
            if plusRangeToCut[0] == 0:
                start = plusRangeToCut[1]
            else:
                end = plusRangeToCut[0]
        elif noOfLines == 1:
            theMin = min(lineRangeToCut[0],plusRangeToCut[0],plusRangeToCut[1])
            if theMin == 0: 
                start = max(lineRangeToCut[0],plusRangeToCut[0],plusRangeToCut[1])
            else:
                end = theMin
        elif noOfLines == 2:
            sortedRanges = sorted([plusRangeToCut[0],plusRangeToCut[1],lineRangeToCut[0],lineRangeToCut[1]])
            start = sortedRanges[1]
            end = sortedRanges[2]
            
            
    elif noOfLines == 2: # simply no pluses
        if lineRangeToCut[0] == 0:
            start = lineRangeToCut[1]
        else:
            end = lineRangeToCut[0]

        
    if line[start] in ("+","|"):
        textToSend = line[start+1:end].strip() 
    else:
        textToSend = line[start:end].strip()
    #print "textToSend:|%s|" % textToSend 
    
    return textToSend

def HyphenAndParaCheck(text):  
    if text == "":
        return text
    
    if text[-1] == "-":
        text = text[:-1]
    elif text[-1] != "\n":
        text += " "
    
    return text
     
def de_col():
    count = 1
    actualText = ''
    with open(INPUT_FILE_NAME) as fp:
        for line in fp:
            line = line.strip()
            if count > 1:
                if line == "":
                    actualText += "\n"
                elif "+" in line or "|" in line:
                    res = removeSpecialChars(line)
                    if res == "":
                        actualText += "\n"
                    else:    
                        actualText += res
                else:    
                    actualText += line
                                     
            actualText = HyphenAndParaCheck(actualText)
            count += 1

        return actualText
             
                
if __name__ == '__main__': 
    
    print de_col()
    
