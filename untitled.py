# library
import streamlit as st

# write
st.write('software perkalian')
st.subheader('ini adalah aplikasi untuk mengalikan bilangan bulat')

# input bilangan pertama
number1 = st.number_input('masukkan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

# bilangan kedua
number2 = st.number_input('masukkan bilangan kedua')
st.write(f'bilangan kedua adalah {number2}')

# hasil kali
hasil = number1*number2

if st.button('hitung'):
    st.write(f'hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('Silahkan pencet tombol hitung!')
    
import numpy as np
array1 = np.random.randint(10,40, size=(10,))
array2 = np.random.randint(10,40, size=(10,))

import pandas as pd
st.dataframe(pd.DataFrame({'kelas A' : array1, 
                           'kelas B' : array2
                          })
            )

