import streamlit as st
import pandas as pd
from web_function import load_data
import plotly.express as px
def app():
    # Judul dan Informasi mengenai Dasboard
    st.markdown("""
    <h1 style='text-align: center; color: black;'>eksploratory data analysis </h1>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <h2 style='text-align: center; color: black;'>Problem Statement</h2>
        """, unsafe_allow_html=True)
        st.markdown("""
           <div style='text-align: justify;'>
              Dalam beberapa tahun terakhir, perubahan suhu udara yang tidak terduga telah menjadi sebuah tantangan signifikan 
              yang mempengaruhi pola cuaca regional di wilayah tertentu. Rata-rata, suhu udara telah menunjukkan tren penurunan 
              sebesar 8.03 derajat Celcius setiap tahunnya. Penurunan suhu udara ini kemungkinan dipengaruhi oleh ketidakstabilan 
              beberapa faktor seperti kecepatan angin, curah hujan, dan tekanan atmosfer, yang pada gilirannya mempengaruhi suhu 
              udara di wilayah tertentu secara kompleks. Namun, diperlukan analisis lebih mendalam mengenai hubungan antara 
              variabel meteorologi ini dengan suhu udara. Sebagai langkah selanjutnya, perlu dilakukan pengembangan model prediksi 
              yang lebih canggih untuk memperkirakan perubahan nilai seluruh variabel meteorologi di masa mendatang dengan akurasi 
              yang lebih tinggi.
          </div>
          """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <h2 style='text-align: center; color: black;'>Business Solution</h2>
        """, unsafe_allow_html=True)
        st.markdown("""
          <div style='text-align: justify;'>
              Dengan memahami hubungan antara variabel meteorologi tertentu serta pengembangan model prediksi suhu udara berbasis 
              data ini dapat membantu lembaga meteorologi, peneliti iklim, atau bahkan bisnis yang terkait dengan cuaca misalnya, 
              perusahaan energi, pertanian dalam membuat keputusan yang lebih baik. Prakiraan cuaca yang lebih akurat dapat meni-
              ngkatkan keselamatan publik, mengurangi risiko kerugian bisnis, dan meningkatkan efisiensi operasional.
          </div>
          """, unsafe_allow_html=True)

     # Load data
    df = load_data("Data/train.csv")
    df_class = df.copy()
    df_class['date'] = pd.to_datetime(df_class['date'])
    df_class.set_index('date', inplace=True)

    # Pilih kolom numerik
    numeric_columns = df_class.select_dtypes(include=['number']).columns.tolist()

    # Dictionary untuk menyimpan narasi untuk setiap variabel
    variable_narratives = {
        "Iws": "Ini adalah narasi untuk variabel Iws.",
        "Ir": "Ini adalah narasi untuk variabel Ir.",
        "pm2.5": "Ini adalah narasi untuk variabel pm2.5.",
        "PRES": "Ini adalah narasi untuk variabel Iws.",
        "cbwd": "Ini adalah narasi untuk variabel Iws.",
        "DEWP": "Ini adalah narasi untuk variabel Iws.",
        "Temperature": "Ini adalah narasi untuk variabel Iws.",
        # Tambahkan narasi untuk variabel lain di sini
    }

    st.subheader("Exploratory Data Analysis")

    # Loop through numeric columns
    for column in numeric_columns:
        # Tampilkan narasi di samping box plot
        st.write(f"## {column}")
        st.write(variable_narratives.get(column, "Narasi untuk variabel ini belum ditambahkan"))

        # Tampilkan box plot dan narasi dalam satu baris
        col1, col2 = st.columns([2, 3])
        with col1:
            st.write(f"### Box Plot for {column}")
            fig = px.box(df_class, x=column, orientation='h', title=f"Horizontal Box Plot for {column}")
            st.plotly_chart(fig)
  
