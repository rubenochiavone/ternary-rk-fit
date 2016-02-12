# ternary-rk-fit

Curve fitting of ternary Redlich-Kister equation.

## Redlich-Kister equation

@TODO: write a section about Redlich-Kister equation.

## Requirements

**ternary-rk-fit** depends on the `lmfit` python library. It performs Levenberg-Marquardt algorithm curve fitting algorithm and many more - take a look at [site](http://cars9.uchicago.edu/software/python/lmfit/ "lmfit"). In order to install it type:

```
$ sudo apt-get install python-numpy python-scipy python-matplotlib ipython \
        ipython-notebook python-pandas python-sympy python-nose python-pip
$ sudo pip install lmfit
```

## Exec

There is an executable file called `ternary-rk-fit` that can run the **ternary-rk-fit** program. It uses default configuration file called `config.json`.

`$ ./ternary-rk-fit`

to specify another config file do:

`$ ./ternary-rk-fit <path_to_config_file>`

### Input samples

There are 4 samples of how to config **ternary-rk-fit**:

- water_meg.json
- water_nacl.json
- meg_nacl.json
- ternary.json

To test one of them do the following:

`$ ./ternary-rk-fit water_meg.json`

Enjoy!

