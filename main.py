import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import json
from echarts import ST_DEMOS
from utils import utils
from utils import nlp
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from langchain.llms import OpenAI
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

st.set_page_config(
    page_title="Customer Experience Dashboard",
    page_icon="✅",
    layout="wide",
)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/G22qsgdv/theme-background-a7pga37i365shzk3.webp");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

# dashboard title
st.title("Customer Experience Dashboard")

supportedRestaurant = [
    'Anthology', 'Bulls Head', 'Coach & Four', 'King William', 'Kings Arms, Wilmslow', 'Miller & Carter Wilmslow',
    'Revolution Wilmslow', 'The Carters Arms', 'The Farmers Arms', 'The Grove', 'The Honey Bee', 'The Mucky Pup',
    'The Railway, Handforth', 'The Ship Styal', 'Unicorn', 'Wilmslow Tavern'
]

# top-level filters
job_filter = st.selectbox("Select the Job", supportedRestaurant)

# creating a single-element container
placeholder = st.empty()

# read data
f = open(f'./data/{job_filter}.json')
 
# returns JSON object 
data = json.load(f)

m1, m2, m3 = st.columns((1,1,1))
with m1:
    _title = data[job_filter]['info']['title']
    _add = data[job_filter]['info']['address']
    _url = data[job_filter]['info']['url']
    st.write(f'Title: {_title}')
    st.write(f'Address: {_add}')
    st.write(f'Google URL: {_url}')

# demo1 = ST_DEMOS["Pie: Simple Pie"]
gauge_rating = ST_DEMOS["Gauge: Simple Gauge"]
with m2:
    st.markdown("<h5 style='text-align: center;'>Google Review Rating</h5>", unsafe_allow_html=True)
    gauge_rating(data[job_filter]['info']['totalScore'], data[job_filter]['info']['rank'], 'main')

rating_summary = ST_DEMOS["Bar: Vertical Rating"]
with m3:
    # Access the reviewsDistribution dictionary
    reviews_distribution = data[job_filter]["info"]["reviewsDistribution"]
    # Create a list of star counts
    star_counts = [reviews_distribution[star] for star in reviews_distribution.keys()]
    rating_summary(star_counts[::-1], 'main_vertical_rating')

st.divider()

(
    tab_sa,
    tab_key_factor,
    tab_aspect,
    tab_favourite,
    tab_comparison,
    tab_ai,
    tab_contact,
) = st.tabs(
    [
        "🤖 Sentiment Analysis",
        "🔑 Keywords",
        "🤾 Aspects (voice of customers)",
        "💖 Your favourite/hated customers",
        "⌛ Comparision",
        "🧰 AI/NLP Tool",
        "🧾 Contact us",
    ]
)


with tab_sa:
    m1, m2, m3, m4, m5, m6 = st.columns((2,1,1,1,1,1))
    m1.markdown("<h3 style='text-align: left;'>Sentiment Summary</h3>", unsafe_allow_html=True)
    m2.write('')

    # Get sentiment summary
    s_sum = utils.count_sentiment(data[job_filter]['data'])
    m3.metric(label=":black[Total]", value=s_sum['pos'] + s_sum['neg'] + s_sum['neu'])
    m4.metric(label =":green[Positive]", value = s_sum['pos'])
    m5.metric(label =":red[Negative]", value = s_sum['neg'])
    m6.metric(label =":blue[Neutral]", value = s_sum['neu'])

    st.divider()

    # Chart
    st.markdown("<h3 style='text-align: left;'>Sentiment Monthly Trend</h3>", unsafe_allow_html=True)
    dataChart = utils.getSentimentTrendChartData(data[job_filter]['data'])
    sTrend = ST_DEMOS["Line: Stacked Line Chart"]
    sTrend(dataChart['date'], dataChart['pos'], dataChart['neg'], dataChart['neu'])

    st.divider()

    m1, m2 = st.columns((1,2))
    with m1:
        st.markdown("<h3 style='text-align: left;'>Sentiment Score</h3>", unsafe_allow_html=True)
        # Score: Max = 100, formula = pos/(pos+neu+neg)
        totalScore = 0
        if (dataChart['neg'][-1] == 0 and dataChart['neu'][-1] == 0):
            totalScore = 100
        else:
            totalScore = dataChart['pos'][-1]*100/ (dataChart['pos'][-1]+dataChart['neg'][-1] + dataChart['neu'][-1])
        scoreGauge = ST_DEMOS["Gauge: Full Circle Gauge"]
        scoreGauge(totalScore)
        m11, m22 = st.columns(2)
        m11.metric(label="Highest", value=max(dataChart['score']))
        m22.metric(label="Lowest", value=min(dataChart['score']))
    with m2:
        st.markdown("<h3 style='text-align: left;'>Sentiment Score Monthly Trend</h3>", unsafe_allow_html=True)
        scoreChart = ST_DEMOS["Bar: Basic Bar"]
        scoreChart(dataChart['date'], dataChart['score'])
    
    st.divider()

