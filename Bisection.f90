! RUNNING THIS CODE
! You must call the function, in a separate file, to be compiled:
! eg: function is in c5p7  "Chp 5 Prob 7"
! 
! >>> gfortran Bisection.f90 c5p7.f90 -o c5p7
! >>> ./c5p7

!==================================================================
! MAIN
! Determine a single root of an equation f(x) == 0 in [x1, x2] 
! Method: Bisection
!==================================================================

PROGRAM main
	
	IMPLICIT NONE

	REAL*8, EXTERNAL :: f
	REAL*8 ::  x1, x2, eps, root
	INTEGER :: flag
	

	! Set interval bounds and error tolerance
	x1 = 0.5
	x2 = 2.0
	eps = 1.0e-6

	call Bisection( f, x1, x2, eps, root, flag )

	write(*,*) root
END PROGRAM main
	




! Bisection( f, x1, x2, eps, root, flag )
! ==================================================================
! Solutions of equation f(x)==0 on [ x1,x2 ]
! Method: Bisection ( closed domain )
! ------------------------------------------------------------------
! input ...
! f	- function - evaluates f(x) for any x in the interval
! x1	- left endpoint of interval
! x2	- right endpoint of interval
! eps 	- desired uncertaintainty of the root as  |b-a|< eps
!
! output ...
! root	- root of the equation f(x) == 0
! flag	- indicator of success
!	> 0	- a single root found; flag = number of iterations
!	  0	- no solutions for bisection method
!	< 0	- not a root but singularity; flag = number of iterations
!
! Comments: 	Function f(x) must change sign between x1 and x2
!		Max number of iterations - 200 ( accuracy (b-a)/2**200 )
! ===================================================================
SUBROUTINE Bisection(f, x1, x2, eps, root, flag)

	IMPLICIT NONE 
	REAL*8	:: f, x1, x2, eps, root
	REAL*8  :: a, b, c
	
	INTEGER :: i, flag
	INTEGER :: iter = 200

	! Check the bisection condition f(x1)*f(x2) < 0
	if ( f(x1) * f(x2) .gt. 0.0 ) then
		flag = 0 
		return
	end if

	! Initialize calculations
	a = x1
	b = x2

	! Begin iteration: shifts (a,b) to solve for root
	do i = 1, iter
		c = (b+a)/2.0	! interval midpoint
		
		! Shift interval 		
		if ( f(a) * f(c) .le. 0.0 ) then
			b = c
		else
			a = c
		end if
		
		! Stop condition
		if ( abs( b - a ) < eps ) then
			exit
		end if
		
	end do

	root = ( b + a )/2.0

	! Check if it is a root or singularity
	if ( abs( root ) .lt. 1.0 ) then
		flag = i
	else
		flag = -i
	end if
END SUBROUTINE Bisection


























	
