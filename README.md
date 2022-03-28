# baby_name_trends

Data-driven Web App made with Streamlit

## Local Installation

```bash
git clone https://github.com/Rishav-12/baby_name_trends.git
cd baby_name_trends
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
streamlit run main.py
```

## Description

This is a web application that basically does exploratory data analysis on the baby names dataset, which is a public dataset with counts of baby names in the United States from 1880 to 2020.

This app filters this data by name and gender, and plots the counts against the years, thus showing the trend of a particular name.

## Technology used

- pandas for EDA
- [matplotlib](https://matplotlib.org) for creating the chart
- [streamlit](https://streamlit.io) for building the beautiful UI in minutes as well as streamlit cloud for hosting the blazingly fast web app

## License
[MIT](https://choosealicense.com/licenses/mit/)