with tab_key_factor:
    st.markdown("<h3 style='text-align: left;'>Entity by Sentiment</h3>", unsafe_allow_html=True)
    # Key by sentiment
    entityFreg = utils.getAdjFrequencyData(data[job_filter]['data'])
    scoreChart = ST_DEMOS["Bar: Horizontal Stacked Bar"]
    scoreChart(entityFreg['words'], entityFreg['pos'], entityFreg['neg'], entityFreg['neu'], "horizontal_entity")   
    st.divider()

    st.markdown("<h3 style='text-align: left;'>Emotional words</h3>", unsafe_allow_html=True)
    
    m1, m2 = st.columns(2)
    mostCommon = utils.getMostCommonAdj(data[job_filter]['data'])
    with m1:
        st.markdown("<h4 style='text-align: left;'>Positive</h4>", unsafe_allow_html=True)
        df = pd.DataFrame()
        posWords = []
        noDuplicate = []
        pos_percentage = []
        for i in mostCommon['pos']:
            posWords.append(i[0])
            noDuplicate.append(i[1])
            pos_percentage.append(i[1]*100 /s_sum['pos'])
        df['Words'] = posWords
        df['Frequency'] = noDuplicate
        df['Weights'] = pos_percentage
        st.dataframe(df, use_container_width=True)

    with m2:
        st.markdown("<h4 style='text-align: left;'>Negative</h4>", unsafe_allow_html=True)
        df = pd.DataFrame()
        negWords = []
        noDuplicate = []
        neg_percentage = []
        for i in mostCommon['neg']:
            negWords.append(i[0])
            noDuplicate.append(i[1])
            neg_percentage.append(i[1]*100 /(s_sum['neg'] + s_sum['neu']))
        df['Words'] = negWords
        df['Frequency'] = noDuplicate
        df['Weights'] = neg_percentage
        st.dataframe(df, use_container_width=True)
    st.divider()

    st.markdown("<h3 style='text-align: left;'>Word Cloud</h3>", unsafe_allow_html=True)
    allNouns, allAdjs = utils.allTexts(data[job_filter]['data'])
    allNounsStr = ', '.join(allNouns)
    allAdjsStr = ', '.join(allAdjs)
    m1, m2 = st.columns(2)
    with m1:
        st.markdown("<h4 style='text-align: left;'>Entity</h4>", unsafe_allow_html=True)
        # Display the generated image:
        figN = plt.figure()
        wordcloud = WordCloud( background_color="white").generate(allNounsStr)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(figN)
    with m2:
        st.markdown("<h4 style='text-align: left;'>Emotion</h4>", unsafe_allow_html=True)
        figA = plt.figure()
        wordcloud = WordCloud( background_color="white").generate(allAdjsStr)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(figA)
    # Most common positive negative
    # Word cloud
