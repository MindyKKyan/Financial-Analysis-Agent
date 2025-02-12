from crewai import Task

class FinancialTasks:
    def research_task(self, agent, company):
        return Task(
            description=f"""Conduct comprehensive analysis of {company} including:
            - Competitive positioning
            - Industry trends
            - Financial ratios""",
            agent=agent,
            expected_output="Detailed report in Markdown format with data visualizations"
        )
    
    def sentiment_task(self, agent, company):
        return Task(
            description=f"""Analyze market sentiment for {company} from:
            - News articles
            - Social media trends
            - Analyst reports""",
            agent=agent,
            expected_output="Sentiment score (-1 to 1) with supporting evidence"
        )
    
    def analysis_task(self, agent, company):
        return Task(
            description=f"""Synthesize research and sentiment data for {company}:
            - Risk-return profile
            - Valuation metrics
            - SWOT analysis""",
            agent=agent,
            expected_output="Professional investment memo with clear recommendations"
        )
    
    def strategy_task(self, agent):
        return Task(
            description="Develop portfolio strategies for different investor profiles",
            agent=agent,
            expected_output="Customized investment strategies for:\n- Conservative\n- Balanced\n- Aggressive"
        )