# load the model
loadModel( 'kuzumoto_et_al_2007_2.5Hz.em' )

# create stubs
S_Logger = createLoggerStub( 'Variable:/CELL/MEMBRANE:Vm:Value' )
S_Logger.create()
Vm = createEntityStub( 'Variable:/CELL/MEMBRANE:Vm' )
a = ('Variable:/CELL/MEMBRANE/ICaL:GX')
ICaLGX = createEntityStub(a)
ICaLGX["Value"]=5.0
b = ('Process:/Pipette:I')
PipetteI = createEntityStub(b)
PipetteI["interval"]=200.0
interval1 = PipetteI["interval"]



# print some values
message( 't= \t%s' % getCurrentTime() )
message( 'Vm:Value= \t%s' % Vm.getProperty( 'Value' ) )
message( 'Vm:MolarConc= \t%s' % Vm.getProperty( 'MolarConc' ) )
# run
message( '\n' )
message( 'run %s sec.\n' % interval1 )
run( interval1*4 )


# print results
message( 't= \t%s' % getCurrentTime() )
message( 'Vm:Value= \t%s' % Vm.getProperty( 'Value' ) )
message( 'Vm:MolarConc= \t%s' % Vm.getProperty( 'MolarConc' ) )

message( '\n' )

from ecell.ECDDataFile import *

message('saving ICaL.ecd..')
aDataFile = ECDDataFile( S_Logger.getData(0,800,0.01) )
aDataFile.setDataName( S_Logger.getName() )
aDataFile.setNote( '' )
aDataFile.save( 'ICaL.ecd' )

#message('loading')
#aNewFile = ECDDataFile()
#aNewFile.load( 'S.ecd' )
#print aNewFile.getData()[:10]
