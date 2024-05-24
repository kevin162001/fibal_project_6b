import streamlit as st
def app():
    # Judul dan Informasi mengenai Dasboard
    st.markdown("""
    <h1 style='text-align: center; color: black;'>tentang kami(synergisma) </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
          synergisma adalah sebuah tim yang dibentuk untuk menyelasaikan sebuah project untuk menganalisis dan 
          memprediksi variabel-variabel dari data-data metereologi. Pembuatan dashboard ini merupakan projek akhir 
          dari Program Data Sience dan Artifitial Intelegence dari Sturtup Campus. Projek ini disusun semata-mata untuk
          tujuan pendidikan dan pembelajaran.
    """)
    col1, col2 = st.columns([2, 1])
    with col_1:
        st.header("Problem statement")
        st.markdown("""
          Dalam beberapa tahun terakhir, perubahan suhu udara yang tidak terduga telah menjadi sebuah tantangan signifikan 
          yang mempengaruhi pola cuaca regional di wilayah tertentu. Rata-rata, suhu udara telah menunjukkan tren penurunan 
          sebesar 8.03 derajat Celcius setiap tahunnya. Penurunan suhu udara ini kemungkinan dipengaruhi oleh ketidakstabilan 
          beberapa faktor seperti kecepatan angin, curah hujan, dan tekanan atmosfer, yang pada gilirannya mempengaruhi suhu 
          udara di wilayah tertentu secara kompleks. Namun, diperlukan analisis lebih mendalam mengenai hubungan antara 
          variabel meteorologi ini dengan suhu udara. Sebagai langkah selanjutnya, perlu dilakukan pengembangan model prediksi 
          yang lebih canggih untuk memperkirakan perubahan nilai seluruh variabel meteorologi di masa mendatang dengan akurasi 
          yang lebih tinggi.
          """)
    with col1:
        st.header("Business solution")
        st.markdown("""
          Dengan memahami hubungan antara variabel meteorologi tertentu serta pengembangan model prediksi suhu udara berbasis 
          data ini dapat membantu lembaga meteorologi, peneliti iklim, atau bahkan bisnis yang terkait dengan cuaca misalnya, 
          perusahaan energi, pertanian dalam membuat keputusan yang lebih baik. Prakiraan cuaca yang lebih akurat dapat meni-
          ngkatkan keselamatan publik, mengurangi risiko kerugian bisnis, dan meningkatkan efisiensi operasional.
          """)
        
        
        
