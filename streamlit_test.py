# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:47:44 2023

@author: AntoineBois
"""

import streamlit as st
import hmac
import streamlit as st


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False
    
if not check_password():
    st.stop()  # Do not continue if check_password is not True.

def runstreamlit () :
    
    st.markdown("Bienvenue sur Dimoclim &mdash;\
        :cyclone ::")

    option = st.selectbox('Localisation ? ',
    ('EU',
      'US'))

    option = st.selectbox('Type de batterie ?',
    ("JH4-4P",
      "JH4-3P",
       "JH4-2P",
        "JH4-1P",
         "JP3-2P",
          "JP3-3P"))

    option = st.selectbox('Type de container ?',
    ("20 pieds",
      "40 pieds",
       "45 pieds"))

    st.file_uploader('Choisissez un fichier de T°C extérieure')
    st.file_uploader('Choisissez un fichier de sollicitation')

    st.markdown('Construction du profil de puissance si pas de fichier de sollicitations')
    st.text_input('C-Rate')
    st.text_input('Temps inter cycle')


if __name__ == "__main__":
    runstreamlit()
        
 
 
