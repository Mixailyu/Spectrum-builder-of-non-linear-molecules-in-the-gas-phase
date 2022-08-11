import sympy as sy

number_of_vibrational_degrees=3
max_indignation_step=4
TYPE_ANGARMONIC_CONST='k'
title=''
n_i=sy.symbols("n_i")
omega_i=sy.symbols("omega_i")

n_j=sy.symbols("n_j")
omega_j=sy.symbols("omega_j")

n_k=sy.symbols("n_k")
omega_k=sy.symbols("omega_k")


###########################################

A_iii=sy.symbols("A_iii")
A_iij=sy.symbols("A_iij")
A_iik=sy.symbols("A_iik")
A_ijj=sy.symbols("A_ijj")
A_ijk=sy.symbols("A_ijk")
A_ikk=sy.symbols("A_ikk")
A_jjj=sy.symbols("A_jjj")
A_jjk=sy.symbols("A_jjk")
A_jkk=sy.symbols("A_jkk")
A_kkk=sy.symbols("A_kkk")

###########################################

A_iiii=sy.symbols("A_iiii")
A_iiij=sy.symbols("A_iiij")
A_iiik=sy.symbols("A_iiik")
A_iijj=sy.symbols("A_iijj")
A_iijk=sy.symbols("A_iijk")
A_iikk=sy.symbols("A_iikk")
A_ijjj=sy.symbols("A_ijjj")
A_ijjk=sy.symbols("A_ijjk")
A_ijkk=sy.symbols("A_ijkk")
A_ikkk=sy.symbols("A_ikkk")
A_jjjj=sy.symbols("A_jjjj")
A_jjjk=sy.symbols("A_jjjk")
A_jjkk=sy.symbols("A_jjkk")
A_jkkk=sy.symbols("A_jkkk")
A_kkkk=sy.symbols("A_kkkk")

###########################################

A_iiiii=sy.symbols("A_iiiii")
A_iiiij=sy.symbols("A_iiiij")
A_iiiik=sy.symbols("A_iiiik")
A_iiijj=sy.symbols("A_iiijj")
A_iiijk=sy.symbols("A_iiijk")
A_iiikk=sy.symbols("A_iiikk")
A_iijjj=sy.symbols("A_iijjj")
A_iijjk=sy.symbols("A_iijjk")
A_iijkk=sy.symbols("A_iijkk")
A_iikkk=sy.symbols("A_iikkk")
A_ijjjj=sy.symbols("A_ijjjj")
A_ijjjk=sy.symbols("A_ijjjk")
A_ijjkk=sy.symbols("A_ijjkk")
A_ijkkk=sy.symbols("A_ijkkk")
A_ikkkk=sy.symbols("A_ikkkk")
A_jjjjj=sy.symbols("A_jjjjj")
A_jjjjk=sy.symbols("A_jjjjk")
A_jjjkk=sy.symbols("A_jjjkk")
A_jjkkk=sy.symbols("A_jjkkk")
A_jkkkk=sy.symbols("A_jkkkk")
A_kkkkk=sy.symbols("A_kkkkk")

###########################################

A_iiiiii=sy.symbols("A_iiiiii")
A_iiiiij=sy.symbols("A_iiiiij")
A_iiiiik=sy.symbols("A_iiiiik")
A_iiiijj=sy.symbols("A_iiiijj")
A_iiiijk=sy.symbols("A_iiiijk")
A_iiiikk=sy.symbols("A_iiiikk")
A_iiijjj=sy.symbols("A_iiijjj")
A_iiijjk=sy.symbols("A_iiijjk")
A_iiijkk=sy.symbols("A_iiijkk")
A_iiikkk=sy.symbols("A_iiikkk")
A_iijjjj=sy.symbols("A_iijjjj")
A_iijjjk=sy.symbols("A_iijjjk")
A_iijjkk=sy.symbols("A_iijjkk")
A_iijkkk=sy.symbols("A_iijkkk")
A_iikkkk=sy.symbols("A_iikkkk")
A_ijjjjj=sy.symbols("A_ijjjjj")
A_ijjjjk=sy.symbols("A_ijjjjk")
A_ijjjkk=sy.symbols("A_ijjjkk")
A_ijjkkk=sy.symbols("A_ijjkkk")
A_ijkkkk=sy.symbols("A_ijkkkk")
A_ikkkkk=sy.symbols("A_ikkkkk")
A_jjjjjj=sy.symbols("A_jjjjjj")
A_jjjjjk=sy.symbols("A_jjjjjk")
A_jjjjkk=sy.symbols("A_jjjjkk")
A_jjjkkk=sy.symbols("A_jjjkkk")
A_jjkkkk=sy.symbols("A_jjkkkk")
A_jkkkkk=sy.symbols("A_jkkkkk")
A_kkkkkk=sy.symbols("A_kkkkkk")

