from RedlichKisterEquation import RedlichKisterEquation

class TernaryRKModel:

    modelTag = "TernaryRKModel::model @"
    residualTag = "TernaryRKModel::residual @"
    
    @staticmethod
    def model(params, data, verbose = False):
        z1 = data[:, 0]  # compound #1 composition data
        z2 = data[:, 1]  # compound #2 composition data
        z3 = data[:, 2]  # compound #3 composition data
        T = data[:, 3]   # temperature data
        
        if verbose:
            print TernaryRKModel.modelTag, "z1", z1
            print TernaryRKModel.modelTag, "z2", z2
            print TernaryRKModel.modelTag, "z3", z3
        
        d1 = params['d1'].value # compound #1 density
        d2 = params['d2'].value # compound #2 density
        d3 = params['d3'].value # compound #3 density
        
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
        
        # ideal volume
        # ternary expression to avoid division by zero
        vid1 = (z1 / d1) if d1 != 0 else 0
        vid2 = (z2 / d2) if d2 != 0 else 0
        vid3 = (z3 / d3) if d3 != 0 else 0
        
        vid = vid1 + vid2 + vid3
        
        # 
        vs12 = 0
        vs13 = 0
        vs23 = 0
        vs123 = 0
        
        for i in range(len(data)):
            
            # binaries
            vs12 += z1[i] * z2[i] * RedlichKisterEquation.calculate(rkp12, z1[i], z2[i])
            
            vs13 += z1[i] * z3[i] * RedlichKisterEquation.calculate(rkp13, z1[i], z3[i])
            
            vs23 += z2[i] * z3[i] * RedlichKisterEquation.calculate(rkp23, z2[i], z3[i])
        
            # ternary
            vs123 += z1[i] * z2[i] * z3[i] * (rkp123[0] + (rkp123[1] * z1[i]) + (rkp123[2] * z2[i]))
        
        # excess volume
        vexcess = vs12 + vs13 + vs23 + vs123
        
        # volume
        y = vid + vexcess
        
        # getting density
        for i, value in enumerate(y):
            y[i] = 1. / value
        
        if verbose:
            print TernaryRKModel.modelTag, "ideal volume", vid
            print TernaryRKModel.modelTag, "12 contribution", vs12
            print TernaryRKModel.modelTag, "13 contribution", vs13
            print TernaryRKModel.modelTag, "23 contribution", vs23
            print TernaryRKModel.modelTag, "123 contribution", vs123
            print TernaryRKModel.modelTag, "excess volume", vexcess
            print TernaryRKModel.modelTag, "y calculated", y
        
        return y
    
    @staticmethod
    def residual(params, data, rho, verbose = False):
        rho_calc = TernaryRKModel.model(params, data, False)
        
        if verbose:
            print TernaryRKModel.residualTag, "rho", rho
            print TernaryRKModel.residualTag, "residual", (rho - rho_calc)
        
        return rho - rho_calc
    
    @staticmethod
    def printResults(out, data, rho):
        rho_calc = TernaryRKModel.model(out.params, data)

        print "[[Results]]"
        print "   ", "rho", "\t", "rho_calc", "\t\t", "err"

        errsum = 0

        mxdev = 0

        for i in range(len(data)):
            err = abs(rho[i] - rho_calc[i])
            
            if err > mxdev:
                mxdev = err
            
            errsum += err
            
            print "   ", rho[i], "\t", rho_calc[i], "\t", err

        # mean deviation
        mndev = errsum / len(data)


        print "    "

        print "    Mean deviation:", mndev
        print "    Max deviation: ", mxdev

