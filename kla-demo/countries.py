from flask import Flask, json, request
api = Flask(__name__)
Countries = []

@api.route('/')
def hello_world():
    return 'Hello, World!'

@api.route('/country', methods=['POST'])
def addCountries():
    acquiredData = request.get_json()
    idTemp = str(len(Countries)+1)
    acquiredData["id"]=idTemp
    Countries.append(acquiredData)
    print(Countries)
    return json.dumps("Success")

@api.route('/country/list',methods=['GET'])
def returnListOfCountries():
    return json.dumps(Countries)

@api.route('/country/<id>', methods=['GET'])
def getParticular(id):
    for i in Countries:
        if i["id"] == id:
            return json.dumps(i)

@api.route('/country/<id>', methods=['PUT'])
def updateList(id):
    acquiredData = request.get_json()
    for i in Countries:
        if i["id"] == id:
            i["capital"] = acquiredData["capital"]
    print(Countries)
    return json.dumps(Countries)

if __name__ == '__main__':
    api.run()