with tab_aspect:
    st.markdown("<h3 style='text-align: left;'>Customer's Voice</h3>", unsafe_allow_html=True)
    m1, m2 = st.columns(2)
    customerVoices = utils.getThreeWords(data[job_filter]['data'])
    with m1:
        st.markdown("<h4 style='text-align: left;'>Positive</h4>", unsafe_allow_html=True)
        posVoiceChart = ST_DEMOS["Bar: Basic Vertical Bar"]
        posVoiceChart(customerVoices['pos'], customerVoices['posValue'], "Seriousness", 1, "customer_voice_positive")
    with m2:
        st.markdown("<h4 style='text-align: left;'>Negative</h4>", unsafe_allow_html=True)
        negVoiceChart = ST_DEMOS["Bar: Basic Vertical Bar"]
        negVoiceChart(customerVoices['neg'], customerVoices['negValue'], "Seriousness", 1, "customer_voice_negative")

    st.divider()
    st.markdown("<h3 style='text-align: left;'>Aspect Co-occurrence</h3>", unsafe_allow_html=True)
    heatmapAspectCooccurrence, vocab = utils.process_co_occurrence_matrix(data[job_filter]['data'])
    figHeatmapAspect = px.imshow(heatmapAspectCooccurrence, text_auto=True, labels=dict(x="Aspect", y="Aspect", color="Seriousness"),
                x=vocab,
                y=vocab, aspect="auto",height=600)
    st.plotly_chart(figHeatmapAspect, theme="streamlit", use_container_width=True)

    st.divider()
    st.markdown("<h3 style='text-align: left;'>Emotion Aspect Co-occurrence</h3>", unsafe_allow_html=True)
    heatmapEmotionCooccurrence, hX, hY = utils.getEmotionAspect(data[job_filter]['data'])
    figHeatmapAspect = px.imshow(heatmapEmotionCooccurrence, text_auto=True, labels=dict(x="Aspect", y="Emotion", color="Seriousness"),
                x=hX,
                y=hY, aspect="auto",height=600)
    st.plotly_chart(figHeatmapAspect, theme="streamlit", use_container_width=True)  

with tab_favourite:
    st.markdown("<h3 style='text-align: left;'>Your Favourite/Hated Customers</h3>", unsafe_allow_html=True)
    st.divider()
    dataFavourite = utils.getMostSentences(data[job_filter]['data'])
    st.markdown("<h4 style='text-align: left;'>Favourite</h4>", unsafe_allow_html=True)
    dfPos = pd.DataFrame()
    dfPos['Name'] = dataFavourite['pos']['name']
    dfPos['URL'] = dataFavourite['pos']['link']
    dfPos['Review'] = dataFavourite['pos']['sentence']
    dfPos['Liked Count'] = dataFavourite['pos']['likedCount']
    dfPos['Rating'] = dataFavourite['pos']['star']
    dfPos['Number of reviewed'] = dataFavourite['pos']['noReview']
    dfPos['Time'] = dataFavourite['pos']['time']
    st.dataframe(dfPos, use_container_width=True)

    st.divider()
    st.markdown("<h4 style='text-align: left;'>Hated</h4>", unsafe_allow_html=True)
    dfNeg = pd.DataFrame()
    dfNeg['Name'] = dataFavourite['neg']['name']
    dfNeg['URL'] = dataFavourite['neg']['link']
    dfNeg['Review'] = dataFavourite['neg']['sentence']
    dfNeg['Liked Count'] = dataFavourite['neg']['likedCount']
    dfNeg['Rating'] = dataFavourite['neg']['star']
    dfNeg['Number of reviewed'] = dataFavourite['neg']['noReview']
    dfNeg['Time'] = dataFavourite['neg']['time']
    st.dataframe(dfNeg, use_container_width=True)
    


