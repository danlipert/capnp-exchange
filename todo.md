### Current Issues
The data types for the IDs in `account.capnp` aren't congruent. The account `id` is `Data` while the arguments for the methods are `Text`. This is a fix for some encoding issues with the current pycapnp implementation of generating random bytes for the `id` but encoding them as hex for testing and debugging purposes. In addition, there are some internal encoding functions in pycapnp that attempt to encode the bytes as a utf-8 string, more debugging will be needed to understand the best way to pass ids.

### Todo

- Fix type of account ids from `Text` to `Data`
- Add some sort of business logic (ex: cannot transfer more funds than current balance)
- Add tests for business logic
- Add benchmarks

### Potential Improvements
- Use Redis or other efficient storage to add robustness, some persistence
- Add longer term data storage async write (i.e. SQL, etc.) for full persistence
