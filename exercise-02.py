import json
import base64
import time

#read json file
def parseFile():
    f = open ('exercise-02/data/data.json', "r")
    data = json.loads(f.read())
    return data

#helper function to convert base64 to int
def convertBase64ToInt(value):
    base64_bytes = value.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    v = int(sample_string_bytes.decode("ascii"))
    return v

#helper function to extract relevant info
def extractData(data):
    info = data["Info"]
    value = data["value"]
    timestamp = data["timestamp"]   
    return info, value, timestamp

#helper function to create the new object given relevant info acc to the new schema
def createNewObject(total, uuids):
    ob = {}
    ob["ValueTotal"] = total
    ob["UUIDS"] = uuids
    return ob

# exctracts and creates new fields. creates the new dictionary
def convertSchema(data):
    
    totalValue = 0
    uuids = []
    for device in data["Devices"]:   
        info, value, timestamp = extractData(device)
        current = int(time.time()) 
        if(current<int(timestamp)):
            uuid = info.split("uuid:")[1].split(',')[0]      
            uuids.append(uuid)
            totalValue = totalValue + convertBase64ToInt(value)
    return(createNewObject(totalValue, uuids))

#write to json
def writeFile(data):
    jdata = json.dumps(data, indent=3)
    with open("exercise02_modified_data.json", "w") as outfile:
        outfile.write(jdata)
   

data = parseFile()
new_data = convertSchema(data)
writeFile(new_data)