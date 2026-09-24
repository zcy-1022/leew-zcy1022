# app.py
import streamlit as st
from typing import List
import json

# 页面配置
st.set_page_config(
    page_title="立法智能审查助手",
    page_icon="⚖️",
    layout="wide"
)

# 标题
st.title("⚖️ 立法智能审查助手")
st.markdown("---")

# 侧边栏 - 功能选择
st.sidebar.title("功能模块")
function_choice = st.sidebar.radio(
    "请选择功能",
    ["法规检索", "冲突检测", "审查报告生成"]
)

# 示例法规数据库（实际项目中应连接真实数据库）
SAMPLE_REGULATIONS = {
    "广西壮族自治区环境保护条例": {
        "层级": "地方性法规",
        "制定机关": "广西壮族自治区人大常委会",
        "生效时间": "2016年7月1日",
        "核心条款": [
            "县级以上人民政府应当将环境保护工作纳入国民经济和社会发展规划",
            "排放污染物的企业事业单位应当建立环境保护责任制度"
        ]
    },
    "中华人民共和国环境保护法": {
        "层级": "法律",
        "制定机关": "全国人大常委会",
        "生效时间": "2015年1月1日",
        "核心条款": [
            "保护环境是国家的基本国策",
            "一切单位和个人都有保护环境的义务"
        ]
    }
}

# 功能1：法规检索
if function_choice == "法规检索":
    st.header("🔍 法规检索")

    search_query = st.text_input(
        "请输入检索关键词",
        placeholder="例如：环境保护、污染防治"
    )

    if st.button("开始检索") and search_query:
        st.subheader("检索结果")

        for reg_name, reg_info in SAMPLE_REGULATIONS.items():
            if search_query in reg_name or any(search_query in clause for clause in reg_info["核心条款"]):
                with st.expander(f"📄 {reg_name}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.info(f"**效力层级**：{reg_info['层级']}")
                        st.info(f"**制定机关**：{reg_info['制定机关']}")
                    with col2:
                        st.info(f"**生效时间**：{reg_info['生效时间']}")

                    st.markdown("**核心条款**：")
                    for i, clause in enumerate(reg_info["核心条款"], 1):
                        st.markdown(f"{i}. {clause}")

# 功能2：冲突检测
elif function_choice == "冲突检测":
    st.header("⚠️ 冲突检测")

    st.markdown("请输入待审查的法规草案条款：")
    draft_text = st.text_area(
        "法规草案内容",
        height=200,
        placeholder="例如：市级人民政府可以自主制定环境排放标准"
    )

    if st.button("开始检测") and draft_text:
        st.subheader("检测结果")

        # 模拟检测结果（实际项目应调用大模型API）
        st.warning("⚠️ 发现潜在冲突")

        conflict_result = {
            "冲突条款": "市级人民政府可以自主制定环境排放标准",
            "上位法依据": "《中华人民共和国环境保护法》第十五条规定：国务院环境保护主管部门制定国家环境质量标准和国家污染物排放标准",
            "冲突原因": "市级政府无权自主制定排放标准，该权限属于国务院环境保护主管部门",
            "修改建议": "建议修改为：市级人民政府可以在国家污染物排放标准基础上，制定更严格的地方污染物排放标准，报国务院环境保护主管部门备案"
        }

        col1, col2 = st.columns(2)
        with col1:
            st.error(f"**冲突条款**：{conflict_result['冲突条款']}")
            st.info(f"**上位法依据**：{conflict_result['上位法依据']}")

        with col2:
            st.warning(f"**冲突原因**：{conflict_result['冲突原因']}")
            st.success(f"**修改建议**：{conflict_result['修改建议']}")

# 功能3：审查报告生成
elif function_choice == "审查报告生成":
    st.header("📝 审查报告生成")

    project_name = st.text_input("法规名称", placeholder="例如：《广西壮族自治区XX条例》")
    review_content = st.text_area("审查内容", height=150, placeholder="请输入需要审查的法规内容")

    if st.button("生成审查报告") and project_name and review_content:
        st.subheader("审查报告")

        report = f"""
        # 法规审查意见书

        ## 一、基本信息
        - **法规名称**：{project_name}
        - **审查日期**：2026年9月24日
        - **审查机关**：广西壮族自治区司法厅

        ## 二、审查依据
        1. 《中华人民共和国立法法》
        2. 《法规规章备案条例》
        3. 《广西壮族自治区立法条例》

        ## 三、审查意见
        经审查，该法规草案整体符合上位法规定，但个别条款需要进一步修改完善：

        ### 需要修改的条款
        1. 第X条关于XX的规定，建议进一步明确执行标准
        2. 第Y条关于XX的规定，建议增加例外情形

        ## 四、修改建议
        建议起草单位对上述条款进行修改完善后，按程序报送审议。
        """

        st.markdown(report)

        # 下载按钮
        st.download_button(
            label="下载审查报告",
            data=report,
            file_name=f"{project_name}_审查报告.md",
            mime="text/markdown"
        )

# 底部信息
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>立法智能审查助手 | 2026年中国（广西）—东盟"AI+法律"应用创新大赛参赛作品</p>
    <p>技术支持：Streamlit + 大模型</p>
</div>
""", unsafe_allow_html=True)
