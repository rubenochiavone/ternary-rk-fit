from TernaryRKModel import TernaryRKModel

class OutputFormatter:

    @staticmethod
    def printHeader():
        
        print ""
        print "  @@@@@@@@@@@@@@@@@@@@@@@@@@"
        print "  @@@                    @@@"
        print "  @@@   ternary-rk-fit   @@@"
        print "  @@@                    @@@"
        print "  @@@@@@@@@@@@@@@@@@@@@@@@@@"
        print ""
        print "Performs curve fitting of ternary Redlich-Kister equation"
        print "Authors: Osvaldo Chiavone Filho (osvaldo@nupeg.ufrn.br) and Ruben O. Chiavone"
        print "UFRN - 2016"
        print ""

    @staticmethod
    def printConfig(config):
        
        #TODO: 
        
        print "[[Configurations]]"
        
        print "    x1 =", config['compounds'][0]['name']
        print "    x2 =", config['compounds'][1]['name']
        print "    x3 =", config['compounds'][2]['name']
        print ""
        print "    x1.density =", config['compounds'][0]['density']
        print "    x2.density =", config['compounds'][1]['density']
        print "    x3.density =", config['compounds'][2]['density']
        
    
    @staticmethod
    def printExperimentaldata(data, rho):
        z1 = data[:, 0] # compound #1 composition data
        z2 = data[:, 1] # compound #2 composition data
        z3 = data[:, 2] # compound #3 composition data
        T = data[:, 3]  # temperature data
        
        print "[[Experimental Data]]"
        
        print "      z1", "      ", "z2", "       ", "z3", "      ", \
                "T", "     ", " rho"
        
        for i in range(len(data)):
            print "    {0:1.5f}   {1:1.5f}    {2:1.5f}   {3:3.2f}   {4:1.5f}" \
                    .format(z1[i], z2[i], z3[i], T[i], rho[i])
    
    @staticmethod
    def printResults(out, data, rho):
        z1 = data[:, 0] # compound #1 composition data
        z2 = data[:, 1] # compound #2 composition data
        z3 = data[:, 2] # compound #3 composition data
        T = data[:, 3]  # temperature data
        
        rho_calc = TernaryRKModel.model(out.params, data)

        print "[[Results]]"
        print "      z1", "      ", "z2", "       ", "z3", "      ", \
                "T", "     ", " rho", "   ", "rho_clc", "    ", "err"

        errsum = 0

        mxdev = 0

        for i in range(len(data)):
            err = abs(rho[i] - rho_calc[i])
            
            if err > mxdev:
                mxdev = err
            
            errsum += err
            
            print "    {0:1.5f}   {1:1.5f}    {2:1.5f}   {3:3.2f}   {4:1.5f}   {5:.5f}   {6:.7f}" \
                    .format(z1[i], z2[i], z3[i], T[i], rho[i], rho_calc[i], err)

        # mean deviation
        mndev = errsum / len(data)


        print "    "

        print "    Mean deviation: {0:5.9f}".format(mndev)
        print "    Max deviation:  {0:5.9f}".format(mxdev)

