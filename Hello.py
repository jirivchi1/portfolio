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
    "title": "AI Ismael Rivera",
    "description": "Hello, I'm Ismael Rivera, an AI and data analysis expert, excelling in business automation projects, LLM models, and artificial vision."}

    spanish_content = {
    "title": "IA Ismael Rivera",
    "description": "Hola, soy Ismael Rivera, experto en IA y análisis de datos, proyectos de automatización  para negocios, modelos LLM y visión artificial."}   

    st.title(english_content["title"])

    if language == 'English':
        st.subheader('"Hello, I am Ismael Rivera, an AI and data analysis expert, excelling in business automation projects, LLM models, and artificial vision."')

    if language == 'Español':
        st.subheader('"Hola, soy Ismael Rivera, experto en IA y análisis de datos, proyectos de automatización  para negocios, modelos LLM y visión artificial."')

    col1, col2, col3 = st.columns([1,2,1])





    if language == 'English':

        tab1,tab2,tab3 = st.tabs(["summary","Career snapshot", "Daily workflow"])

        with tab1:

            st.header(':one: Explaratory data analysis and visualization')
            st.subheader('use cases')

            st.header(':two: VISION')
            st.subheader('Sports')

            st.header(':three: LLMs')
            st.subheader('Chatgpt4o')

            st.header(':four: Recommender Systems')
            st.subheader('Tripadvisor')
            


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

        
    if language == 'Español':

        tab1,tab2,tab3 = st.tabs(["Resumen","Vision General", "Flujo de trabajo diario"])

        with tab1:

            st.header(':one: Explaratory data analysis and visualization')
            st.subheader('use cases')

            st.header(':two: VISION')
            st.subheader('Sports')

            st.header(':three: LLMs')
            st.subheader('Chatgpt4o')

            st.header(':four: Recommender Systems')
            st.subheader('Tripadvisor')
            

        with tab2:

            with st.spinner(text="Building line"):
                with open('timeline.json', "r", encoding='utf-8') as f:
                    data = f.read()
                    timeline(data, height=500)
        
        with tab3:
            st.graphviz_chart(graph_es)
            

        # sidebar
        st.sidebar.caption('¿Deseas Contactar?')
        st.sidebar.write('📧: jirivchi@gmail.com')
        st.sidebar.write('📧 : ismael.rivera@oga.ai')
        pdfFileObj = open('pdfs/CV_ISMAEL_RIVERA_090424.pdf', 'rb')
        st.sidebar.download_button('Descargar CV',pdfFileObj,file_name='CV_ISMAEL_RIVERA_090424.pdf',mime='pdf')



if __name__ == "__main__":
    main()