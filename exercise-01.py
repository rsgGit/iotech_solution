import json

#read json file
def parseFile():
    f = open ('exercise-01/data/devices.json', "r")
    data = json.loads(f.read())
    return data

#helper function to extract relevant info
def extractData(data):
    name = data["Name"]
    type = data["Type"]
    info = data["Info"]
    sensors = data["Sensors"]
    return name, type, info, sensors

#helper function to calculate total pay load given the list of sensors for a device
def getTotalPayload(sensors):
    payloadTotal = 0

    for sensor in sensors:
        payloadTotal = payloadTotal + int(sensor['Payload'])
    return payloadTotal

#helper function to create the new object given relevant info acc to the new schema
def createNewObject(name, type, info, uuid, total):
    ob = {}
    ob["Name"] = name
    ob["Type"] = type
    ob["Info"] = info
    ob["Uuid"] = uuid
    ob["PayloadTotal"] = total
    return ob

# exctracts and creates new fields. creates the new dictionary
def convertSchema(data):
    ob = {}
    ob["Devices"] = []
    for device in data["Devices"]:
       
        name, type, info, sensors = extractData(device)
        uuid = info.split("uuid:")[1].split(',')[0]
        info = info.replace("uuid:"+uuid+', ', '')
        payloadTotal = getTotalPayload(sensors)
        ob["Devices"].append(createNewObject(name, type, info, uuid, payloadTotal))

    ob["Devices"].sort(key=lambda x: x["Name"].lower())
    return(ob)

#write to json
def writeFile(data):
    jdata = json.dumps(data, indent=3)
    with open("exercise01_modified_data.json", "w") as outfile:
        outfile.write(jdata)
   



data = parseFile()
new_data = convertSchema(data)
writeFile(new_data)