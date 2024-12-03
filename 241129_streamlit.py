#%%
import streamlit as st

st.title("Streamlit Example")
st.write("안녕하세요.")

st.dataframe(
    
    ({
        "컬럼1":[1,2,3,4],
 
        "컬럼2":[10,20,30,40]
    }
    )
)
x = st.slider("x")
st.write(x, 'squared is', x*x)

st.sidebar.write("사이드바에 텍스트를 작성합니다.")
st.slider("슬라이더를 테스트합니다.", 0,100,30)
st.button("버튼을 눌러보세요.")
st.checkbox("체크박스를 테스트합니다.")
