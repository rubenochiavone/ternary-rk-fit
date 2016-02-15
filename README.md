# ternary-rk-fit

Curve fitting of ternary Redlich-Kister (RK) equation.

## Redlich-Kister equation

@TODO: write a section about Redlich-Kister equation.

## Requirements

**ternary-rk-fit** depends on the `lmfit` python library. It performs Levenberg-Marquardt algorithm curve fitting algorithm and many more - take a look at their [site](http://cars9.uchicago.edu/software/python/lmfit/ "lmfit").

In order to install it type:

```
$ sudo apt-get install python-numpy python-scipy python-matplotlib ipython \
        ipython-notebook python-pandas python-sympy python-nose python-pip
$ sudo pip install lmfit
```

## Exec

There is an executable file called `ternary-rk-fit` that can run the **ternary-rk-fit** program. To run it specify an input config file:

`$ ./ternary-rk-fit <path_to_config_file>`

### Input samples

There are 5 samples of how to config **ternary-rk-fit**:

- `config/water_meg.json` - calculates Water and MEG binary RK parameters at 298.15 K experimental data using density equation
- `config/water_nacl.json` - calculates Water and NaCl binary RK parameters at 298.15 K experimental data using density equation
- `config/meg_nacl.json` - calculates MEG and NaCl RK binary parameters at 298.15 K experimental data using density equation
- `config/ternary.json` - calculates Water, MEG and NaCl ternary RK parameters at 298.15 K experimental data using density equation
- `config/volume_ternary.json` - calculates Water, MEG and NaCl ternary RK parameters at 298.15 K experimental data using volume equation

To test one of them do the following:

`$ ./ternary-rk-fit config/water_meg.json`

All output written to `stdout` will be write to `config/water_meg.out` file simultaneously.

## Authors

- Osvaldo Chiavone Filho (osvaldo@eq.ufrn.br) - [site](http://nupeg.ufrn.br "nupeg")
- Ruben O. Chiavone (rubenochiavone@gmail.com) - [GitHub](https://github.com/rubenochiavone "rubenochiavone")

Enjoy!

