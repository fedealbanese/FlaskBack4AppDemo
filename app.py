import json
from flask import Flask
from flask import make_response, jsonify

#initiate app
variables = {}
variables["user_state_salary"] = 0
variables["file_name"] = "account_summery.json"

#Flask APP
app = Flask(__name__)

@app.route('/')
def restart():
    variables["user_state_salary"] = 0
    return "Hi :)"

@app.route('/update/<salary>')
def update(salary):
    variables["user_state_salary"] = salary
    print(f"Update salary to {salary}")
    return f"Salary: {salary}"

@app.route('/salary')
def salary():
    print(f"Your salary is {variables['user_state_salary']}")
    return variables["user_state_salary"]

@app.route("/APIsalary")
def apisalary():
    with open(variables["file_name"]) as f:
        account_summery = json.load(f)
    for key in account_summery:
        account_summery[key]["amount"] = int(variables["user_state_salary"])
    jsonify_account_summery = jsonify(account_summery)
    response = make_response(jsonify_account_summery)
    #response.headers["customHeader"] = "custom value"
    print(jsonify_account_summery)
    print(account_summery) #print(json.dumps(account_summery, indent=2))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
