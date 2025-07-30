#!/usr/bin/env python3
"""
Text Analysis Utility - Demo 10
A comprehensive text analyzer that provides statistics and insights about text content.

Features:
- Word count and character analysis
- Reading time estimation
- Most common words analysis
- Basic sentiment indicators
- Text complexity metrics
"""

import re
import sys
from collections import Counter
from typing import Dict, List, Tuple

class TextAnalyzer:
    """A comprehensive text analysis tool."""
    
    def __init__(self):
        # Average reading speed (words per minute)
        self.wpm = 200
        
        # Simple positive/negative word lists for basic sentiment
        self.positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 
            'awesome', 'brilliant', 'perfect', 'outstanding', 'superb', 'marvelous',
            'love', 'like', 'enjoy', 'happy', 'pleased', 'delighted', 'excited',
            'beautiful', 'nice', 'best', 'better', 'incredible', 'magnificent'
        }
        
        self.negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'disgusting', 'hate', 'dislike',
            'sad', 'angry', 'frustrated', 'disappointed', 'upset', 'annoyed',
            'worst', 'worse', 'boring', 'stupid', 'ridiculous', 'pathetic',
            'useless', 'worthless', 'nightmare', 'disaster', 'failure'
        }
    
    def analyze_text(self, text: str) -> Dict:
        """Perform comprehensive text analysis."""
        if not text.strip():
            return {
                'error': 'Please provide some text to analyze.',
                'word_count': 0,
                'char_count': 0,
                'char_count_no_spaces': 0
            }
        
        # Basic counts
        word_count = len(text.split())
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        
        # Sentence and paragraph counts
        sentences = self._count_sentences(text)
        paragraphs = len([p for p in text.split('\n\n') if p.strip()])
        
        # Reading time estimation
        reading_time = max(1, round(word_count / self.wpm))
        
        # Common words analysis
        common_words = self._get_common_words(text, top_n=5)
        
        # Sentiment analysis
        sentiment = self._analyze_sentiment(text)
        
        # Complexity metrics
        avg_word_length = self._average_word_length(text)
        avg_sentence_length = word_count / max(1, sentences)
        
        return {
            'word_count': word_count,
            'char_count': char_count,
            'char_count_no_spaces': char_count_no_spaces,
            'sentence_count': sentences,
            'paragraph_count': paragraphs,
            'reading_time_minutes': reading_time,
            'avg_word_length': round(avg_word_length, 1),
            'avg_sentence_length': round(avg_sentence_length, 1),
            'common_words': common_words,
            'sentiment': sentiment
        }
    
    def _count_sentences(self, text: str) -> int:
        """Count sentences in text."""
        # Simple sentence counting using punctuation
        sentence_endings = re.findall(r'[.!?]+', text)
        return max(1, len(sentence_endings))
    
    def _get_common_words(self, text: str, top_n: int = 5) -> List[Tuple[str, int]]:
        """Get most common words (excluding common stop words)."""
        # Simple stop words list
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
            'before', 'after', 'above', 'below', 'between', 'among', 'is', 'are',
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does',
            'did', 'will', 'would', 'should', 'could', 'can', 'may', 'might', 'must',
            'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us',
            'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'this', 'that',
            'these', 'those', 'what', 'when', 'where', 'why', 'how', 'who'
        }
        
        # Extract words and count them
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        meaningful_words = [word for word in words if word not in stop_words and len(word) > 2]
        
        # Count and return top N
        word_counts = Counter(meaningful_words)
        return word_counts.most_common(top_n)
    
    def _analyze_sentiment(self, text: str) -> Dict:
        """Basic sentiment analysis."""
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        positive_count = sum(1 for word in words if word in self.positive_words)
        negative_count = sum(1 for word in words if word in self.negative_words)
        
        total_sentiment_words = positive_count + negative_count
        
        if total_sentiment_words == 0:
            sentiment_label = "Neutral"
            confidence = "N/A"
        elif positive_count > negative_count:
            sentiment_label = "Positive"
            confidence = f"{round(positive_count / total_sentiment_words * 100)}%"
        elif negative_count > positive_count:
            sentiment_label = "Negative"
            confidence = f"{round(negative_count / total_sentiment_words * 100)}%"
        else:
            sentiment_label = "Mixed"
            confidence = "50%"
        
        return {
            'label': sentiment_label,
            'confidence': confidence,
            'positive_words': positive_count,
            'negative_words': negative_count
        }
    
    def _average_word_length(self, text: str) -> float:
        """Calculate average word length."""
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        if not words:
            return 0
        return sum(len(word) for word in words) / len(words)
    
    def format_analysis(self, analysis: Dict) -> str:
        """Format analysis results for CLI display."""
        if 'error' in analysis:
            return f"❌ Error: {analysis['error']}"
        
        result = [
            "📊 TEXT ANALYSIS RESULTS",
            "=" * 40,
            f"📝 Word Count: {analysis['word_count']:,}",
            f"🔤 Character Count: {analysis['char_count']:,}",
            f"📏 Characters (no spaces): {analysis['char_count_no_spaces']:,}",
            f"📄 Sentences: {analysis['sentence_count']:,}",
            f"📋 Paragraphs: {analysis['paragraph_count']:,}",
            f"⏱️  Estimated Reading Time: {analysis['reading_time_minutes']} minute(s)",
            "",
            "📈 COMPLEXITY METRICS",
            "-" * 20,
            f"📊 Average Word Length: {analysis['avg_word_length']} characters",
            f"📏 Average Sentence Length: {analysis['avg_sentence_length']} words",
            "",
            "🔍 COMMON WORDS",
            "-" * 15
        ]
        
        if analysis['common_words']:
            for i, (word, count) in enumerate(analysis['common_words'], 1):
                result.append(f"{i}. '{word}' - {count} times")
        else:
            result.append("No significant words found")
        
        result.extend([
            "",
            "😊 SENTIMENT ANALYSIS",
            "-" * 20,
            f"Overall Sentiment: {analysis['sentiment']['label']}",
            f"Confidence: {analysis['sentiment']['confidence']}",
            f"Positive indicators: {analysis['sentiment']['positive_words']}",
            f"Negative indicators: {analysis['sentiment']['negative_words']}"
        ])
        
        return "\n".join(result)

def main():
    """Main CLI interface."""
    print("🔍 Text Analysis Utility - Demo 10")
    print("=" * 40)
    
    analyzer = TextAnalyzer()
    
    while True:
        print("\nOptions:")
        print("1. Analyze text from input")
        print("2. Analyze text from file")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            print("\nEnter your text (press Ctrl+D or Ctrl+Z when done):")
            try:
                text = sys.stdin.read()
            except KeyboardInterrupt:
                print("\n❌ Input cancelled.")
                continue
            
            if text.strip():
                analysis = analyzer.analyze_text(text)
                print("\n" + analyzer.format_analysis(analysis))
            else:
                print("❌ No text provided.")
        
        elif choice == '2':
            filename = input("Enter filename: ").strip()
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    text = file.read()
                analysis = analyzer.analyze_text(text)
                print("\n" + analyzer.format_analysis(analysis))
            except FileNotFoundError:
                print(f"❌ File '{filename}' not found.")
            except Exception as e:
                print(f"❌ Error reading file: {e}")
        
        elif choice == '3':
            print("👋 Thank you for using Text Analysis Utility!")
            break
        
        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()