

	Variable Variable( Vmaxr_CK )
	{
		Value 500.0;
	}

	Variable Variable( VCK_GX )
	{
#		Value @( Lambeth[Glycolysis]);
		Value 1.0;
	}


	Process CK_Process( V_CK )
	{
		StepperID  ODE;
		Priority   0;

		VariableReferenceList
			[ VCK_maxr :.:Vmaxr_CK   0 ]
			[ PCr      :.:PCr   1 ]
			[ ADP      :.:ADPtotal   1 ]
			[ Cr       :.:Creatine   0 ]
#			[ Cr       :.:Cr   -1 ]
			[ ATP      :.:ATPtotal   -1 ]
			[ GX      :.:VCK_GX   0 ];
			
		KCK_PCr 1.11;
		KCK_iATP 3.5;
		KCK_iADP 0.135;
		KCK_iPCr 3.9;
		KCK_Cr 3.8;
		KCK_eq 233.0;

#		ADP.addDydt(V_PFK.getValue() - V_PGK.getValue() - V_PK.getValue() + 2 * V_ADK.getValue() + V_CK.getValue() + V_ATPase.getValue());
#		ATP.addDydt(-V_PFK.getValue() + V_PGK.getValue() + V_PK.getValue() - V_ADK.getValue() - V_CK.getValue() - V_ATPase.getValue());
#		PCr.addDydt(V_CK.getValue());
# 		Cr??
	
	}
