import capnp

import account_capnp

host = "localhost:60000"
client = capnp.TwoPartyClient(host)

accounts = client.bootstrap().cast_as(account_capnp.Accounts)
account_ids = []

def create_account(initial_balance):
    create_promise = accounts.createAccount(initial_balance)
    account = create_promise.wait()
    return account

def delete_account(account_id):
    accounts.deleteAccount(account_id.hex()).wait()

def transfer_funds(source_account_id, destination_account_id, funds_amount_id):
    accounts.transferFunds(source_account_id, destination_account_id, funds_amount_id)

for i in range(1, 10):
    account = create_account(i)
    print(account.account.id.hex())
    account_ids.append(account.account.id.hex())
    transfer_funds(account_ids[i-1], account_ids[0], 1)
    delete_account(account.account.id)
