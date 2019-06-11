@{
"""
Maleckar MM, Greenstein JL, Giles WR, Trayanova NA. K+ current changes account
for the rate dependence of the action potential in the human atrial myocyte. Am J
Physiol Heart Circ Physiol. 2009 Oct;297(4):H1398-410. doi:
10.1152/ajpheart.00411.2009. Epub 2009 Jul 24. PubMed PMID: 19633207; PubMed
Central PMCID: PMC2770776.
"""

# initial values of Variables
IKur_I = 0.0

IKur_g = {
	"V"   : 0.0,
	"A"   : 2.5e-4,
	"EMB" : 0.0,
	"LAT" : 0.0,
	"NEO" : 0.0,
	"SAN" : 0.0,
}

}

System System(/CELL/MEMBRANE/IKur)
{
	StepperID	ODE;

	Variable Variable( I )
	{
		Value @IKur_I;
	}

	Variable Variable( aur )
	{
		Value 3.67e-4;
	}

	Variable Variable( iur )
	{
		Value 0.9673;
	}

	Variable Variable( v_aur )
	{
		Value 0.0;
	}

	Variable Variable( v_iur )
	{
		Value 0.0;
	}

	Variable Variable( GX ){
		Value @( Kv1_5[SimulationMode]);
	}

	Process IKurAssignmentProcess( I )
	{
		StepperID	PSV;
		Priority	20;

		VariableReferenceList
			[ Vm     :..:Vm     0 ]
			[ EK     :..:EK     0 ]
			[ aur    :.:aur     0 ]
			[ iur    :.:iur     0 ]
			[ v_aur  :.:v_aur   1 ]
			[ v_iur  :.:v_iur   1 ]
			[ GX     :.:GX      0 ]
			[ Cm     :..:Cm     0 ]
			[ I      :.:I       1 ];

		g   @( IKur_g[SimulationMode]);
	}


	Process ZeroVariableAsFluxProcess( v_aur )
	{
		Priority	15;

		VariableReferenceList
			[ aur   :.:aur    1 ]
			[ v_aur :.:v_aur  0 ];
	}

	Process ZeroVariableAsFluxProcess( v_iur )
	{
		Priority	15;

		VariableReferenceList
			[ iur   :.:iur    1 ]
			[ v_iur :.:v_iur  0 ];
	}

	@setCurrents( [ 'I' ], [ 'K', 'I' ] )

}