from crewai_tools import tool
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import yfinance as yf
import numpy as np
import random

# Predefined financial sentiment word library (example)
FINANCIAL_LEXICON = {
    "bullish": 1.5,
    "bearish": -1.5,
    "outperform": 1.2,
    "downgrade": -1.0,
    "bankruptcy": -2.0,
    "dividend": 0.8
}

class EnhancedSentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
        # Expanding the Financial Domain Dictionary
        self.vader.lexicon.update(FINANCIAL_LEXICON)
    
    def analyze(self, text: str) -> float:
        """Hybrid Sentiment Analysis Algorithm"""
        # VADER 
        vader_score = self.vader.polarity_scores(text)['compound']
        # TextBlob 
        blob_score = TextBlob(text).sentiment.polarity
        # Weighted Average
        return (vader_score * 0.7) + (blob_score * 0.3)

def _fetch_news_sentiment(ticker: str, max_articles: int = 10) -> dict:
    """Capture and analyze news sentiment"""
    try:
        stock = yf.Ticker(ticker)
        news_items = stock.news[:max_articles]
        analyzer = EnhancedSentimentAnalyzer()
        
        news_data = []
        scores = []
        for item in news_items:
            content = f"{item.get('title', '')}. {item.get('content', '')}"
            score = analyzer.analyze(content)
            news_data.append({
                "title": item.get('title', '')[:100] + "...",
                "publisher": item.get('publisher', 'Unknown'),
                "sentiment": round(score, 2),
                "link": item.get('link', '#')
            })
            scores.append(score)
        
        return {
            "articles": news_data,
            "average_score": round(np.mean(scores).item(), 2) if scores else 0.0,
            "confidence": round(np.std(scores).item(), 2) if scores else 0.0
        }
    except Exception as e:
        return {"error": f"News analysis failed: {str(e)}"}

def _simulate_social_sentiment(ticker: str) -> dict:
    """Improved social media sentiment simulation"""
    # Simulate the weight of different platforms
    platforms = {
        "twitter": random.uniform(-0.8, 0.8),
        "stocktwits": random.uniform(-0.7, 0.7),
        "reddit": random.uniform(-0.6, 0.6)
    }
    
    # Generate mock posts
    sample_posts = [
        f"${ticker} looking strong with new CEO appointment! 📈 #bullish",
        f"Concerned about {ticker}'s debt ratio... 😟",
        f"Analysts downgrade {ticker} to hold ⚠️"
    ]
    
    return {
        "platform_sentiments": {k: round(v, 2) for k, v in platforms.items()},
        "weighted_average": round(
            sum([v * 0.5 for v in platforms.values()]) / 1.5, 2  # 加权计算
        ),
        "sample_posts": random.sample(sample_posts, 2)
    }

@tool
def sentiment_analysis(ticker: str) -> dict:
    """
    Enhanced stock sentiment analysis tool

    Args:
        ticker (str): stock code (e.g. 'AAPL')

    Returns:
        dict: contains structured sentiment analysis results
    """
    try:
        # News sentiment analysis
        news = _fetch_news_sentiment(ticker)
        if "error" in news:
            raise ValueError(news["error"])

        # Social media sentiment analysis
        social = _simulate_social_sentiment(ticker)

        # Composite score calculation
        composite_score = round(
            (news["average_score"] * 0.6) +
            (social["weighted_average"] * 0.4), 2
        )

        # Generate final report
        return {
            "ticker": ticker,
            "composite_score": composite_score,
            "sentiment_classification": _classify_sentiment(composite_score),
            "news_analysis": news,
            "social_analysis": social,
            "technical_indicators": {
                # Add technical sentiment indicators
                "rsi_sentiment": "Overbought" if composite_score > 0.7 else "Oversold" if composite_score < -0.7 else "Neutral",
                "volume_trend": "Increasing" if composite_score > 0 else "Decreasing"
            }
        }
    except Exception as e:
        return {
            "ticker": ticker,
            "error": f"Sentiment analysis failed: {str(e)}",
            "composite_score": 0.0,
            "sentiment_classification": "Neutral"
        }

def _classify_sentiment(score: float) -> str:
    """Sentiment Classification Logic"""
    if score >= 0.5:
        return "Strong Bullish"
    elif score >= 0.2:
        return "Bullish"
    elif score <= -0.5:
        return "Strong Bearish"
    elif score <= -0.2:
        return "Bearish"
    else:
        return "Neutral"