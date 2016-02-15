from EquationModel import EquationModel
from TernaryRKModel import TernaryRKModel

class ConductivityEquationModel(EquationModel):

    residualTag = "ConductivityEquationModel::residual @"

    def model(self, params, data, verbose = False):
        return TernaryRKModel.model(params, data, verbose)
    
    def residual(self, params, data, k, verbose = False):
        k_calc = self.model(params, data, verbose)
        
        if verbose:
            print ConductivityEquationModel.residualTag, "k_calc", k_calc
            print ConductivityEquationModel.residualTag, "k", k
            print ConductivityEquationModel.residualTag, "residual", (k - k_calc)
        
        return k - k_calc
