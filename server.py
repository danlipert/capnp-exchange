import secrets

import capnp

import account_capnp

accounts = {}

class AccountServer(account_capnp.Accounts.Server):

    def createAccount(self, **kwargs):
        print("creating account")
        rand_id = secrets.token_bytes(32)
        new_account = account_capnp.Accounts.Account.new_message(
            id=rand_id, balance=kwargs['initialBalance'])
        accounts[new_account.id.hex()] = new_account
        return new_account

    def deleteAccount(self, **kwargs):
        print("deleting account")
        accounts.pop(kwargs['accountId'])

    def transferFunds(self, **kwargs):
        print("transfer funds")
        source_account_id = kwargs['sourceAccountId']
        destination_account_id = kwargs['destinationAccountId']
        funds_amount = kwargs['fundsAmount']

        accounts[source_account_id].balance -= funds_amount
        accounts[destination_account_id].balance += funds_amount

server = capnp.TwoPartyServer("*:60000", bootstrap=AccountServer())
print('booting server...')
server.run_forever()
