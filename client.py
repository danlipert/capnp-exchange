import timeit

import capnp

import account_capnp

host = "localhost:60000"
client = capnp.TwoPartyClient(host)

accounts = client.bootstrap().cast_as(account_capnp.Accounts)


def create_account(initial_balance):
    create_promise = accounts.createAccount(initial_balance)
    account = create_promise.wait()
    return account


def delete_account(account_id):
    accounts.deleteAccount(account_id.hex()).wait()


def transfer_funds(source_account_id, destination_account_id, funds_amount_id):
    accounts.transferFunds(source_account_id, destination_account_id,
                           funds_amount_id)


if __name__ == "__main__":
    def generate_and_delete_account():
        account = create_account(1)
        delete_account(account.account.id)

    def generate_and_transfer_funds():
        account_ids = []
        for i in range(10000):
            account = create_account(5)
            account_ids.append(account.account.id.hex())
            transfer_funds(account_ids[i-1], account_ids[0], 1)

    print('generating 10000 accounts')
    print(timeit.timeit("create_account(1)",
                        "from __main__ import create_account", number=10000))
    print('generating and deleting 10000 accounts')
    print(timeit.timeit("generate_and_delete_account()",
                        "from __main__ import generate_and_delete_account",
                        number=10000))
    print('create 10000 accounts and transfer funds to one account')
    print(timeit.timeit("generate_and_transfer_funds()",
                        "from __main__ import generate_and_transfer_funds",
                        number=1))
