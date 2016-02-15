from EquationModel import EquationModel
from TernaryRKModel import TernaryRKModel

class VolumeEquationModel(EquationModel):

    residualTag = "VolumeEquationModel::residual @"

    def model(self, params, data, verbose = False):
        return TernaryRKModel.model(params, data, verbose)

    def residual(self, params, data, v, verbose = False):
        v_calc = self.model(params, data, verbose)
        
        if verbose:
            print VolumeEquationModel.residualTag, "v_calc", v_calc
            print VolumeEquationModel.residualTag, "v", v
            print VolumeEquationModel.residualTag, "residual", (v - v_calc)
        
        return v - v_calc
