from DensityEquationModel import DensityEquationModel
from VolumeEquationModel import VolumeEquationModel
from ConductivityEquationModel import ConductivityEquationModel

class EquationModelFactory:

    @staticmethod
    def createNew(modelName):
        if modelName == "density":
            return DensityEquationModel()
        elif modelName == "volume":
            return VolumeEquationModel()
        elif modelName == "conductivity":
            return ConductivityEquationModel()
        
        return None
        
