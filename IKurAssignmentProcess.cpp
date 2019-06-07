#include "libecs.hpp"
#include "Process.hpp"

USE_LIBECS;

LIBECS_DM_CLASS( IKurAssignmentProcess, Process )
{

 public:

	LIBECS_DM_OBJECT( IKurAssignmentProcess, Process )
	{
		INHERIT_PROPERTIES( Process );

		PROPERTYSLOT_SET_GET( Real, g );
	}

	IKurAssignmentProcess()
		:
		g( 0.0 )
	{
		// do nothing
	}

	SIMPLE_SET_GET_METHOD( Real, g );

	virtual void initialize()
	{
		Process::initialize();

		Vm    = getVariableReference( "Vm" ).getVariable();
		EK    = getVariableReference( "EK" ).getVariable();
		aur   = getVariableReference( "aur" ).getVariable();
		iur   = getVariableReference( "iur" ).getVariable();
    v_aur = getVariableReference( "v_aur" ).getVariable();
		v_iur = getVariableReference( "v_iur" ).getVariable();
		GX    = getVariableReference( "GX" ).getVariable();
    Cm    = getVariableReference( "Cm" ).getVariable();
	}

	virtual void fire()
	{
		_v       = Vm->getValue() - EK->getValue();

    I->setValue( ( GX->getValue() * g * aur->getValue() * iur->getValue() * _v * Cm->getValue() );

		_aur_inf = 1.0 / ( 1.0 + exp( -( Vm->getValue() + 6.0 )/ 8.6 ));
    _iur_inf = 1.0 / ( 1.0 + exp( ( Vm->getValue() + 7.5 )/ 10.0 ));

    _tau_aur = 0.009 / ( 1.0 + exp( ( Vm->getValue() + 5.0 )/ 12.0 )) + 0.0005;
    _tau_iur = 0.59 / ( 1.0 + exp( ( Vm->getValue() + 60.0 )/ 10.0 )) + 3.05;

		v_aur->setValue( (_aur_inf - aur->getValue() )/ _tau_aur );
    v_iur->setValue( (_iur_inf - iur->getValue() )/ _tau_iur );
	}

 protected:

	Variable* Vm;
	Variable* EK;
	Variable* aur;
	Variable* iur;
  Variable* v_aur;
	Variable* v_iur;
	Variable* GX;
  Variable* Cm;

	Real g;

 private:

	Real _v;
	Real _aur_inf;
	Real _iur_inf;
  Real _tau_aur;
	Real _tau_iur;

};

LIBECS_DM_INIT( IKurAssignmentProcess, Process );
