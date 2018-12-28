### Current Issues
The data types for the IDs in `account.capnp` aren't congruent. The account `id` is `Data` while the arguments for the methods are `Text`. This is a fix for some encoding issues with the current pycapnp implementation of generating random bytes for the `id` but encoding them as hex for testing and debugging purposes. In addition, there are some internal encoding functions in pycapnp that attempt to encode the bytes as a utf-8 string, more debugging will be needed to understand the best way to pass ids.

### Todo

- [ ] Fix type of account ids from `Text` to `Data`
- [ ] Add some sort of business logic (ex: cannot transfer more funds than current balance)
- [ ] Add tests for business logic
- [x] Add benchmarks

### Potential Improvements
- Use Redis or other efficient storage to add robustness, some persistence
- Add longer term data storage async write (i.e. SQL, etc.) for full persistence

### Current benchmarks
Performed on a 2017 Macbook Air 1.8 Ghz i5 / 8 GB RAM

    `generating 10000 accounts  
    4.384568012988893  
    generating and deleting 10000 accounts
    9.855974756996147
    create 10000 accounts and transfer funds to one account
    10.997326050011907`

    `generating 10000 accounts
    5.884779487008927
    generating and deleting 10000 accounts
    11.113609858992277
    create 10000 accounts and transfer funds to one account
    9.053881350002484`

    `generating 10000 accounts
    4.3889953900070395
    generating and deleting 10000 accounts
    10.03580996999517
    create 10000 accounts and transfer funds to one account
    8.624133358011022`
