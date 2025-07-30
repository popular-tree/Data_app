import streamlit as st
import numpy as np # 수치 계산
import pandas as pd # 표 생성, 그룹화, 정렬, 병합, 엑셀에서 쓰는 기능
from datetime import datetime, timedelta # 날짜, 시간 관련

st.set_page_config(
    page_title='Data Lab',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)

# CSS 스타일 적용
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;
    }
    
    .main > div {
        max-width: 100% !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }
    
    .element-container {
        margin-bottom: 10px !important;
    }
    
    .stTextInput input {
        background-color: #f0f2f6 !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 10px 15px !important;
        font-size: 16px !important;
    }
    
    .stButton button {
        background-color: white !important;
        color: #424242 !important;
        width: 100% !important;
        border: 1px solid #ccc !important;
        border-radius: 5px !important;
        padding: 6px 12px !important;
        font-size: 14px !important;
        margin-top: 2px !important;
        margin-bottom: 2px !important;
        transition: all 0.3s !important;
    }
    
    .stButton button:hover {
        color: #1E88E5 !important;
        border-color: #1E88E5 !important;
    }
    
    .stButton button[kind="primary"] {
        background-color: #1E88E5 !important;
        color: white !important;
        border: 1px solid #1E88E5 !important;
    }

    .stButton button[kind="primary"]:hover {
        background-color: #1976D2 !important;
        color: white !important;
        border-color: #1976D2 !important;
    }
            
    .main-header {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        margin-top: 1rem;
        font-weight: 600;
        color: #333;
        line-height: 1.2;
        padding-top: 0.5rem;
        overflow: visible;
    }
            
    .sub-header {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 500;
        color: #424242;
    }
    
    .dashboard-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    .upload-box {
        border: 2px dashed #1E88E5;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
    
    .report-container {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    .dataframe {
        width: 100%;
        border-collapse: collapse;
    }
    
    .dataframe th {
        background-color: #f0f2f6;
        padding: 8px;
        text-align: left;
    }
    
    .dataframe td {
        padding: 8px;
        border-bottom: 1px solid #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

if 'active_menu' not in st.session_state:
    st.session_state.active_menu = '대시보드'

def set_menu(menu_name):
    st.session_state.active_menu = menu_name
    st.rerun()

with st.sidebar:
    st.subheader('메인메뉴')
    
    if st.button('대시보드'
                 , type='primary' if st.session_state.active_menu == '대시보드'\
                    else 'secondary'):
        set_menu('대시보드')

    elif st.button('판매 데이터 분석', type='primary' if st.session_state.active_menu == '판매 데이터 분석'\
                    else 'secondary'):
        set_menu('판매 데이터 분석')

    elif st.button('고객 데이터 분석', type='primary' if st.session_state.active_menu == '고객 데이터 분석'\
                    else 'secondary'):
        set_menu('고객 데이터 분석')

    elif st.button('문서 분석기', type='primary' if st.session_state.active_menu == '문서 분석기'\
                    else 'secondary'):
        set_menu('문서 분석기')

    elif st.button('트렌드 모니터링', type='primary' if st.session_state.active_menu == '트렌드 모니터링'\
                    else 'secondary'):
        set_menu('트렌드 모니터링')

    elif st.button('보고서', type='primary' if st.session_state.active_menu == '보고서'\
                    else 'secondary'):
        set_menu('보고서')

    elif st.button('설정', type='primary' if st.session_state.active_menu == '설정'\
                    else 'secondary'):
        set_menu('설정')

    st.divider()

# 샘플 데이터 생성
def generate_sample_data():
    #판매 데이터 생성
    if 'sales_data' not in st.session_state:
        np.random.seed(73) # 고정된 랜덤 데이터 사용
        dates = pd.date_range(end = datetime.now(), periods = 365).to_list()
        # pd.date_rang(end=종료날짜, periods=정수형_기간_입력) -> 종료날짜 - 기간
        # .to_list() : 리스트로 변환
        products = ['노트북', '스마트폰', '태블릿', '스마트워치', '데스크탑', '모니터', '키보드', '마우스', '헤드폰', '이어폰']
        categories = ['전자기기', '액세서리', '컴퓨터 주변기기']
        regions = ['서울', '부산', '인천', '대구', '광주', '대전', '울산', '경기', '제주']

        sales_data = []
        for _ in range(500): # 0~499까지의 인덱스를 사용하지 않겠다                    
            date = np.random.choice(dates)
            product_name = np.random.choice(products)
            category = np.random.choice(categories)
            price = np.random.uniform(10000, 2000000) #가격, 실수
            quantity = np.random.randint(1, 10) #수량, 정수
            customer_id = f'CUST{np.random.randint(1000, 9999)}'
            region = np.random.choice(regions)

            sales_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'product_id': f"PROD{np.random.randint(100, 999)}",
                'product_name': product_name,
                'category': category,
                'price': price,
                'quantity': quantity,
                'total': price * quantity,
                'customer_id': customer_id,
                'region': region
            })

        st.session_state.sales_data = pd.DataFrame(sales_data)

    # 고객 데이터 생성
    if 'customer_data' not in st.session_state:
        np.random.seed(73)
        customer_ids = st.session_state.sales_data['customer_id'].unique().tolist()
        names = ['김민준', '이서연', '박지민', '정수빈', '최예준', '강서윤', '윤지우', '임하은']
        segments = ['VIP', '일반', '골드', '실버', '신규']
        
        customer_data = []
        for customer_id in customer_ids:
            name = np.random.choice(names)
            email = f"{name}{np.random.randint(100, 999)}@example.com"
            phone = f"010-{np.random.randint(1000, 9999)}-{np.random.randint(1000, 9999)}"
            join_date = (datetime.now() - timedelta(days=np.random.randint(1, 1000))).strftime('%Y-%m-%d')
            segment = np.random.choice(segments)
            satisfaction = np.random.randint(1, 11)
            
            customer_data.append({
                'customer_id': customer_id,
                'name': name,
                'email': email,
                'phone': phone,
                'join_date': join_date,
                'segment': segment,
                'satisfaction': satisfaction
            })
        
        st.session_state.customer_data = pd.DataFrame(customer_data)
    
    # 트렌드 데이터 생성
    if 'trend_data' not in st.session_state:
        np.random.seed(73)
        sources = ['Twitter', 'News', 'Blog', 'Instagram', 'YouTube']
        keywords = ['인공지능', '메타버스', '블록체인', '클라우드', '사이버보안', '데이터분석', '로봇공학', '가상현실']
        dates = pd.date_range(end=datetime.now(), periods=30).tolist()
        
        trend_data = []
        for _ in range(200):
            source = np.random.choice(sources)
            keyword = np.random.choice(keywords)
            frequency = np.random.randint(1, 100)
            sentiment = np.random.uniform(-1.0, 1.0)
            date = np.random.choice(dates).strftime('%Y-%m-%d')
            
            trend_data.append({
                'source': source,
                'keyword': keyword,
                'frequency': frequency,
                'sentiment': sentiment,
                'date': date
            })
        
        st.session_state.trend_data = pd.DataFrame(trend_data)

generate_sample_data()

def show_dashboard_content():
    st.title('대시보드')

    # sale_df = st.session_state.sales_data # 원본 데이터, 건드리지 않는게 중요
    sale_df = st.session_state.sales_data.copy() # 데이터 복사본, copy로 메모리 주소를 다르게 만들어 줌
    # st.write(sale_df['date'].dtype)
    sale_df['date']=pd.to_datetime(sale_df['date'])
    # st.write(sale_df['date'].dtype)
    
    customer_df = st.session_state.customer_data.copy()
    customer_df['join_date']=pd.to_datetime(customer_df['join_date'])

    current_month = sale_df['date'].max().to_period('M')
    previous_month = current_month - 1

    current_month_df = sale_df[sale_df['date'].dt.to_period('M')==current_month]
    pre_month_df = sale_df[sale_df['date'].dt.to_period('M')==previous_month]

    #만족도 계산 함수
    def get_satisfaction(df):
        merged = df.merge(customer_df[['customer_id', 'satisfaction']], on='customer_id', how='left')
        return merged['satisfaction'].mean()

    current_sales = current_month_df['total'].sum()
    previous_sales = pre_month_df['total'].sum()

    current_avg_purchase = current_month_df['total'].mean()
    previous_avg_purchase = pre_month_df['total'].mean()

    current_satisfaction = get_satisfaction(current_month_df)
    previous_satisfaction = get_satisfaction(pre_month_df)

    # 증감률 함수
    def calc_delta(current, previous):
        if previous == 0:
            return 0
        return round((current - previous) / previous * 100, 2)

    sales_delta = calc_delta(current_sales, previous_sales)
    avg_purchase_delta = calc_delta(current_avg_purchase, previous_avg_purchase)
    satisfaction_delta = calc_delta(current_satisfaction, previous_satisfaction)

    # 데이터 확인용
    st.dataframe(current_month_df)
    st.dataframe(pre_month_df)

    # 지표 출력
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("총매출", f"{current_sales:,.0f}원", f"{sales_delta:+.2f}%")

    with col2:
        st.metric("평균 구매액", f"{current_avg_purchase:,.0f}원", f"{avg_purchase_delta:+.2f}%")

    with col3:
        st.metric("고객 만족도", f"{current_satisfaction:.2f}", f"{satisfaction_delta:+.2f}%")

def show_sales_analysis():
    data_source = st.radio('데이터 소스 선택'
                           , ['샘플 데이터', '파일 업로드'], horizontal = True)
    
    if data_source == '샘플 데이터':
        pass
    elif data_source == '파일 업로드':
        sales_df = st.session_state.sales_data.copy()
        upload_file = st.file_uploader('판매 데이터 파일 업로드'
                                       , type=['csv','xlsx','xls'])
        
        if upload_file is not None:
            try:
                if upload_file.name.endswith('.csv'): #확장자가 xlsx는
                    sales_df = pd.read_csv(upload_file) #pd.read_excel()로 처리
                    st.dataframe(sales_df)
                
                date_columns = ['날짜', 'date', 'Date', '거래일자']

                for i in date_columns:
                    if i in sales_df.columns:
                        sales_df[i] = pd.to_datetime(sales_df[i])
            except:
                pass

    col1, col2, col3 = st.columns(3)

    with col1:
        # 날짜 범위 필터
        sales_df['date'] = pd.to_datetime(sales_df['date'])
        min_date = sales_df['date'].min().date()
        max_date = sales_df['date'].max().date()
        
        date_range = st.date_input("날짜 범위 선택",
                                 [min_date, max_date],
                                 min_value=min_date,
                                 max_value=max_date)
        
        if len(date_range) == 2:
            start_date, end_date = date_range
            mask = (sales_df['date'].dt.date >= start_date) & (sales_df['date'].dt.date <= end_date)
            sales_df = sales_df[mask]
    
    with col2:
        # 제품 카테고리 필터
        categories = ["전체"] + sorted(sales_df['category'].unique().tolist())
        selected_category = st.selectbox("제품 카테고리", categories)
        
        if selected_category != "전체":
            sales_df = sales_df[sales_df['category'] == selected_category]
    
    with col3:
        # 지역 필터
        regions = ["전체"] + sorted(sales_df['region'].unique().tolist())
        selected_region = st.selectbox("지역", regions)
        
        if selected_region != "전체":
            sales_df = sales_df[sales_df['region'] == selected_region]

if st.session_state.active_menu == '대시보드':
    show_dashboard_content()
    # st.write('대시보드')
    # st.dataframe(st.session_state.sales_data)
    # st.dataframe(st.session_state.customer_data)
    # st.dataframe(st.session_state.trend_data)
elif st.session_state.active_menu == '판매 데이터 분석':
    show_sales_analysis()
    # st.write('판매 데이터 분석')
elif st.session_state.active_menu == '고객 데이터 분석':
    st.write('고객 데이터 분석')
elif st.session_state.active_menu == '문서 분석기':
    st.write('문서 분석기')
elif st.session_state.active_menu == '트렌드 모니터링':
    st.write('트렌드 모니터링')
elif st.session_state.active_menu == '보고서':
    st.write('보고서')
elif st.session_state.active_menu == '설정':
    st.write('설정')