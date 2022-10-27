from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/user')    
def test():
    retJson={
         'json1':'abcd',
         'field2':"djsvkj",
          "data":[{"stuff":[
    {"onetype":[
        {"id":1,"name":"John Doe"},
        {"id":2,"name":"Don Joeh"}
    ]},
    {"othertype":[
        {"id":2,"company":"ACME"}
    ]}]
},{"otherstuff":[
    {"thing":
        [[1,42],[2,2]]
    }]
}]
    }
    return jsonify(retJson)

if __name__=="__main__":
    app.run(debug=True)