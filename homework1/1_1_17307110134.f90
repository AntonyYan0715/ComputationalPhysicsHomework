PROGRAM solve_equation
implicit none
REAL a, b, c, delta, solu1, solu2, real_part, imaginary_part
COMPLEX solu3, solu4
! Consider both real solutions and complex solutions.
! For complex solutions, we need to calculate both real part and imaginary part.
PRINT *, 'Input a, b and c:'
READ *, a, b, c
    delta = b**2 - 4*a*c
    ! Calculate the delta to determine whether the solutions are real or complex.
    IF (delta > 0) THEN
    ! The solutions are real. 
        solu1 = (-b + sqrt(delta)) / (2*a)
        solu2 = (-b - sqrt(delta)) / (2*a)
        PRINT *, 'There are two real solutions:', solu1, solu2
    ELSE IF (delta < 0) THEN
    ! The solutions are complex.
        real_part = (-b)/(2*a)
        imaginary_part = sqrt(-delta)
        solu3 = cmplx(real_part,imaginary_part)
        solu4 = cmplx(real_part,-imaginary_part)
        PRINT *, 'There are two complex solutions:', solu3, solu4
    ELSE
    ! The solution is a double root, so there is only one solution.
        solu1 = -b / (2*a)
        PRINT *, 'There is only one solution:', solu1
    END IF
END