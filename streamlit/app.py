import streamlit as st
import pandas as pd
import numpy as np
import os
import streamlit.components.v1 as components  # Import Streamlit

# The minimal injection possibility
#components.html("<script type='text/javascript' src='https://js-cdn.dynatrace.com/jstag/<YOUR_APP_TAG_HERE>_complete.js' crossorigin='anonymous'></script>", height=0)

# The raw file injection possibility
def inject(tag):
  with open(os.path.dirname(st.__file__) + "/static/index.html", 'r') as file:
    str = file.read()
    if str.find(tag) == -1:
        idx = str.index('<head>')
        new_str = str[:idx] + tag + str[idx:]
        with open(os.path.dirname(st.__file__) + "/static/index.html", 'w') as file:
            file.write(new_str)

inject("<script type='text/javascript' src='https://js-cdn.dynatrace.com/jstag/<YOUR_APP_TAG_HERE>_complete.js' crossorigin='anonymous'></script>")


st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