with tab_comparison:
    st.write(
        "Please select two pubs you want to compare. Then, the results will show accordingly!"
    )

    m1, m2 = st.columns(2)
    with m1:
        job_filter_1 = st.selectbox("Select the Job", supportedRestaurant, 0, key="company_a")
    with m2:
        job_filter_2 = st.selectbox("Select the Job", supportedRestaurant, 1, key="company_b")

    f1 = open(f'./data/{job_filter_1}.json')
    data1 = json.load(f1)
    f2 = open(f'./data/{job_filter_2}.json')
    data2 = json.load(f2)
    mJob1, mJob2 = st.columns(2)
    with mJob1:
        _title1 = data1[job_filter_1]['info']['title']
        _add1 = data1[job_filter_1]['info']['address']
        _url1 = data1[job_filter_1]['info']['url']
        st.write(f'Title: {_title1}')
        st.write(f'Address: {_add1}')
        st.write(f'Google URL: {_url1}')
    with mJob2:
        _title2 = data2[job_filter_2]['info']['title']
        _add2 = data2[job_filter_2]['info']['address']
        _url2 = data2[job_filter_2]['info']['url']
        st.write(f'Title: {_title2}')
        st.write(f'Address: {_add2}')
        st.write(f'Google URL: {_url2}')

    i1 = data1[job_filter_1]['info']
    i2 = data2[job_filter_2]['info']
    d1 = data1[job_filter_1]['data']
    d2 = data2[job_filter_2]['data']
    st.divider()

    mRank1, mRank2 = st.columns(2)
    with mRank1:
        mRank1m1, mRank1m2,mRank1m3,mRank1m4 = st.columns(4)
        s_sum1 = utils.count_sentiment(d1)
        mRank1m1.metric(label=":black[Total]", value=s_sum1['pos'] + s_sum1['neg'] + s_sum1['neu'])
        mRank1m2.metric(label =":green[Positive]", value = s_sum1['pos'])
        mRank1m3.metric(label =":red[Negative]", value = s_sum1['neg'])
        mRank1m4.metric(label =":blue[Neutral]", value = s_sum1['neu'])
    with mRank2:
        mRank2m1, mRank2m2,mRank2m3,mRank2m4 = st.columns(4)
        s_sum2 = utils.count_sentiment(d2)
        mRank2m1.metric(label=":black[Total]", value=s_sum2['pos'] + s_sum2['neg'] + s_sum2['neu'])
        mRank2m2.metric(label =":green[Positive]", value = s_sum2['pos'])
        mRank2m3.metric(label =":red[Negative]", value = s_sum2['neg'])
        mRank2m4.metric(label =":blue[Neutral]", value = s_sum2['neu'])

    st.divider()


    mRate1, mRate2 = st.columns(2)
    with mRate1:
        gauge_rating = ST_DEMOS["Gauge: Simple Gauge"]
        st.markdown("<h5 style='text-align: center;'>Google Review Rating</h5>", unsafe_allow_html=True)
        gauge_rating(i1['totalScore'], i1['rank'],'company_a1')
        rating_summary = ST_DEMOS["Bar: Vertical Rating"]
        # Access the reviewsDistribution dictionary
        reviews_distribution = i1["reviewsDistribution"]
        # Create a list of star counts
        star_counts = [reviews_distribution[star] for star in reviews_distribution.keys()]
        rating_summary(star_counts[::-1], 'company_a_vertical_rating')

    with mRate2:
        gauge_rating = ST_DEMOS["Gauge: Simple Gauge"]
        st.markdown("<h5 style='text-align: center;'>Google Review Rating</h5>", unsafe_allow_html=True)
        gauge_rating(i2['totalScore'], i2['rank'], 'company_b1')
        rating_summary = ST_DEMOS["Bar: Vertical Rating"]
        # Access the reviewsDistribution dictionary
        reviews_distribution = i2["reviewsDistribution"]
        # Create a list of star counts
        star_counts = [reviews_distribution[star] for star in reviews_distribution.keys()]
        rating_summary(star_counts[::-1], 'company_b_vertical_rating')      

    st.divider()




with tab_ai:
    st.write(
        "Explore the sentiment feature powered by cutting-edge AI/NLP technology, providing valuable insights into the emotional tone of text. Gain a deeper understanding with sentiment analysis, categorizing content as Positive, Negative, or Neutral based on advanced linguistic analysis."
    )
    st.divider()

    st.markdown("<h4 style='text-align: left;'>Sentence full-packaged sentiment</h4>", unsafe_allow_html=True)
    with st.form('my_form'):
        text = st.text_area('Enter text:', 'I really love this food, its full of flavor and has complex texture.')
        submitted = st.form_submit_button('Submit')
        if submitted:
            fStatus, fEmo, fKeywords = nlp.sentiment(text)
            _fKeywordsList = []
            for i in fKeywords:
                _fKeywordsList.append(i[0])
            _fKeywords = ' '.join(_fKeywordsList).split()
            st.write(f'The sentence sentiment: {fStatus}')
            st.write(f'The sentence emotion: {fEmo}')
            st.write(f'List keywords in the sentence are: {_fKeywords}')

    st.divider()
    st.markdown("<h4 style='text-align: left;'>Chat-GPT</h4>", unsafe_allow_html=True)
    openai_api_key = st.text_input('OpenAI API Key')

    with st.form('my_form_gpt'):
        text = st.text_area('Enter text:', 'What are the best pubs in Wilmslow?')
        submitted = st.form_submit_button('Submit')
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text)


with tab_contact:
    st.markdown("<h5 style='text-align: center;'>Contact form 💌</h5>", unsafe_allow_html=True)
    with st.form('my_form1'):
        text1 = st.text_area('Your Email:')
        text2 = st.text_area('Your Message:')
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Done, thank you!')
            st.balloons()
