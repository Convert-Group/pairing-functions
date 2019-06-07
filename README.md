# pairing-functions

A pairing function is a function that *reversibly* maps two non-negative integers onto a single non-negative integer.


This package currently supports the following pairing functions:

- **Szudzik pairing function**


## Install

Simply:

    $ pip install pairing-functions

## Usage

    from pairing_functions.szudzik import pairing

    pair((3, 4))  
    // 19
    
    unpair(19)
    // (3, 4)
    
You can also work with more than 2 integers:
    
    pair((1, 2, 3, 4))
    //1126
    
    # by default, unpairing will result in two integers
    
    unpair(1126)
    // (33, 4)
    
    # but going back to the start is also possible - just specify how many integers you expect !
    
    unpair(1126, n=4)
    // (1, 2, 3, 4)

Documentation
-------------

You can find more about pairing functions in the [docs](docs/pairing_functions.md).


How to contribute
-------------

If you wish to contribute, you can start from [here](CONTRIBUTING.md) !