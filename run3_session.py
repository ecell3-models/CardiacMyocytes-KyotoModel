# load the model
loadModel( 'kuzumoto_et_al_2007_2.5Hz.em' )

# create stubs
S_Logger = createLoggerStub( 'Variable:/CELL/MEMBRANE:Vm:Value' )
S_Logger.create()
Vm = createEntityStub( 'Variable:/CELL/MEMBRANE:Vm' )
a = ('Variable:/CELL/MEMBRANE/IKr:GX')
IKrGX = createEntityStub(a)
x = ('Variable:/CELL/MEMBRANE/IKs:GX')
IKsGX = createEntityStub(x)
b = ('Process:/Pipette:I')
PipetteI = createEntityStub(b)
PipetteI["interval"]=200.0
interval1 = PipetteI["interval"]
values = [0.1,0.5,1,5,10]
for num1 in values:
    for num2 in values:
      IKrGX["Value"] = num1
      IKsGX["Value"] = num2


    # print some values
      message( 'IKrGX= \t%s' % IKrGX.getProperty('Value') )
      message( 'IKsGX= \t%s' % IKsGX.getProperty('Value') )
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

message('saving ICaL2.ecd..')
aDataFile = ECDDataFile( S_Logger.getData(0,4800,0.1) )
aDataFile.setDataName( S_Logger.getName() )
aDataFile.setNote( '' )
aDataFile.save( 'ICaL2.ecd' )

#message('loading')
#aNewFile = ECDDataFile()
#aNewFile.load( 'S.ecd' )
#print aNewFile.getData()[:10]
