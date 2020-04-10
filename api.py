from flask import Flask, jsonify, request, make_response
import bank_manager
from saving import SavingAccount
from chequing import ChequingAccount
from bank_account import BankAccount


app = Flask(__name__)




@app.route("/validate", methods=["GET", "POST", "PUT", "DELETE"])
def validate_setup():
    """Sets up methods"""
    return jsonify(
        {
            "method": request.method,
            "Content-Type header": request.headers.get("Content-Type"),
            "data": request.data.decode(),
        }
    )
@app.route("/entitymanager/create", methods=["POST"])
def add_account():
    """Adds chequing account to DB"""
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        account = (data["interest_rate"], data["max_withdraw"],data["type"],data["person_name"],data["home_branch"],data["account_number"],data["balance"],data["min_bal"],data["stock"])
        bank_manager.create_account(account)
        return make_response('OK' + ' ' + str(account[5]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)





@app.route("/entitymanager/entities/<string:entity_id>", methods=["PUT"])
def update_account(entity_id):
    """Update accounts home branch"""
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)

    account = bank_manager.get_account_info(entity_id)
    if not account:
        return make_response("Account not found.", 404)

    if "branch" not in data.keys():
        return make_response("Invalid JSON: missing branch name", 400)

    try:
        bank_manager.update_home_branch(data["branch"], entity_id)
        return make_response("OK", 200)
    except ValueError as e:
        return make_response(str(e), 404)







@app.route("/entitymanager/entities/<string:entity_id>", methods=["DELETE"])
def delete_account(entity_id):
    """Deletes account"""
    a = bank_manager.get_account_info(entity_id)
    if a is None:
        return make_response('Account does not exist', 404)
    else:
        bank_manager.delete_account(entity_id)
        return make_response("OK", 200)





@app.route("/entitymanager/entities/<string:entity_id>", methods=["GET"])
def get_account_by_id(entity_id):
    """Gets account by ID"""
    account = bank_manager.get_account_info(entity_id)
    if not account:
        return make_response("Account not found.", 404)
    item = bank_manager.get_account_info(entity_id)
    print(item)
    x = {'Account Holder': item[1], 'Account Number': item[2], 'Balance': item[3], 'Minimum Balance': item[4],
         'Stock': item[5], 'Home Branch': item[6], "Type": item[7]}
    print(x)
    return make_response(jsonify(x), 200)



@app.route("/entitymanager/entities/all", methods=["GET"])
def get_all_accounts():
    """Returns list of accounts"""
    acc_list = bank_manager.get_all_accounts()
    print(acc_list)
    return jsonify(acc_list)


@app.route("/entitymanager/entities/all/<string:type>", methods=["GET"])
def get_account_by_type(type):
    """Returns accounts by specified type"""
    if (type != 'chequing') and (type != 'savings'):
        return make_response('Invalid Account Type', 400)
    try:
        acc_list = bank_manager.get_acc_by_type(type)
        return make_response(jsonify(acc_list), 200)
    except ValueError as e:
        return make_response(str(e), 404)



@app.route("/entitymanager/entities/stats", methods=["GET"])
def get_stats():
    """Returns entity stats"""
    stats = bank_manager.stats()
    print(stats)
    return make_response(jsonify(stats), 200)



### Create your methods here

if __name__ == "__main__":
    app.run(debug=True)
