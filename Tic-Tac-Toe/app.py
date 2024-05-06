from flask import Flask, render_template, jsonify,request
from main import System_play,check
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/play', methods=['POST','GET'])
def play():
    userresponse = request.json['value']
    xState = request.json['xState']
    zState = request.json['zState']
    if xState[int(userresponse)]==1 or zState[int(userresponse)]==1:
        message="Wrong Input"
        system_play = zState
    else:
        message=""
        xState[int(userresponse)]=1
        checking=check(xState,zState)
        print(checking)
        if (checking[0] == 1):
            message="You Won"
            system_play=zState
        elif (checking[0] == 0):
            message="System Won"
            system_play = zState
        elif (checking[0] == 2):
            message="It's a Draw"
            system_play = zState
        else:
            system_play=System_play(xState,zState)[1]

    checking = check(xState, zState)
    if (checking[0] == 1):
        message="You Won"
    elif (checking[0] == 0):
        message="System Won"
    elif (checking[0] == 2):
        message="It's a Draw"
    print(checking[1])
    return jsonify({'xState': xState, 'zState': system_play,'message':message ,'win':f"{checking[1]}"})

if __name__ == '__main__':
    app.run(debug=True)