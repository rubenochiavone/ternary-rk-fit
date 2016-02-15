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
        print "Authors: Osvaldo Chiavone Filho (osvaldo@eq.ufrn.br) and Ruben O. Chiavone"
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
                
        try:
            modelName = config['equation']
            
            if modelName == "density":
                print "    Using density equation"
                print ""
                print "    x1.density =", config['compounds'][0]['density']
                print "    x2.density =", config['compounds'][1]['density']
                print "    x3.density =", config['compounds'][2]['density']
            elif modelName == "volume":
                print "    Using volume equation"
                print ""
                print "    x1.volume =", config['compounds'][0]['volume']
                print "    x2.volume =", config['compounds'][1]['volume']
                print "    x3.volume =", config['compounds'][2]['volume']
            elif modelName == "conductivity":
                print "    Using conductivity equation"
                print ""
                print "    x1.conductivity =", config['compounds'][0]['conductivity']
                print "    x2.conductivity =", config['compounds'][1]['conductivity']
                print "    x3.conductivity =", config['compounds'][2]['conductivity']
            else:
                print "    Unknown equation '{}'".format(config['equation'])
        except KeyError:
            print "    Equation parameter must be set. Using density equation as default"
            print ""
            print "    x1.density =", config['compounds'][0]['density']
            print "    x2.density =", config['compounds'][1]['density']
            print "    x3.density =", config['compounds'][2]['density']
        
    
    @staticmethod
    def printExperimentaldata(data, exp):
        z1 = data[:, 0] # compound #1 composition data
        z2 = data[:, 1] # compound #2 composition data
        z3 = data[:, 2] # compound #3 composition data
        T = data[:, 3]  # temperature data
        
        print "[[Experimental Data]]"
        
        print "      z1", "      ", "z2", "       ", "z3", "      ", \
                "T", "     ", " exp"
        
        for i in range(len(data)):
            print "    {0:1.5f}   {1:1.5f}    {2:1.5f}   {3:3.2f}   {4:1.5f}" \
                    .format(z1[i], z2[i], z3[i], T[i], exp[i])
    
    @staticmethod
    def printResults(out, data, exp, calc):
        z1 = data[:, 0] # compound #1 composition data
        z2 = data[:, 1] # compound #2 composition data
        z3 = data[:, 2] # compound #3 composition data
        T = data[:, 3]  # temperature data
        
        print "[[Results]]"
        print "      z1", "      ", "z2", "       ", "z3", "      ", \
                "T", "     ", " exp", "    ", "calc", "     ", "err"

        errsum = 0
        errpersum = 0

        # max deviation
        mxdev = 0
        
        for i in range(len(data)):
            err = abs(exp[i] - calc[i])
            
            if err > mxdev:
                mxdev = err
            
            errsum += err
            
            print "    {0:1.5f}   {1:1.5f}    {2:1.5f}   {3:3.2f}   {4:1.5f}   {5:.5f}   {6:.7f}" \
                    .format(z1[i], z2[i], z3[i], T[i], exp[i], calc[i], err)

        # mean deviation
        mndev = errsum / len(data)


        print "    "

        print "    Mean deviation: {0:5.9f}".format(mndev)
        print "    Max deviation:  {0:5.9f}".format(mxdev)

