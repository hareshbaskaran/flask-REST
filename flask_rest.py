from flask import Flask,jsonify,request
from flask_restful import Api,Resource
app = Flask(__name__)
api=Api(app)

def checkPostedData(postedData,functionName):
    if(functionName=="add" or "sub" or "mul"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
class Add(Resource):
    def post(self):
    #get posted data:
        postedData=request.get_json()
        status_code=checkPostedData(postedData,"add")
        if(status_code!=200):
            retJson={
                  'message':"error message",
            'status code':status_code
            }
            return jsonify(retJson)
        x=postedData["x"]
        y=postedData["y"]
        x=int(x)
        y=int(y)
    #Add the posted Data       
        ret=x+y
        retMap={
            'message':ret,
            'status code':200 
        }
        return jsonify(retMap)
class Sub(Resource):
       def post(self):
    #get posted data:
        postedData=request.get_json()
        status_code=checkPostedData(postedData,"sub")
        if(status_code!=200):
            retJson={
                  'message':"error message",
            'status code':status_code
            }
            return jsonify(retJson)
        x=postedData["x"]
        y=postedData["y"]
        x=int(x)
        y=int(y)
    #Add the posted Data       
        ret=x-y
        retMap={
            'message':ret,
            'status code':200 
        }
        return jsonify(retMap)
class Mul(Resource):
    def post(self):
    #get posted data:
        postedData=request.get_json()
        status_code=checkPostedData(postedData,"mul")
        if(status_code!=200):
            retJson={
                  'message':"error message",
            'status code':status_code
            }
            return jsonify(retJson)
        x=postedData["x"]
        y=postedData["y"]
        x=int(x)
        y=int(y)
    #Add the posted Data       
        ret=x*y
        retMap={
            'message':ret,
            'status code':200 
        }
        return jsonify(retMap)
class Div(Resource):
    pass

#add api resources for created classes
api.add_resource(Add,"/add")
api.add_resource(Sub,"/sub")
api.add_resource(Mul,"/mul")

@app.route('/')    
def test():
    return'test'

if __name__=="__main__":
    app.run(debug=True)