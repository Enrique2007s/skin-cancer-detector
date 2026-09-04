import streamlit as st

# Class to make the streamlit pages
class MultiPage:
    def __init__(self, skin_cancer_detector) -> None:
        self.skin_cancer_detector = skin_cancer_detector
        self.pages = []

        st.set_page_config(page_title="Skin Cancer Detector", page_icon=":🥼")

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.title(self.skin_cancer_detector)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()