import json
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from market_research.crew import MarketResearchCrew


st.set_page_config(
    page_title="AI Market Intelligence Dashboard",
    layout="wide"
)


st.title("AI-Powered Intelligent Market Analytics Dashboard")

if "data" not in st.session_state:
    st.session_state.data = None


topic = st.text_input(
    "Enter Research Topic",
    placeholder="AI in Agriculture"
)

if st.button("Generate Intelligence Report"):

    with st.spinner("AI agents are analyzing the market..."):

        inputs = {
            "topic": topic
        }

        crew = MarketResearchCrew().crew()

        result = crew.kickoff(inputs=inputs)

        try:

            clean_result = (
                str(result)
                .replace("```json", "")
                .replace("```", "")
            )

            parsed = json.loads(clean_result)

            st.session_state.data = parsed

            st.success("Market intelligence generated successfully!")

        except Exception:

            st.error("Failed to parse AI output.")

            st.code(str(result))


if st.session_state.data:

    data = st.session_state.data

    report = data.get("executive_report", "")

    analytics = data.get("analytics", {})

    st.divider()

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            "Market Size",
            analytics.get("market_size", "N/A")
        )

    with kpi2:
        st.metric(
            "CAGR",
            analytics.get("cagr", "N/A")
        )

    with kpi3:
        st.metric(
            "AI Adoption",
            analytics.get("ai_adoption", "N/A")
        )

    with kpi4:
        st.metric(
            "Risk Level",
            analytics.get("risk_level", "N/A")
        )

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Analytics",
            "Regional Intelligence",
            "Competitors",
            "Executive Insights"
        ]
    )

    with tab1:

        forecast = analytics.get("market_forecast", {})

        forecast_df = pd.DataFrame({
            "Year": list(forecast.keys()),
            "Growth": list(forecast.values())
        })

        forecast_chart = px.line(
            forecast_df,
            x="Year",
            y="Growth",
            markers=True,
            title=f'{analytics.get("topic", "")} Market Forecast'
        )

        st.plotly_chart(
            forecast_chart,
            use_container_width=True
        )

        sentiment = analytics.get(
            "customer_sentiment",
            {}
        )

        sentiment_df = pd.DataFrame({
            "Sentiment": list(sentiment.keys()),
            "Value": list(sentiment.values())
        })

        sentiment_chart = px.pie(
            sentiment_df,
            names="Sentiment",
            values="Value",
            title="Customer Sentiment Analysis"
        )

        st.plotly_chart(
            sentiment_chart,
            use_container_width=True
        )

        swot = analytics.get("swot", {})

        radar = go.Figure()

        radar.add_trace(go.Scatterpolar(
            r=[
                swot.get("strength", 0),
                swot.get("weakness", 0),
                swot.get("opportunity", 0),
                swot.get("threat", 0)
            ],
            theta=[
                "Strength",
                "Weakness",
                "Opportunity",
                "Threat"
            ],
            fill='toself'
        ))

        radar.update_layout(
            title="SWOT Intelligence"
        )

        st.plotly_chart(
            radar,
            use_container_width=True
        )

    with tab2:

        regions = analytics.get(
            "regional_distribution",
            {}
        )

        region_df = pd.DataFrame({
            "Region": list(regions.keys()),
            "Market Share": list(regions.values())
        })

        region_chart = px.bar(
            region_df,
            x="Region",
            y="Market Share",
            title="Regional Market Distribution"
        )

        st.plotly_chart(
            region_chart,
            use_container_width=True
        )

    with tab3:

        competitors = analytics.get(
            "competitors",
            []
        )

        competitor_df = pd.DataFrame(
            competitors
        )

        if not competitor_df.empty:

            competitor_chart = px.bar(
                competitor_df,
                x="name",
                y="innovation_score",
                title="Competitor Innovation Score"
            )

            st.plotly_chart(
                competitor_chart,
                use_container_width=True
            )

            share_chart = px.pie(
                competitor_df,
                names="name",
                values="market_share",
                title="Competitor Market Share"
            )

            st.plotly_chart(
                share_chart,
                use_container_width=True
            )

    with tab4:

        st.subheader("Executive Insights")

        insights = analytics.get(
            "executive_insights",
            []
        )

        for insight in insights:

            st.info(insight)

        st.subheader(
            "Strategic Recommendations"
        )

        recommendations = analytics.get(
            "recommendations",
            []
        )

        for recommendation in recommendations:

            st.success(recommendation)

    st.divider()

    st.subheader(
        "Executive Market Intelligence Report"
    )

    st.write(report)

    st.download_button(
        label="Download Executive Report",
        data=report,
        file_name="market_report.txt",
        mime="text/plain"
    )
