# Open the file in read mode
Alphabeth=[]
SetofStates=[]
SetofFStates=[]
SetofIStates=[]
exceptions=[" ","_"]
def split_string(s, size):
    return [s[i:i+size] for i in range(0, len(s), size)]

with open('Fa.input', 'r') as file:
    content = file.read()
result = split_string(content, 5)
# Print the content
print(result)
print (len(result))

for i in range(0,len(result)-1):
    if ((result[i][2] not in Alphabeth) and (result[i][2]not in exceptions)):{
        Alphabeth.append(result[i][2])
    }

    ss=result[i][0:2]
    sf=result[i][-5:-3]
    print(sf)
    if (ss not in SetofStates):{
        SetofStates.append(ss)
    }
    if(result[i][2]==" "):{
    SetofIStates.append(ss)
    }
    if (result[i][2] == "_"): {
        SetofFStates.append(ss)
    }
    if (sf not in SetofStates):{
        SetofStates.append(sf)
    }
print("Alpabeth:")
print(Alphabeth)
print("Set of states:")
print(SetofStates)
print("Starting node ")
print(SetofIStates)
print("Final nodes ")
print(SetofFStates)

for i in range(0,len(result)-1):
    if (result[i][2] in Alphabeth): {
        print(result[i])
    }
