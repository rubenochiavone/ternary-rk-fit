from RedlichKisterEquation import RedlichKisterEquation

class TernaryRKModel:

    modelTag = "TernaryRKModel::model @"
    
    @staticmethod
    def model(params, data, verbose = False):
        n = range(len(data))
        
        z1 = data[:, 0]  # compound #1 composition data
        z2 = data[:, 1]  # compound #2 composition data
        z3 = data[:, 2]  # compound #3 composition data
        T = data[:, 3]   # temperature data
        
        if verbose:
            print TernaryRKModel.modelTag, "z1", z1
            print TernaryRKModel.modelTag, "z2", z2
            print TernaryRKModel.modelTag, "z3", z3
        
        c1 = params['c1'].value # compound #1 density
        c2 = params['c2'].value # compound #2 density
        c3 = params['c3'].value # compound #3 density
        
        rkp12 = []
        rkp12.append(params['rkp12_1'].value) # #1 redlich-kister parameter for 1-2 compound composition
        rkp12.append(params['rkp12_2'].value) # #2 redlich-kister parameter for 1-2 compound composition
        rkp12.append(params['rkp12_3'].value) # #3 redlich-kister parameter for 1-2 compound composition
        
        rkp13 = []
        rkp13.append(params['rkp13_1'].value) # #1 redlich-kister parameter for 1-3 compound composition
        rkp13.append(params['rkp13_2'].value) # #2 redlich-kister parameter for 1-3 compound composition
        rkp13.append(params['rkp13_3'].value) # #3 redlich-kister parameter for 1-3 compound composition
        
        rkp23 = []
        rkp23.append(params['rkp23_1'].value) # #1 redlich-kister parameter for 2-3 compound composition
        rkp23.append(params['rkp23_2'].value) # #2 redlich-kister parameter for 2-3 compound composition
        rkp23.append(params['rkp23_3'].value) # #3 redlich-kister parameter for 2-3 compound composition
        
        rkp123 = []
        rkp123.append(params['rkp123_1'].value) # #1 redlich-kister parameter for 1-2-3 compound composition
        rkp123.append(params['rkp123_2'].value) # #2 redlich-kister parameter for 1-2-3 compound composition
        rkp123.append(params['rkp123_3'].value) # #3 redlich-kister parameter for 1-2-3 compound composition
        
        # ideal
        id1 = z1 * c1
        id2 = z2 * c2
        id3 = z3 * c3
        
        ideal = id1 + id2 + id3
        
        # compounds contributions
        contrib12 = []
        contrib13 = []
        contrib23 = []
        contrib123 = []
        excess = []
        
        for i in n:
            
            # binaries
            contrib12.append(z1[i] * z2[i] * RedlichKisterEquation.calculate(rkp12, z1[i], z2[i]))
            
            contrib13.append(z1[i] * z3[i] * RedlichKisterEquation.calculate(rkp13, z1[i], z3[i]))
            
            contrib23.append(z2[i] * z3[i] * RedlichKisterEquation.calculate(rkp23, z2[i], z3[i]))
            
            # ternary
            contrib123.append(z1[i] * z2[i] * z3[i] * (rkp123[0] + (rkp123[1] * z1[i]) + (rkp123[2] * z2[i])))
            
            # excess
            excess.append(contrib12[i] + contrib13[i] + contrib23[i] + contrib123[i])
        
        calc = []
        
        for i in n:
            calc.append(ideal[i] + excess[i])
        
        if verbose:
            print TernaryRKModel.modelTag, "ideal", ideal
            print TernaryRKModel.modelTag, "12 contribution", contrib12
            print TernaryRKModel.modelTag, "13 contribution", contrib13
            print TernaryRKModel.modelTag, "23 contribution", contrib23
            print TernaryRKModel.modelTag, "123 contribution", contrib123
            print TernaryRKModel.modelTag, "excess", excess
            print TernaryRKModel.modelTag, "calculated", calc
        
        return calc

