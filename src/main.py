import sys
import json
from Config import Config
import lmfit
from lmfit import Minimizer
from TernaryRKModel import TernaryRKModel

# default config file
configFileName = "config.json"

if len(sys.argv) > 1:
    # override default file
    configFileName = sys.argv[1]

# open config file
configFile = open(configFileName, 'r', -1)

# parse json data from config file
configJson = json.loads(configFile.read())

# close config file
configFile.close()

config = Config(configJson)

# retrieve params from config
params = config.getParams()
data = config.getData()
rho = config.getRho()

minimizer = Minimizer(TernaryRKModel.residual, params, fcn_args=(data, rho))
out = minimizer.leastsq()

# show output
#lmfit.printfuncs.report_fit(out.params)

print(lmfit.fit_report(out))

# confidence
# ci = lmfit.conf_interval(minimizer, out)

# show output
# lmfit.printfuncs.report_ci(ci)

TernaryRKModel.printResults(out, data, rho)