###########################################

D_0=sy.symbols('D_0')
D_i=sy.symbols("D_i")
D_j=sy.symbols("D_j")
D_k=sy.symbols("D_k")

D_ii=sy.symbols("D_ii")
D_ij=sy.symbols("D_ij")
D_ik=sy.symbols("D_ik")
D_jj=sy.symbols("D_jj")
D_jk=sy.symbols("D_jk")
D_kk=sy.symbols("D_kk")

D_iii=sy.symbols("D_iii")
D_iij=sy.symbols("D_iij")
D_iik=sy.symbols("D_iik")
D_ijj=sy.symbols("D_ijj")
D_ijk=sy.symbols("D_ijk")
D_ikk=sy.symbols("D_ikk")
D_jjj=sy.symbols("D_jjj")
D_jjk=sy.symbols("D_jjk")
D_jkk=sy.symbols("D_jkk")
D_kkk=sy.symbols("D_kkk")

D_iiii=sy.symbols("D_iiii")
D_iiij=sy.symbols("D_iiij")
D_iiik=sy.symbols("D_iiik")
D_iijj=sy.symbols("D_iijj")
D_iijk=sy.symbols("D_iijk")
D_iikk=sy.symbols("D_iikk")
D_ijjj=sy.symbols("D_ijjj")
D_ijjk=sy.symbols("D_ijjk")
D_ijkk=sy.symbols("D_ijkk")
D_ikkk=sy.symbols("D_ikkk")
D_jjjj=sy.symbols("D_jjjj")
D_jjjk=sy.symbols("D_jjjk")
D_jjkk=sy.symbols("D_jjkk")
D_jkkk=sy.symbols("D_jkkk")
D_kkkk=sy.symbols("D_kkkk")

const_n_dikt={n_i:0,n_j:0,n_k:0}
const_omega_dikt={omega_i:0,omega_j:0,omega_k:0}
const_angarmonik_dikt={A_iii:0,A_iij:0,A_iik:0,A_ijj:0,A_ijk:0,A_ikk:0,A_jjj:0,A_jjk:0,A_jkk:0,A_kkk:0,A_iiii:0,A_iiij:0,A_iiik:0,A_iijj:0,A_iijk:0,A_iikk:0,A_ijjj:0,A_ijjk:0,A_ijkk:0,A_ikkk:0,A_jjjj:0,A_jjjk:0,A_jjkk:0,A_jkkk:0,A_kkkk:0,A_iiiii:0,A_iiiij:0,A_iiiik:0,A_iiijj:0,A_iiijk:0,A_iiikk:0,A_iijjj:0,A_iijjk:0,A_iijkk:0,A_iikkk:0,A_ijjjj:0,A_ijjjk:0,A_ijjkk:0,A_ijkkk:0,A_ikkkk:0,A_jjjjj:0,A_jjjjk:0,A_jjjkk:0,A_jjkkk:0,A_jkkkk:0,A_kkkkk:0,A_iiiiii:0,A_iiiiij:0,A_iiiiik:0,A_iiiijj:0,A_iiiijk:0,A_iiiikk:0,A_iiijjj:0,A_iiijjk:0,A_iiijkk:0,A_iiikkk:0,A_iijjjj:0,A_iijjjk:0,A_iijjkk:0,A_iijkkk:0,A_iikkkk:0,A_ijjjjj:0,A_ijjjjk:0,A_ijjjkk:0,A_ijjkkk:0,A_ijkkkk:0,A_ikkkkk:0,A_jjjjjj:0,A_jjjjjk:0,A_jjjjkk:0,A_jjjkkk:0,A_jjkkkk:0,A_jkkkkk:0,A_kkkkkk:0}
const_dipol_dikt={D_0:0,D_i:0,D_j:0,D_k:0,D_ii:0,D_ij:0,D_ik:0,D_jj:0,D_jk:0,D_kk:0,D_iii:0,D_iij:0,D_iik:0,D_ijj:0,D_ijk:0,D_ikk:0,D_jjj:0,D_jjk:0,D_jkk:0,D_kkk:0,D_iiii:0,D_iiij:0,D_iiik:0,D_iijj:0,D_iijk:0,D_iikk:0,D_ijjj:0,D_ijjk:0,D_ijkk:0,D_ikkk:0,D_jjjj:0,D_jjjk:0,D_jjkk:0,D_jkkk:0,D_kkkk:0}
ZAMENA={**const_n_dikt,**const_angarmonik_dikt,**const_dipol_dikt}
DATA_TABEL=[]
