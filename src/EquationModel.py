from TernaryRKModel import TernaryRKModel

class EquationModel:

    residualTag = "EquationModel::residual @"

    def model(self, params, data, verbose = False):
        return TernaryRKModel.model(params, data, verbose)

    def residual(self, params, data, exp, verbose = False):
        calc = self.model(params, data, verbose)
        
        if verbose:
            print EquationModel.residualTag, "calc", calc
            print EquationModel.residualTag, "exp", exp
            print EquationModel.residualTag, "residual", (exp - calc)
        
        return exp - calc
