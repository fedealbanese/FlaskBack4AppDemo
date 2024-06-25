import json
from openai import OpenAI
from flask import Flask, render_template, request, redirect, url_for
from api_functions import generate_response
from initilized_functions import initiate_state, initilized_templates
from user_state_functions import update_state_from_api, update_state_from_configuration

#initiate app
variables = {}
variables["directory_examples"] = "examples/"
variables["OpenAI_client"] = None
variables["user_state"] = {}
variables["templates"] = {}
variables["response_dicts"] = {}


#Flask APP
app = Flask(__name__)

#Base Paths
@app.route('/')
def restart():
    variables["user_state"] = initiate_state(variables["directory_examples"])
    variables["templates"], variables["response_dicts"] = initilized_templates(variables["directory_examples"])
    return variables["user_state"]

@app.route('/Key/<key>')
def OpenAIKey(key):
    variables["OpenAI_client"] = OpenAI(
        api_key = "sk-" + key,
    )
    return f"New key: {key}"

@app.route('/User_state')
def Userstate():
    return variables["user_state"]

@app.route('/Update_state', methods=['GET', 'POST'])
def UpdateState():
    if request.method == 'POST':
        prompt = request.form['input_configuration']
        variables["user_state"] = update_state_from_configuration(
            variables["OpenAI_client"], 
            variables["user_state"], 
            prompt
        )
        return redirect(url_for('UpdateState'))
    return render_template('configuration.html', user_state = variables["user_state"])

#API Paths
@app.route('/portfolio/<accountId>/ledger') #Account_Ledger
def accountLedger(accountId):
    print("Se llamo al endpoint Account_Ledger con parametro:", accountId)
    response = generate_response(
        "Account_Ledger", 
        variables["user_state"], 
        variables["response_dicts"]
    )
    return response

@app.route('/portfolio/<accountId>/summary') #Account_Summary
def accountSummary(accountId):
    print("Se llamo al endpoint Account_Summary con parametro:", accountId)
    response = generate_response(
        "Account_Summary", 
        variables["user_state"], 
        variables["response_dicts"]
    )
    return response

@app.route('/iserver/account/<accountId>/orders/whatif') #Preview_Orders
def previewOrders(accountId):
    print("Se llamo al endpoint Preview_Orders con parametro:", accountId)
    response = generate_response(
        "Preview_Orders", 
        variables["user_state"], 
        variables["response_dicts"]
    )
    return response

@app.route('/iserver/account/orders') #Live_Orders
def LiveOrders():
    print("Se llamo al endpoint Live_Orders sin parametros.")
    response = generate_response(
        "Live_Orders", 
        variables["user_state"], 
        variables["response_dicts"]
    )
    return response

@app.route('/iserver/account/order/status/<orderId>') #Order_Status
def orderStatus(orderId):
    print("Se llamo al endpoint Order_Status con parametro:", orderId)
    response = generate_response(
        "Order_Status", 
        variables["user_state"], 
        variables["response_dicts"]
    )
    return response

@app.route('/portfolio/<accountId>/positions/<pageId>') #Portfolio_Position
def portfolioPosition(accountId, pageId):
    print("Se llamo al endpoint Portfolio_Position con parametros:", accountId, " y ", pageId)
    response = generate_response(
        "Portfolio_Position", 
        variables["user_state"], 
        variables["response_dicts"]
    )
    return response

@app.route('/iserver/marketdata/history') #Market_Data_History
def marketDataHistory():
    print("Se llamo al endpoint Market_Data_History sin parametros.")
    response = generate_response(
        "Market_Data_History", 
        variables["user_state"], 
        variables["response_dicts"]
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
