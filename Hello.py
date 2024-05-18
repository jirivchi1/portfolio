# create basic streamlit app

import streamlit as st
import pandas as pd
import numpy as np

from streamlit_timeline import timeline

from graph_builder_en import *
from graph_builder_es import *
from graph_vision_en import *
from graph_vision_es import *



def main():

    language = st.sidebar.radio('Choose your language', ['Español', 'English'])
    st.sidebar.image('imgs/Ismael-Rivera-OGA-2024.jpg')



    english_content = {
    "title": "Ismael Rivera",
    "description": "Ismael Rivera, an AI and data analysis expert, holds master's degrees from Loyola University (2022-2023) and the Sorbonne University Paris (2021-2022), excelling in business automation projects, LLM models, and artificial vision. His technical prowess covers Python and time series analysis, with experience in entrepreneurship leadership. He is proficient in Spanish, English (Cambridge First), and has an intermediate level of Italian."}

    spanish_content = {
    "title": "Ismael Rivera",
    "description": "Ismael Rivera, experto en IA y análisis de datos, tiene másteres de la Universidad Loyola (2022-2023) y la Sorbona de París (2021-2022), destacándose en proyectos de automatización  para negocios, modelos LLM y visión artificial. Su destreza técnica abarca Python y análisis de series temporales, con experiencia en liderazgo en emprendimiento. Maneja el castellano, inglés (Cambridge First) e italiano a nivel intermedio."}   

    st.title(english_content["title"])

    if language == 'English':
        st.subheader('"Faciliting the adoption of ai techonology into the world, into businesses, etc."')

    if language == 'Español':
        st.subheader('"Facilitando la adopción de la tecnología de inteligencia artificial en el mundo, en los negocios, etc."')

    col1, col2, col3 = st.columns([1,2,1])





    if language == 'English':

        tab1,tab2,tab3,tab4 = st.tabs(["summary","Career snapshot", "Daily workflow","Projects"])

        with tab1:

            st.write(english_content["description"])


        with tab2:
            with st.spinner(text="Building line"):
                with open('timeline_en.json', "r", encoding='utf-8') as f:
                    data = f.read()
                    timeline(data, height=400)


        with tab3:
            st.graphviz_chart(graph)

        st.sidebar.caption('Wish to connect?')
        st.sidebar.write('📧: jirivchi@gmail.com')
        st.sidebar.write('📧 : ismael.rivera@oga.ai')
        pdfFileObj = open('pdfs/CV_ISMAEL_RIVERA_090424.pdf', 'rb')
        st.sidebar.download_button('download resume',pdfFileObj,file_name='CV_Ismael_280923.pdf',mime='pdf')

        with tab4:
            st.header('VISION')
            st.subheader('EPIs-YOLO')
            st.graphviz_chart(graph_en)

        
    if language == 'Español':

        tab1,tab2,tab3,tab4 = st.tabs(["Resumen","Vision General", "Flujo de trabajo diario","Trabajos"])

        with tab1:
            st.write(spanish_content["description"])

        with tab2:

            with st.spinner(text="Building line"):
                with open('timeline.json', "r", encoding='utf-8') as f:
                    data = f.read()
                    timeline(data, height=500)
        
        with tab3:
            st.graphviz_chart(graph_es)

        with tab4:
            st.header('VISION')
            st.subheader('EPIs-YOLO')
            st.graphviz_chart(graph_vision_es)

        # sidebar
        st.sidebar.caption('¿Deseas Contactar?')
        st.sidebar.write('📧: jirivchi@gmail.com')
        st.sidebar.write('📧 : ismael.rivera@oga.ai')
        pdfFileObj = open('pdfs/CV_Ismael_280923.pdf', 'rb')
        st.sidebar.download_button('Descargar CV',pdfFileObj,file_name='CV_Ismael_280923.pdf',mime='pdf')



if __name__ == "__main__":
    main()