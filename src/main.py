import sys
import subprocess
import os
import json
from Config import Config
import lmfit
from lmfit import Minimizer
from OutputFormatter import OutputFormatter
from TernaryRKModel import TernaryRKModel

argc = len(sys.argv)

verbose = False

if argc > 1:
    for i in range(argc):
        if sys.argv[i] == "-v" or sys.argv[i] == "--verbose":
            verbose = True
        else:
            configFileName = sys.argv[i]
else:
    print "Error! An input file must be specified. Call it './ternary-rk-fit <path_to_config_file>'."
    sys.exit()

# unbuffer output
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

logFile = os.path.splitext(configFileName)[0] + ".out"

print "Writing output to './{}' ...".format(logFile)

# tee output to both stdout and file
tee = subprocess.Popen(["tee", logFile], stdin=subprocess.PIPE)
os.dup2(tee.stdin.fileno(), sys.stdout.fileno())
os.dup2(tee.stdin.fileno(), sys.stderr.fileno())

# print program header
OutputFormatter.printHeader()

# open config file
configFile = open(configFileName, 'r', -1)

# parse json data from config file
configJson = json.loads(configFile.read())

# close config file
configFile.close()

# print config JSON info
OutputFormatter.printConfig(configJson)

config = Config(configJson)

# retrieve params from config
equationModel = config.getEquationModel()
params = config.getParams()
data = config.getData()
exp = config.getExp()

OutputFormatter.printExperimentalData(data, exp)

minimizer = Minimizer(equationModel.residual, params, fcn_args=(data, exp, verbose))
out = minimizer.leastsq()

# show output
#lmfit.printfuncs.report_fit(out.params)

print(lmfit.fit_report(out))

# confidence
# ci = lmfit.conf_interval(minimizer, out)

# show output
# lmfit.printfuncs.report_ci(ci)

calc = equationModel.model(params, data, False)

# print results
OutputFormatter.printResults(out, data, exp, calc)
