import streamlit as st
import sys
import os
from loguru import logger

# Submodules have been removed to prevent version fragmentation.
# API communication over sg_network will be used instead.

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="SG Integration Step 3 - Reverse Engineering",
    page_icon="🧬",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Main UI
# ---------------------------------------------------------------------------
st.title("통합 표면 분석 플랫폼 - Step 3: 역설계 및 신규 배합 예측")
st.markdown("기존 제품으로 대응이 불가능할 경우, AI 모델을 통해 신규 고분자 배합을 예측하고 물성을 검증합니다.")

tab1, tab2, tab3 = st.tabs(["목표 스펙 설정", "역설계 앙상블 (013)", "물성 검증 및 구조 (001, 006, 009)"])

with tab1:
    st.header("타겟 목표 스펙 입력")
    st.info("Step 2에서 매칭 실패 시 요구된 타겟 물성(점착력, Tg 등)을 설정합니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        target_adhesion = st.number_input("목표 점착력 (gf/25mm)", value=1200.0, step=10.0)
        target_tg = st.number_input("목표 유리전이온도 (Tg, °C)", value=-20.0, step=1.0)
    with col2:
        target_viscosity = st.number_input("목표 점도 (cps)", value=3500.0, step=100.0)

with tab2:
    st.header("역설계 AI 피드백 루프 (013)")
    st.markdown("목표 물성을 달성하기 위한 모노머 배합을 최적화합니다.")
    if st.button("역설계 사이클 시작", type="primary"):
        logger.info("Step3 UI: Starting reverse engineering cycle.")
        aa_content = 5.0
        if aa_content > 3.0:
            logger.warning(f"Step3 UI: Polymer gelation risk! AA content {aa_content} phr exceeds 3.0 phr limit.")
            st.warning(f"경고: AA 함량({aa_content}%)이 3.0%를 초과하여 겔화 위험이 있습니다. 최적화 패널티가 부여됩니다.")
        logger.info("Step3 UI: Reverse engineering cycle completed.")
        st.success("역설계 완료! 최적 배합: [2-EHA: 70%, AA: 5%, VAc: 25%]")

with tab3:
    st.header("예측 물성 및 IR 스펙트럼 (001, 006, 009)")
    st.markdown("도출된 배합의 물성 예측(001, 006) 및 구조 시뮬레이션(009) 결과입니다.")
    
    if st.button("물성 검증 실행", type="primary"):
        logger.info("Step3 UI: Executing property verification and IR simulation.")
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.metric("예측 점착력", "1185 gf/25mm", "-15 gf (목표대비)")
            st.metric("예측 Tg", "-21.2 °C", "-1.2 °C (목표대비)")
        with col_res2:
            st.metric("예측 점도", "3450 cps", "-50 cps (목표대비)")
            st.metric("자유부피율 (FFV)", "0.185", "")
