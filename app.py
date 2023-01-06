import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('Streamlitサンプル')
st.caption('Pythonプログラミング VTuber サプーさんのYoutube見てつくったものです。一部だけ。')
st.markdown('##### 詳細は')
link = '[イチゲブログ](https://kikuichige.com/17180/)'
st.markdown(link, unsafe_allow_html=True)
col1,col2 = st.columns(2)
# name=st.text_input('名前')
# print(name)
with col1:
    with st.form(key='profile_form'):
        #テキストボックス
        name=st.text_input('名前')
        address=st.text_input('住所')
        #セレクトボックス
        age_category=st.selectbox(
            '年齢層',
            ('子供','大人'))
        #複数選択
        hobby=st.multiselect(
            '趣味',
            ('スポーツ','読書','登山','映画鑑賞')
        )
        #ボタン
        submit_btn=st.form_submit_button('送信')
        cancel_btn=st.form_submit_button('消す')
        if submit_btn:
            st.text(f'ようこそ！{name}さん{address}に書類を送りました')
            st.text(f'年齢層：{age_category}')
            st.text(f'趣味：{",".join(hobby)}')

with col2:
    df = pd.read_csv('データ.csv',index_col='月')
    st.dataframe(df)
    st.line_chart(df)
    st.bar_chart(df['2021年'])

    #matplotlib
    fig,ax=plt.subplots()
    ax.plot(df.index,df['2021年'])
    ax.set_title('matplotlig graph')
    st.pyplot(fig)
