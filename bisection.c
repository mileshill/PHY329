#include <stdio.h>
#include <math.h>

// Fuction:  f(x) = x**3 - 4 * x - 9
float fun( float x ){

	return (  log(x*x) - 0.7	);

}

void bisection( float *x, float a, float b, int *itr){
	// performs and prints result of single iteration
	*x = ( a+b )/2;
	++( *itr );
	//printf( "Iteration no. %3d X = %20.18f\n", *itr, *x );
}

int main(){

	int itr = 0, maxmitr;
	float x, a, b, allerr, x1;
	//printf("\nEnter the values of a,b, allowed error and max iterations.");
	//scanf("%f %f %f %d", &a, &b, &allerr, &maxmitr);
	a = 0.5;
	b = 2.0;
	allerr = 0.000001;
	maxmitr = 100;

	// invoke bisection
	bisection( &x, a, b, &itr );
	// logic
	do{
		// bisection condition
		if( fun(a)*fun(x) < 0)
			b = x;
		else
			a = x;

		bisection( &x1, a, b, &itr );

		// exit on error conditions
		if( fabs(x1 - x) < allerr ){
			printf("After %d iterations, root = %20.18f\n", itr, x1);
			return 0;
		}
		x = x1;

	}// end do

	while ( itr < maxmitr );
	printf("The solution does not converge or iterations are not sufficient");
	return 1;
}


