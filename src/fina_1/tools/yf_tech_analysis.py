import yfinance as yf
import pandas as pd
import numpy as np
from ta import add_all_ta_features
from ta.utils import dropna
from scipy.signal import find_peaks
from typing import Dict, Union, List, Tuple

def yf_tech_analysis(ticker: str, period: str = "1y") -> Dict[str, Union[float, List[float]]]:
    """
    Perform technical analysis on a given stock ticker.
    
    Args:
        ticker (str): Stock ticker symbol
        period (str): Time period for analysis (e.g., "1y" for 1 year)
    
    Returns:
        dict: Dictionary containing technical analysis results
    """
    # Fetch stock data
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    
    if df.empty:
        raise ValueError(f"No data found for ticker {ticker}")
    
    # Clean data
    df = dropna(df)
    
    # Add all technical analysis features
    df = add_all_ta_features(
        df, 
        open="Open", 
        high="High", 
        low="Low",
        close="Close", 
        volume="Volume",
        fillna=True
    )
    
    # Calculate custom indicators
    df['daily_returns'] = df['Close'].pct_change()
    df['volatility'] = df['daily_returns'].rolling(window=20).std() * np.sqrt(252)  # Annualized
    df['momentum'] = df['Close'] - df['Close'].shift(20)
    
    # Find support and resistance levels
    prices = df['Close'].values
    resistance_idx, _ = find_peaks(prices, distance=20)
    support_idx, _ = find_peaks(-prices, distance=20)
    
    resistance_levels = prices[resistance_idx][-5:]  # Last 5 resistance levels
    support_levels = prices[support_idx][-5:]        # Last 5 support levels
    
    def is_head_and_shoulders(prices: np.ndarray, window: int = 100) -> bool:
        """Detect head and shoulders pattern"""
        if len(prices) < window:
            return False
            
        recent_prices = prices[-window:]
        peaks_idx, _ = find_peaks(recent_prices, distance=10)
        
        if len(peaks_idx) >= 3:
            peak_values = recent_prices[peaks_idx]
            # Check if middle peak is higher than surrounding peaks
            for i in range(1, len(peak_values) - 1):
                if peak_values[i] > peak_values[i-1] and peak_values[i] > peak_values[i+1]:
                    # Check if surrounding peaks are within 5% of each other
                    if abs(peak_values[i-1] - peak_values[i+1]) / peak_values[i-1] < 0.05:
                        return True
        return False
    
    def is_double_top(prices: np.ndarray, window: int = 100) -> bool:
        """Detect double top pattern"""
        if len(prices) < window:
            return False
            
        recent_prices = prices[-window:]
        peaks_idx, _ = find_peaks(recent_prices, distance=10)
        
        if len(peaks_idx) >= 2:
            peak_values = recent_prices[peaks_idx]
            # Check if last two peaks are within 2% of each other
            if abs(peak_values[-1] - peak_values[-2]) / peak_values[-2] < 0.02:
                return True
        return False
    
    def is_double_bottom(prices: np.ndarray, window: int = 100) -> bool:
        """Detect double bottom pattern"""
        if len(prices) < window:
            return False
            
        recent_prices = prices[-window:]
        troughs_idx, _ = find_peaks(-recent_prices, distance=10)
        
        if len(troughs_idx) >= 2:
            trough_values = recent_prices[troughs_idx]
            # Check if last two troughs are within 2% of each other
            if abs(trough_values[-1] - trough_values[-2]) / trough_values[-2] < 0.02:
                return True
        return False
    
    # Get current values
    current_price = df['Close'].iloc[-1]
    sma_50 = df['Close'].rolling(window=50).mean().iloc[-1]
    sma_200 = df['Close'].rolling(window=200).mean().iloc[-1]
    rsi = df['momentum_rsi'].iloc[-1]
    macd = df['trend_macd'].iloc[-1]
    macd_signal = df['trend_macd_signal'].iloc[-1]
    bb_upper = df['volatility_bbh'].iloc[-1]
    bb_lower = df['volatility_bbl'].iloc[-1]
    atr = df['volatility_atr'].iloc[-1]
    
    # Detect patterns
    patterns = {
        'head_and_shoulders': is_head_and_shoulders(prices),
        'double_top': is_double_top(prices),
        'double_bottom': is_double_bottom(prices)
    }
    
    return {
        'current_price': current_price,
        'sma_50': sma_50,
        'sma_200': sma_200,
        'rsi': rsi,
        'macd': macd,
        'macd_signal': macd_signal,
        'bollinger_upper': bb_upper,
        'bollinger_lower': bb_lower,
        'atr': atr,
        'volatility': df['volatility'].iloc[-1],
        'momentum': df['momentum'].iloc[-1],
        'support_levels': support_levels.tolist(),
        'resistance_levels': resistance_levels.tolist(),
        'patterns': patterns
    }

def format_analysis_results(results: Dict[str, Union[float, List[float]]]) -> str:
    """
    Format technical analysis results into a readable string.
    
    Args:
        results (dict): Dictionary containing technical analysis results
    
    Returns:
        str: Formatted analysis results
    """
    output = []
    output.append(f"Current Price: ${results['current_price']:.2f}")
    output.append(f"50-day SMA: ${results['sma_50']:.2f}")
    output.append(f"200-day SMA: ${results['sma_200']:.2f}")
    output.append(f"RSI: {results['rsi']:.2f}")
    output.append(f"MACD: {results['macd']:.2f}")
    output.append(f"MACD Signal: {results['macd_signal']:.2f}")
    output.append(f"Bollinger Bands: Upper=${results['bollinger_upper']:.2f}, Lower=${results['bollinger_lower']:.2f}")
    output.append(f"ATR: {results['atr']:.2f}")
    output.append(f"Volatility: {results['volatility']:.2%}")
    output.append(f"Momentum: {results['momentum']:.2f}")
    
    output.append("\nSupport Levels:")
    for level in results['support_levels']:
        output.append(f"${level:.2f}")
        
    output.append("\nResistance Levels:")
    for level in results['resistance_levels']:
        output.append(f"${level:.2f}")
        
    output.append("\nPatterns Detected:")
    for pattern, detected in results['patterns'].items():
        if detected:
            output.append(f"- {pattern.replace('_', ' ').title()}")
    
    return "\n".join(output)

# Example usage
if __name__ == "__main__":
    try:
        ticker = "AAPL"  # Example ticker
        analysis = yf_tech_analysis(ticker)
        formatted_results = format_analysis_results(analysis)
        print(f"\nTechnical Analysis for {ticker}:")
        print(formatted_results)
    except Exception as e:
        print(f"Error performing technical analysis: {str(e)}")