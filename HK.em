

	Variable Variable( Vf )
	{
		Value 16.6;
	}

       Variable Variable( VHK_GX )
        {
		Value @( Lambeth[Glycolysis]);
#                Value 1.0;
        }

        Process HK_Process( V_HK )
        {
                StepperID  ODE;
                Priority   0;

                VariableReferenceList
                        [ Vf           :.:Vf           0 ]
                        [ ATP          :.:ATPtotal    -1 ]
                        [ Glc          :.:Glc          0 ]
#                       [ Glc          :.:Glc         -1 ]
                        [ ADP          :.:ADPtotal     1 ]
                        [ G6P          :.:G6P          1 ]
                        [ GX           :.:VHK_GX       0 ];

#                       Kapp 1700.0;
                        Kapp 7800.0;#130227
                        KATP 0.17;
                        KGlc 0.11;
#                       KADP 1.2;#Lueck_1974
                        KADP 0.57;#Ganson_1985
#                       KG6P 0.0014;#Lueck_1974
                        KG6P 0.064;#Ganson_1985
#                       KiATP 0.17;
#                       KiGlc 0.11;
#                       KiADP 1.2;
#                       KiG6P 0.0014;

	}

