from EquationModel import EquationModel
from TernaryRKModel import TernaryRKModel

class DensityEquationModel(EquationModel):

    residualTag = "DensityEquationModel::residual @"

    def model(self, params, data, verbose = False):
        rho_calc = TernaryRKModel.model(params, data, verbose)
        
        for i in range(len(data)):
            rho_calc[i] = 1.0 / rho_calc[i]
        
        return rho_calc

    def residual(self, params, data, rho, verbose = False):
        rho_calc = self.model(params, data, verbose)
        
        if verbose:
            print DensityEquationModel.residualTag, "rho_calc", rho_calc
            print DensityEquationModel.residualTag, "rho", rho
            print DensityEquationModel.residualTag, "residual", (rho - rho_calc)
        
        return rho - rho_calc
