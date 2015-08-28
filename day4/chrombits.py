import numpy
import copy

class ChromosomeLocationBitArrays( object ):

    def __init__( self, dicts=None, fname=None ):
        # If dicts parameter provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        # If fname parameter provided, initialize from file
        if fname is not None: 
            for line in open( fname ):
                fields = line.split()
                name = fields[0]
                size = int( fields[1] )
                arrays[name] = numpy.zeros( size, dtype=bool )
        self.arrays = arrays

    def set_bits_from_file( self, fname ):
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            self.arrays[ chrom ][ start : end ] = 1
            
    def bed_from_bit(self):
        I = []
        II =[]
        III = []
        for chrom in self.arrays:
            counter = 0
            I.append(chrom)
            for x in self.arrays[chrom]:
                if x == False:
                    counter += 1
                if x == True:
                    II.append(counter)
                    counter += 1
                    while self.arrays[chrom][counter] == True:
                        counter += 1
                    III.append(counter -1)                  
            return I, II, III
        
    def intersect( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def union( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def complement( self ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~ self.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def copy( self ):
        return ChromosomeLocationBitArrays( 
            dicts=copy.deepcopy( self.arrays ) )