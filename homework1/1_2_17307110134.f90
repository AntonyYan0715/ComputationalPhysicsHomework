PROGRAM solve_24
  use tools
  implicit none
  REAL                 :: reals(4), p, q, r, s
  INTEGER              :: numbers(4), num1, num2, num3, num4, i, j, k, a, b, c, d
  CHARACTER, parameter :: ops(4) = (/ '+', '-', '*', '/' /)
  LOGICAL              :: last
  ! numbers(4) contains 4 numbers that we input.
  ! ops(4) contains 4 operators that we have.

  PRINT *, 'Please input 4 numbers:'
  READ *, num1, num2, num3, num4
  numbers(1) = num1; numbers(2) = num2; numbers(3) = num3; numbers(4) = num4
  call Sort(numbers)
  ! Sort() is a function which can order the numbers from smallest to largest.
  ! This function can make sure that we go through all possible permutations.

    permutations: DO
      a = numbers(1); b = numbers(2); c = numbers(3); d = numbers(4)
      reals = REAL(numbers)
      p = reals(1);   q = reals(2);   r = reals(3);   s = reals(4)
      ! Combine numbers with operators to generate a result.
      DO i=1,4
        DO j=1,4
          DO k=1,4
            ! We have 5 ways to arrange the brackets.
            ! We use IF-ELSE to go through all possiblities.
            IF      ( op(op(op(p,i,q),j,r),k,s)-24.0 == 0 ) THEN
              WRITE (*,*) numbers, ' : ', '((',a,ops(i),b,')',ops(j),c,')',ops(k),d
              exit permutations
            ELSE IF ( op(op(p,i,op(q,j,r)),k,s)-24.0 == 0 ) THEN
              WRITE (*,*) numbers, ' : ', '(',a,ops(i),'(',b,ops(j),c,'))',ops(k),d
              exit permutations
            ELSE IF ( op(p,i,op(op(q,j,r),k,s))-24.0 == 0 ) THEN
              WRITE (*,*) numbers, ' : ', a,ops(i),'((',b,ops(j),c,')',ops(k),d,')'
              exit permutations
            ELSE IF ( op(p,i,op(q,j,op(r,k,s)))-24.0 == 0 ) THEN
              WRITE (*,*) numbers, ' : ', a,ops(i),'(',b,ops(j),'(',c,ops(k),d,'))'
              exit permutations
            ELSE IF ( op(op(p,i,q),j,op(r,k,s))-24.0 == 0 ) THEN
              WRITE (*,*) numbers, ' : ', '(',a,ops(i),b,')',ops(j),'(',c,ops(k),d,')'
              exit permutations
            END IF
          END DO
        END DO
      END DO
      CALL next_permutation(numbers,last)
      ! next_permutation() is a function to generate the next permutation of 4 numbers.
      IF (last) THEN
        WRITE (*,*) numbers, ' : No solution.'
        exit permutations
      END IF
    END DO permutations

contains
  pure REAL function op(x,c,y)
    INTEGER, intent(in) :: c
    REAL, intent(in)    :: x,y
    ! op() is a function to combine numbers with operators.

    SELECT CASE ( ops(c) )
      CASE ('+')
        op = x+y
      CASE ('-')
        op = x-y
      CASE ('*')
        op = x*y
      CASE ('/')
        op = x/y
    END SELECT
  END function op

END PROGRAM solve_24

MODULE tools

contains

  PURE SUBROUTINE Sort(a)
    INTEGER, intent(inout) :: a(:)
    INTEGER                :: temp, i, j
    DO i=2,SIZE(a)
      j = i-1
      temp = a(i)
      DO WHILE ( j>=1 .and. a(j)>temp )
        a(j+1) = a(j)
        j = j - 1
      END DO
      a(j+1) = temp
    END DO
  END SUBROUTINE Sort
  ! We use insertion sort to order the numbers from small to large.

  SUBROUTINE next_permutation(perm,last)
    INTEGER, intent(inout) :: perm(:)
    LOGICAL, intent(out)   :: last
    INTEGER                :: k,l
    k = arrange1()
    last = (k == 0)
    IF ( .not. last ) THEN    
      l = arrange2(k)
      CALL swap(l,k)
      CALL reverse(k)
    END IF
    ! We generate a function next_permutation() to rearrange the position of 4 numbers.
    ! This function rearranges numbers into the lexicographically next greater permutation.

  contains
    pure INTEGER function arrange1()
      INTEGER :: k, max
      max = 0
      DO k=1, (SIZE(perm)-1)
        IF ( perm(k) < perm(k+1) ) THEN
          max = k
        END IF
      END DO
      largest1 = max
    END function arrange1

    pure INTEGER function arrange2(k)
      INTEGER, intent(in) :: k
      INTEGER             :: l, max
      max = k+1
      DO l=(k+2), SIZE(perm)
        IF ( perm(k) < perm(l) ) THEN
          max = l
        END IF
      END DO
      arrange2 = max
    END function arrange2

    SUBROUTINE swap(l,k)
      INTEGER, intent(in) :: k,l
      INTEGER             :: temp
      temp    = perm(k)
      perm(k) = perm(l)
      perm(l) = temp
    END SUBROUTINE swap
    ! swap() is a function which can swap the position of 2 numbers.
 
    SUBROUTINE reverse(k)
      INTEGER, intent(in) :: k
      INTEGER             :: i
      DO i=1, (SIZE(perm)-k)/2
        CALL swap(k+i, SIZE(perm)+1-i)
      END DO
    END SUBROUTINE reverse
    ! reverse() is a function which can reverse the order of numbers after perm(k).

  END SUBROUTINE next_permutation

END MODULE tools