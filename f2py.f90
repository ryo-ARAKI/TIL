!#######################################################################
!
! F2PYのサンプルプログラム
! f2py3.8 -c --fcompiler=gfortran -m test f2py.f90
!
!#######################################################################

subroutine cal_test(xdim, ydim, x, y)
  integer xdim, ydim
  double precision x(xdim,ydim)
  double precision y(xdim,ydim)
  intent(in) xdim, ydim, x
  intent(out) y
  integer i, j

  do j = 1, ydim
  do i = 1, xdim
    y(i,j) = 2.0d0 * x(i,j)
  end do
  end do

end subroutine cal_test
