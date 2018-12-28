@0xa44beceeaf4e8d2f;

interface Accounts {
    struct Account {
        # 32 byte id
        id @0 :Data;

        # must be careful here depending on asset type - 256 bit precision can be
        # used for some cryptocurrencies (i.e. ERC20)
        balance @1 :UInt64;
    }

    createAccount @0 (initialBalance :UInt64) -> (account :Account);

    deleteAccount @1 (accountId :Text);

    transferFunds @2 (sourceAccountId :Text,
                      destinationAccountId :Text,
                      fundsAmount :UInt64);
}
