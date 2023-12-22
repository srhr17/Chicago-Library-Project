import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium import Marker,Popup,Icon
from streamlit_folium import st_folium

st.set_page_config(page_title='Chicago Public Libraries : My Journey',page_icon='📚')

@st.cache_data
def load_data():
    df = pd.read_csv('Libraries&locations.csv')
    return df


df = load_data()

df['lat'] = df['LOCATION'].apply(lambda x : float(x.split(",")[0].strip("()")))
df['lon'] = df['LOCATION'].apply(lambda x : float(x.split(",")[1].strip("()")))

st.header(":blue[Chicago Public Libraries] : My Journey")
st.write("""
Welcome to :blue["Chicago Public Libraries: My Journey,"] an exploration of the vibrant tapestry that is Chicago, woven together by its :red[77 diverse neighborhoods]. In a city where every locality tells a :green[unique story], we embark on a journey to uncover the rich cultures, flavors, and communities surrounding each :blue[Chicago Public Library]. Chicago, renowned for its melting pot of cultures, is a city that thrives on its diversity. Each of the 77 neighborhoods encapsulates a microcosm of experiences, traditions, and histories. Remarkably, nestled within the heart of each community is a :blue[Chicago Public Library], serving as a hub for knowledge, connection, and local insights.

This journey is a celebration of the people, the neighborhoods, and the wealth of experiences waiting to be discovered. From the historic streets of Bronzeville to the artistic allure of Pilsen, we'll traverse the cityscape, immersing ourselves in the distinct character of each locale. My approach is simple yet profound – We start by stepping into the libraries. Librarians, the unsung keepers of local wisdom, are our guides. Armed with their knowledge, we'll uncover hidden gems, delve into neighborhood secrets, and embrace the authentic flavors that define each community.

Join me on this expedition through Chicago's :red[77 neighborhoods], as we navigate the pages of the city's libraries and explore the living stories etched in its streets, culture, and people. :blue["Chicago Public Libraries: My Journey"] is more than a documentation; it's an odyssey into the heart of a city that thrives on its diversity, waiting to share its tales with those who seek to listen.
""")

st.header("been there ?")

m = folium.Map(location=[df.loc[5,'lat'], df.loc[5,'lon']], zoom_start=10.5)

for i, row in df.iterrows():
    if row['visited']==True:
        Marker(
            location=[row['lat'],row['lon']],
            popup=Popup("<h1>" + row['NAME'] +"</h1><h6> Visited? Yes</h6> ("+ row['WEBSITE']  +")" , parse_html=False),
            tooltip=row['NAME'] + " (" +row['ADDRESS'] + ")",
            icon=Icon(icon="heart",icon_color='red')
        ).add_to(m)
    else:
        Marker(
            location=[row['lat'],row['lon']],
            popup=Popup("<h1>" + row['NAME'] +"</h1><h6> Visited? Nope</h6> ("+ row['WEBSITE']  +")" , parse_html=False),
            tooltip=row['NAME'] + " (" +row['ADDRESS'] + ")",
            icon=Icon(icon="heart",icon_color='gray')
        ).add_to(m)


out = st_folium(m,use_container_width=True,height=700)

if st.checkbox('View the entire list'):
    st.data_editor(df)


