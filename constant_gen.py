

#Функция для генерации символов постоянных
from apendix import *
def constant_gen(number_of_vibrational_degrees=4,max_indignation_step=4,TYPE_ANGARMONIC_CONST='A',title=''):
  CONST_A_LIST=""
  CONST_n_LIST=""
  CONST_W_LIST=""
  CONST_D_LIST=""
  CONST_KEY_KEY=""
  f=open(f'const.py','w')
  f.write('import sympy as sy\n')
  f.write('\n')
  f.write(f'number_of_vibrational_degrees={number_of_vibrational_degrees}\n')
  f.write(f'max_indignation_step={max_indignation_step}\n')
  f.write(f"TYPE_ANGARMONIC_CONST='{TYPE_ANGARMONIC_CONST}'\n")
  f.write(f"title='{title}'\n")
  for i in range(1,number_of_vibrational_degrees+1):# Изменил (for i in VECTOR_INDEX[:number_of_vibrational_degrees]:) так как в VECTOR_INDEX в начале добавил 0
    i=VECTOR_INDEX[i]
    a='n_%s'%(i)
    A='%s=sy.symbols(''"%s"'')'%(a,a)
    CONST_n_LIST+="%s:0,"%(a)
    f.write(A+'\n')
    a='omega_%s'%(i)
    B='%s=sy.symbols(''"%s"'')'%(a,a)
    CONST_W_LIST+="%s:0,"%(a)
    f.write(B+'\n')
    f.write('\n')
  f.write('\n')
  f.write('###########################################\n')
  f.write('\n')
  C=1
  while C<=max_indignation_step:
    for i in INDEX(C,number_of_vibrational_degrees):
      a='A_%s'%(i)
      A='%s=sy.symbols(''"%s"'')'%(a,a)
      CONST_A_LIST+="%s:0,"%(a)
      f.write(A+'\n')
    f.write('\n')
    f.write('###########################################\n')
    f.write('\n')
    C+=1
  C=-1
  f.write("D_0=sy.symbols('D_0')\n")
  CONST_D_LIST+="D_0:0,"
  while C<max_indignation_step-1:
    for i in INDEX(C,number_of_vibrational_degrees):
      a='D_%s'%(i)
      A='%s=sy.symbols(''"%s"'')'%(a,a)
      CONST_D_LIST+="%s:0,"%(a)
      f.write(A+'\n')
    
    f.write('\n')
    C+=1
  CONST_n_LIST='const_n_dikt={%s}'%(CONST_n_LIST[:-1])
  CONST_W_LIST='const_omega_dikt={%s}'%(CONST_W_LIST[:-1])
  CONST_A_LIST='const_angarmonik_dikt={%s}'%(CONST_A_LIST[:-1])
  CONST_D_LIST='const_dipol_dikt={%s}'%(CONST_D_LIST[:-1])

  f.write(CONST_n_LIST+'\n')
  f.write(CONST_W_LIST+'\n')
  f.write(CONST_A_LIST+'\n')
  f.write(CONST_D_LIST+'\n')
  f.write("ZAMENA={**const_n_dikt,**const_angarmonik_dikt,**const_dipol_dikt}\n")
  f.write("DATA_TABEL=[]\n")
  
  f.close()
  return #from const import *
