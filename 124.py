from flask import Flask,jsonify,request

app= Flask(__name__)

contacts =[
    {
        'Name': "Raju",
        'Contact': "9987644456",
        'done' : False,
        'id':1
    },
    {
       
        'Name': "Rahul",
        'Contact': "9876543222",
        'done' : False,
        'id':2 
    }
]

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Something Went Wrong..."
        },400)
        contact={
            'id': tasks[-1]['id']+1,
            'Name': request.json['Name'],
            'Contact': request.json.get('Contact',""),
            'done' : False
        }
        contacts.appened(contact)
        return jsonify({
            "status":"success",
            "message":"Succfully Done.."
        })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    })

if(__name__ == "__main__"):
    app.run(debug=True)