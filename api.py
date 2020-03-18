from flask import Flask, jsonify, request, make_response
from bank_manager import Bank
from saving import SavingAccount
from chequing import ChequingAccount


app = Flask(__name__)

bank = Bank("TD Canada Trust")


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
@app.route("/entitymanager/chequing", methods=["POST"])
def add_chequing_account():
    """Adds chequing account to bank array"""
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        account = ChequingAccount(data["max_spend"], data["min_spend"],data["name"],data["branch"],data["acc_num"])
        bank.add_account(account)
        return make_response('OK' + ' ' + account._account_number, 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)


@app.route("/entitymanager/savings", methods=["POST"])
def add_savings_account():
    """Adds saving account to bank array"""
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        account = SavingAccount(data["interest"], data["max_withdraw"],data["name"],data["branch"],data["acc_num"])
        bank.add_account(account)
        return make_response('OK' + ' ' + account._account_number, 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)


@app.route("/entitymanager/entities/<string:entity_id>", methods=["PUT"])
def update_account(entity_id):
    """Update accounts home branch"""
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)

    account = bank.get_account_info(entity_id)
    if not account:
        return make_response("Account not found.", 404)

    if "branch" not in data.keys():
        return make_response("Invalid JSON: missing branch name", 400)

    try:
        bank.update_home_branch(data["branch"], entity_id)
        return make_response("OK", 200)
    except ValueError as e:
        return make_response(str(e), 404)







@app.route("/entitymanager/entities/<string:entity_id>", methods=["DELETE"])
def delete_account(entity_id):
    """Deletes account"""
    a = bank.get_account_info(entity_id)
    a = bank.get_account_info(entity_id)
    if a is None:
        return make_response('Account does not exist', 404)
    else:
        bank.close_account(entity_id)
        return make_response("OK", 200)





@app.route("/entitymanager/entities/<string:entity_id>", methods=["GET"])
def get_account_by_id(entity_id):
    """Gets account by ID"""
    account = bank.get_account_info(entity_id)
    if not account:
        return make_response("Account not found.", 404)

    return make_response(jsonify(bank.get_account_info(entity_id).to_dict()), 200)


@app.route("/entitymanager/entities/all", methods=["GET"])
def get_all_accounts():
    """Returns list oft accounts"""
    acc_list = bank.get_all_accounts()
    return make_response(jsonify(acc_list), 200)


@app.route("/entitymanager/entities/all/<string:type>", methods=["GET"])
def get_account_by_type(type):
    """Returns accounts by specified type"""
    if (type != 'chequing') and (type != 'savings'):
        return make_response('Invalid Account Type', 400)
    try:
        acc_list = bank.get_acc_by_type(type)
        return make_response(jsonify(acc_list), 200)
    except ValueError as e:
        return make_response(str(e), 404)



@app.route("/entitymanager/entities/stats", methods=["GET"])
def get_stats():
    """Returns entity stats"""
    stats = bank.stats()
    return make_response(stats, 200)



### Create your methods here

if __name__ == "__main__":
    app.run(debug=True)
