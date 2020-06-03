# pairing-functions

A pairing function is a function that *reversibly* maps two non-negative integers onto a single non-negative integer.

This package currently supports the following pairing functions:

- **Szudzik pairing function**
- **Cantor pairing function**


Install
-------

Simply:
```shell script
$ pip install pairing-functions
```
 
Usage
-----
```python
from pairing_functions import cantor, szudzik

szudzik.pair(3, 4)  
// 19

szudzik.unpair(19)
// (3, 4)

cantor.pair(3, 4)  
// 32

cantor.unpair(32)
// (3, 4)
```

You can also work with more than 2 integers:

```python
from pairing_functions import cantor, szudzik

szudzik.pair(1, 2, 3, 4)
// 1126

cantor.pair(1, 2, 3, 4)
// 2705

# by default, unpairing will result in two integers

szudzik.unpair(1126)
// (33, 4)

cantor.unpair(2705)
// (69, 4)

# but going back to the initial integers is also possible - just specify how many integers you expect !

szudzik.unpair(1126, n=4)
// (1, 2, 3, 4)

cantor.unpair(2705, n=4)
// (1, 2, 3, 4)
```
    
Documentation
-------------
You can find more about pairing functions in the [docs](docs/pairing_functions.md).

How to contribute
-----------------
If you wish to contribute, you can start from [here](CONTRIBUTING.md) !

Test
----
You can run the available tests with [pytest](https://docs.pytest.org/en/latest/) - code coverage metrics are also available via [pytest-cov](https://github.com/pytest-dev/pytest-cov).