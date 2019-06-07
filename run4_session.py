
# load the model
loadModel( 'takahashi.em' )

# create stubs
S_Logger = createLoggerStub( 'Variable:/CELL/MEMBRANE:Vm:Value' )
S_Logger.create()
Vm = createEntityStub( 'Variable:/CELL/MEMBRANE:Vm' )



# print some values
message( 't= \t%s' % getCurrentTime() )
message( 'Vm:Value= \t%s' % Vm.getProperty( 'Value' ) )
message( 'Vm:MolarConc= \t%s' % Vm.getProperty( 'MolarConc' ) )
# run
duration = 1000
message( '\n' )
message( 'run %s sec.\n' % duration )
run( duration*10 )


# print results
message( 't= \t%s' % getCurrentTime() )
message( 'Vm:Value= \t%s' % Vm.getProperty( 'Value' ) )
message( 'Vm:MolarConc= \t%s' % Vm.getProperty( 'MolarConc' ) )

message( '\n' )

from ecell.ECDDataFile import *

message('saving Atrial2.ecd..')
aDataFile = ECDDataFile( S_Logger.getData(7000,10000,.5) )
aDataFile.setDataName( S_Logger.getName() )
aDataFile.setNote( '' )
aDataFile.save( 'Atrial2.ecd' )
