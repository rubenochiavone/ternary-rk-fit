from EquationModelFactory import EquationModelFactory
from DensityEquationModel import DensityEquationModel
from lmfit import Parameters
from lmfit import Parameter
import numpy as np

class Config:
    
    def __init__(self, config):
        
        defaultRkpVary = True
        defaultRkpMin = float("-inf")
        defaultRkpMax = float("inf")
        
        params = Parameters()
        
        try:
            equationModel = EquationModelFactory.createNew(config['equation'])
            
            if config['equation'] == "density":
                params['c1'] = Parameter('c1', value=config['compounds'][0]['density'], vary=False)
                params['c2'] = Parameter('c2', value=config['compounds'][1]['density'], vary=False)
                params['c3'] = Parameter('c3', value=config['compounds'][2]['density'], vary=False)
            elif config['equation'] == "volume":
                params['c1'] = Parameter('c1', value=config['compounds'][0]['density'], vary=False)
                params['c2'] = Parameter('c2', value=config['compounds'][1]['density'], vary=False)
                params['c3'] = Parameter('c3', value=config['compounds'][2]['density'], vary=False)
            elif config['equation'] == "conductivity":
                params['c1'] = Parameter('c1', value=config['compounds'][0]['conductivity'], vary=False)
                params['c2'] = Parameter('c2', value=config['compounds'][1]['conductivity'], vary=False)
                params['c3'] = Parameter('c3', value=config['compounds'][2]['conductivity'], vary=False)
            else:
                raise ValueError("Unknown equation '{}'".format(config['equation']))
        except KeyError:
            print "Equation parameter must be set. Using 'density' equation ..."
            
            equationModel = DensityEquationModel()
            
            params['c1'] = Parameter('c1', value=config['compounds'][0]['density'], vary=False)
            params['c2'] = Parameter('c2', value=config['compounds'][1]['density'], vary=False)
            params['c3'] = Parameter('c3', value=config['compounds'][2]['density'], vary=False)

        rkp12Conf = config['binary']['rkp']['x1-x2']
        
        params['rkp12_1'] = \
                Parameter('rkp12_1', \
                        value=rkp12Conf[0]['value'],
                        vary=(rkp12Conf[0]['vary'] if 'vary' in rkp12Conf[0] else defaultRkpVary), \
                        min=(rkp12Conf[0]['min'] if 'min' in rkp12Conf[0] else defaultRkpMin), \
                        max=(rkp12Conf[0]['max'] if 'max' in rkp12Conf[0] else defaultRkpMax))
        params['rkp12_2'] = \
                Parameter('rkp12_2', \
                        value=rkp12Conf[1]['value'],
                        vary=(rkp12Conf[1]['vary'] if 'vary' in rkp12Conf[1] else defaultRkpVary), \
                        min=(rkp12Conf[1]['min'] if 'min' in rkp12Conf[1] else defaultRkpMin), \
                        max=(rkp12Conf[1]['max'] if 'max' in rkp12Conf[1] else defaultRkpMax))
        params['rkp12_3'] = \
                Parameter('rkp12_3', \
                        value=rkp12Conf[2]['value'],
                        vary=(rkp12Conf[2]['vary'] if 'vary' in rkp12Conf[2] else defaultRkpVary), \
                        min=(rkp12Conf[2]['min'] if 'min' in rkp12Conf[2] else defaultRkpMin), \
                        max=(rkp12Conf[2]['max'] if 'max' in rkp12Conf[2] else defaultRkpMax))

        rkp13Conf = config['binary']['rkp']['x1-x3']
        
        params['rkp13_1'] = \
                Parameter('rkp13_1', \
                        value=rkp13Conf[0]['value'],
                        vary=(rkp13Conf[0]['vary'] if 'vary' in rkp13Conf[0] else defaultRkpVary), \
                        min=(rkp13Conf[0]['min'] if 'min' in rkp13Conf[0] else defaultRkpMin), \
                        max=(rkp13Conf[0]['max'] if 'max' in rkp13Conf[0] else defaultRkpMax))
        params['rkp13_2'] = \
                Parameter('rkp13_2', \
                        value=rkp13Conf[1]['value'],
                        vary=(rkp13Conf[1]['vary'] if 'vary' in rkp13Conf[1] else defaultRkpVary), \
                        min=(rkp13Conf[1]['min'] if 'min' in rkp13Conf[1] else defaultRkpMin), \
                        max=(rkp13Conf[1]['max'] if 'max' in rkp13Conf[1] else defaultRkpMax))
        params['rkp13_3'] = \
                Parameter('rkp13_3', \
                        value=rkp13Conf[2]['value'],
                        vary=(rkp13Conf[2]['vary'] if 'vary' in rkp13Conf[2] else defaultRkpVary), \
                        min=(rkp13Conf[2]['min'] if 'min' in rkp13Conf[2] else defaultRkpMin), \
                        max=(rkp13Conf[2]['max'] if 'max' in rkp13Conf[2] else defaultRkpMax))

        
        rkp23Conf = config['binary']['rkp']['x2-x3']
        
        params['rkp23_1'] = \
                Parameter('rkp23_1', \
                        value=rkp23Conf[0]['value'],
                        vary=(rkp23Conf[0]['vary'] if 'vary' in rkp23Conf[0] else defaultRkpVary), \
                        min=(rkp23Conf[0]['min'] if 'min' in rkp23Conf[0] else defaultRkpMin), \
                        max=(rkp23Conf[0]['max'] if 'max' in rkp23Conf[0] else defaultRkpMax))
        params['rkp23_2'] = \
                Parameter('rkp23_2', \
                        value=rkp23Conf[1]['value'],
                        vary=(rkp23Conf[1]['vary'] if 'vary' in rkp23Conf[1] else defaultRkpVary), \
                        min=(rkp23Conf[1]['min'] if 'min' in rkp23Conf[1] else defaultRkpMin), \
                        max=(rkp23Conf[1]['max'] if 'max' in rkp23Conf[1] else defaultRkpMax))
        params['rkp23_3'] = \
                Parameter('rkp23_3', \
                        value=rkp23Conf[2]['value'],
                        vary=(rkp23Conf[2]['vary'] if 'vary' in rkp23Conf[2] else defaultRkpVary), \
                        min=(rkp23Conf[2]['min'] if 'min' in rkp23Conf[2] else defaultRkpMin), \
                        max=(rkp23Conf[2]['max'] if 'max' in rkp23Conf[2] else defaultRkpMax))

        rkp123Conf = config['ternary']['rkp']
        
        params['rkp123_1'] = \
                Parameter('rkp123_1', \
                        value=rkp123Conf[0]['value'],
                        vary=(rkp123Conf[0]['vary'] if 'vary' in rkp123Conf[0] else defaultRkpVary), \
                        min=(rkp123Conf[0]['min'] if 'min' in rkp123Conf[0] else defaultRkpMin), \
                        max=(rkp123Conf[0]['max'] if 'max' in rkp123Conf[0] else defaultRkpMax))
        params['rkp123_2'] = \
                Parameter('rkp123_2', \
                        value=rkp123Conf[1]['value'],
                        vary=(rkp123Conf[1]['vary'] if 'vary' in rkp123Conf[1] else defaultRkpVary), \
                        min=(rkp123Conf[1]['min'] if 'min' in rkp123Conf[1] else defaultRkpMin), \
                        max=(rkp123Conf[1]['max'] if 'max' in rkp123Conf[1] else defaultRkpMax))
        params['rkp123_3'] = \
                Parameter('rkp123_3', \
                        value=rkp123Conf[2]['value'],
                        vary=(rkp123Conf[2]['vary'] if 'vary' in rkp123Conf[2] else defaultRkpVary), \
                        min=(rkp123Conf[2]['min'] if 'min' in rkp123Conf[2] else defaultRkpMin), \
                        max=(rkp123Conf[2]['max'] if 'max' in rkp123Conf[2] else defaultRkpMax))
        
        # data
        
        rawdata = np.array(config['data'])
        
        rawdataLength = len(rawdata)
        
        data = np.delete(rawdata, 4, 1)

        exp = np.delete(rawdata, [0, 1, 2, 3], 1).reshape((rawdataLength,))
        
        self.equationModel = equationModel
        self.params = params
        self.data = data
        self.exp = exp
        
    def getEquationModel(self):
        return self.equationModel
    
    def getParams(self):
        return self.params
    
    def getData(self):
        return self.data
    
    def getExp(self):
        return self.exp
