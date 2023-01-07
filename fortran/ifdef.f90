!#######################################################################
!
! #ifdef フラグのサンプルプログラム
! $gfortran ifdef_flag.f90 -cpp -Dhello && ./a.out
! Hello
! How do you do?
!
! $gfortran ifdef_flag.f90 -cpp -Dgoodbye && ./a.out
! Goodbye
! How do you do?
!
! $gfortran ifdef_flag.f90 -cpp -Dhello -Dgoodbye && ./a.out
!  Hello
!  Goodbye
!  How do you do?
!  It's great to meet you!
!
!#######################################################################

program main
  implicit none

#ifdef hello
  write(*,*) "Hello"
#endif

#ifdef goodbye
  write(*,*) "Goodbye"
#endif

#if defined hello || defined goodbye
  write(*,*) "How do you do?"
#endif

#if defined hello && defined goodbye
  write(*,*) "It's great to meet you!"
#endif

end program main
