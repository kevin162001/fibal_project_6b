import streamlit as st
import pandas as pd
from web_function import load_data
import plotly.express as px
import plotly.graph_objects as go

def app():
    # Judul dan Informasi mengenai Dasboard
    st.markdown("""
    <h1 style='text-align: center; color: black;'>Dashboard Pemantauan dan Prediksi Variabel-Variabel Metereologi 🌦️</h1>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col2:
       st.image("Picture/img-20230327-wa0013.jpg", caption="cuaca ekstrem", use_column_width=True)
    with col1:
       st.write("Dibuka pintu ke Dashboard prediksi Variabel-Variabel Metereologi yang memukau! "
            "Di sini, data bertemu dengan kreativitas, mengungkap rahasia langit dan atmosfer dalam segala warna. " 
            "Dari riak kecepatan angin hingga percikan curah hujan, melalui lautan konsentrasi PM2.5, hingga cakrawala suhu yang menggoda, " 
            "mari kita menjelajahi kisah-kisah cuaca yang menarik dengan prediksi yang memukau dan pemantauan yang real-time. "
            "Siap untuk mengikuti petualangan melintasi atmosfer?" 
            )

    # Load Dataset
    df = load_data("Data/train.csv")

    # Data Historis metereologi
    df_class = df.copy()
    df_class['date'] = pd.to_datetime(df_class['date'])
    df_class.set_index('date', inplace=True)

    # Pemfilteran Data Berdasarkan Range Waktu
    date_range = st.date_input("Pilih Rentang Waktu :", [df_class.index.min(), df_class.index.max()], key="date_range")
    start_date, end_date = date_range
    filtered_df_class = df_class.loc[start_date:end_date]

    # Menampilkan Data Historis Banjir
    st.header("Data Historis dari Variabel-Variabel Metereologi")
    st.write(filtered_df_class)

    # Menampilkan penjelasan dari struktur data
    st.write("Deskripsi kolom dari tabel tersebut adalah:")   
    kolomdesc = '\n1.  date\t: Setiap titik data memiliki timestamp yang menunjukkan tanggal dan waktu observasi\
                 \n2.  Iws\t        : Kecepatan angin kumulatif selama periode menjelang setiap pengamatan\
                 \n3.  Ir\t        : Intensitas curah hujan yang diukur pada setiap waktu pengamatan\
                 \n4.  Pm2.5\t: Konsentrasi materi partikulat halus (PM2.5) di udara\
                 \n5.  PRES\t: Tekanan atmosfer dicatat pada setiap titik waktu\
                 \n6.  Cbwd\t: Gabungan arah angin yang diukur di lokasi pengamatan\
                 \n7.  DEWP\t: Suhu titik embun, mewakili suhu saat udara menjadi jenuh dengan uap air\
                 \n8.  Temperature\t: Suhu udara (dalam derajat Celcius) sekitar yang dicatat pada setiap waktu,berfungsi sebagai fokus utama analisis dan prediksi'
    st.write(kolomdesc) 

    st.header("Visualisasi Tren untuk Masing-masing Variabel")
    st.subheader("Tren Kecepatan Angin Kumulatif")
    col1, col2 = st.columns([2, 1])
    with col1:
       fig_iws = px.line(filtered_df_class, x=filtered_df_class.index, y="Iws", title="Tren Kecepatan Angin Kumulatif", line_shape='linear')
       fig_iws.update_traces(line=dict(color='#ADD8E6'))
       fig_iws.update_layout(xaxis_title=None, autosize=True, height=500, yaxis=dict(showgrid=False))
       st.plotly_chart(fig_iws, use_container_width=True, responsive=True)
       
    with col2:
        st.text("Dengan menghitung rata-rata dari frekuensi data yang diresample, kita dapat mendapatkan  \
            \nnilai rata-rata curah hujan untuk setiap interval waktu yang dipilih (misalnya, harian, \
            \nmingguan, atau bulanan). Perhitungan ini memberikan gambaran umum tentang kecenderungan  \
            \ncurah hujan selama interval waktu tersebut. Misalnya, rata-rata harian dapat memberikan \
            \ninformasi tentang curah hujan rata-rata setiap hari dalam satu bulan. Proses ini tidak  \
            \nhanya membantu dalam menyederhanakan data, tetapi juga memungkinkan penggunaan metrik \
            \nyang lebih mudah diinterpretasi dalam analisis. \
            \n\nDengan menggunakan nilai rata-rata ini, pengguna dapat mengidentifikasi pola, tren,  \
            \natau fluktuasi dalam curah hujan dengan lebih baik. Informasi ini kemudian dapat \
            \ndigunakan sebagai dasar untuk proses forecasting lebih lanjut atau untuk  \
            \nmengembangkan model prediksi terkait potensi banjir. Rata-rata frekuensi data \
            \nyang diresample memberikan ringkasan yang lebih mudah dipahami, yang dapat  \
            \ndigunakan sebagai dasar untuk pengambilan keputusan terkait manajemen risiko banjir."
    )    

    st.subheader("Tren Intensitas Curah Hujan")
    col1, col2 = st.columns([2, 1])
    with col1:
      fig_ir = px.line(filtered_df_class, x=filtered_df_class.index, y="Ir", title="Tren Intensitas Curah Hujan", line_shape='linear')
      fig_ir.update_traces(line=dict(color='#4682B4'))
      fig_ir.update_layout(xaxis_title=None, autosize=True, height=500, yaxis=dict(showgrid=False))
      st.plotly_chart(fig_ir, use_container_width=True, responsive=True)
    with col2:
        st.text("Dengan menghitung rata-rata dari frekuensi data yang diresample, kita dapat mendapatkan  \
            \nnilai rata-rata curah hujan untuk setiap interval waktu yang dipilih (misalnya, harian, \
            \nmingguan, atau bulanan). Perhitungan ini memberikan gambaran umum tentang kecenderungan  \
            \ncurah hujan selama interval waktu tersebut. Misalnya, rata-rata harian dapat memberikan \
            \ninformasi tentang curah hujan rata-rata setiap hari dalam satu bulan. Proses ini tidak  \
            \nhanya membantu dalam menyederhanakan data, tetapi juga memungkinkan penggunaan metrik \
            \nyang lebih mudah diinterpretasi dalam analisis. \
            \n\nDengan menggunakan nilai rata-rata ini, pengguna dapat mengidentifikasi pola, tren,  \
            \natau fluktuasi dalam curah hujan dengan lebih baik. Informasi ini kemudian dapat \
            \ndigunakan sebagai dasar untuk proses forecasting lebih lanjut atau untuk  \
            \nmengembangkan model prediksi terkait potensi banjir. Rata-rata frekuensi data \
            \nyang diresample memberikan ringkasan yang lebih mudah dipahami, yang dapat  \
            \ndigunakan sebagai dasar untuk pengambilan keputusan terkait manajemen risiko banjir."
    )  

    st.subheader("Tren pm2.5")
    fig_pm25 = px.line(filtered_df_class, x=filtered_df_class.index, y="pm2.5", title="Tren Konsentrasi PM2.5", line_shape='linear')
    fig_pm25.update_traces(line=dict(color='gray'))
    fig_pm25.update_layout(xaxis_title=None, autosize=True, height=500, yaxis=dict(showgrid=False))
    st.plotly_chart(fig_pm25, use_container_width=True, responsive=True)

    st.subheader("Tren Tekanan Atmosfer")
    fig_pres = px.line(filtered_df_class, x=filtered_df_class.index, y="PRES", title="Tren Tekanan Atmosfer", line_shape='linear')
    fig_pres.update_traces(line=dict(color='#008080'))
    fig_pres.update_layout(xaxis_title=None, autosize=True, height=500, yaxis=dict(showgrid=False))
    st.plotly_chart(fig_pres, use_container_width=True, responsive=True)

    st.subheader("Tren Suhu Titik Embun")
    fig_dewp = px.line(filtered_df_class, x=filtered_df_class.index, y="DEWP", title="Tren Suhu Titik Embun", line_shape='linear')
    fig_dewp.update_traces(line=dict(color='blue'))
    fig_dewp.update_layout(xaxis_title=None, autosize=True, height=500, yaxis=dict(showgrid=False))
    st.plotly_chart(fig_dewp, use_container_width=True, responsive=True)

    st.subheader("Tren Gabungan arah angin")
    fig_Cbdw = px.line(filtered_df_class, x=filtered_df_class.index, y="cbwd", title="Gabungan arah angin")
    fig_Cbdw.update_layout(xaxis_title=None, autosize=True, height=500, yaxis=dict(showgrid=False))
    st.plotly_chart(fig_Cbdw)

    st.subheader("Tren Suhu Udara")
    fig_temp = px.line(filtered_df_class, x=filtered_df_class.index, y="Temperature", title="Tren Suhu Udara", line_shape='linear')
    fig_temp.update_traces(line=dict(color='orange'))
    fig_temp.update_layout(xaxis_title=None, autosize=True, height=500, yaxis=dict(showgrid=False))
    st.plotly_chart(fig_temp, use_container_width=True, responsive=True)

     # Visualisasi Korelasi antar variabel (kecuali id)
    st.header("Visualisasi Korelasi antar Variabel")
    corr_matrix = filtered_df_class.drop(columns=["id"]).corr()
    fig_corr = go.Figure(data=go.Heatmap(
                   z=corr_matrix.values,
                   x=corr_matrix.columns,
                   y=corr_matrix.index,
                   colorscale='Greens'))
    fig_corr.update_layout(title='Korelasi antar Variabel')

    # Menambahkan teks nilai korelasi di setiap sel heatmap
    for i in range(len(corr_matrix.index)):
        for j in range(len(corr_matrix.columns)):
            fig_corr.add_annotation(x=corr_matrix.columns[j], y=corr_matrix.index[i],
                                    text=str(round(corr_matrix.values[i, j], 2)),
                                    showarrow=False, font=dict(size=10), xshift=-5)

    st.plotly_chart(fig_corr)

    

   











  
