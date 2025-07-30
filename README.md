# Demo-2025

## Text Analysis Utility - Demo 10

A comprehensive text analysis tool that provides detailed insights and statistics about text content. This utility offers both command-line and web interfaces for analyzing text in multiple ways.

### Features

**Core Analysis:**
- Word count, character count, and reading time estimation
- Sentence and paragraph counting
- Text complexity metrics (average word/sentence length)
- Most common words extraction (excluding stop words)
- Basic sentiment analysis with confidence scoring

**Interfaces:**
- **CLI Version**: Interactive command-line tool (`text_analyzer.py`)
- **Web Version**: Modern responsive web interface (`text_analyzer.html`)

### Usage

#### Command Line Interface

```bash
python3 text_analyzer.py
```

Options:
1. Analyze text from direct input
2. Analyze text from file
3. Exit

Example CLI output:
```
📊 TEXT ANALYSIS RESULTS
========================================
📝 Word Count: 52
🔤 Character Count: 318
📏 Characters (no spaces): 267
📄 Sentences: 6
📋 Paragraphs: 1
⏱️  Estimated Reading Time: 1 minute(s)

📈 COMPLEXITY METRICS
--------------------
📊 Average Word Length: 5.0 characters
📏 Average Sentence Length: 8.7 words

🔍 COMMON WORDS
---------------
1. 'amazing' - 1 times
2. 'excellent' - 1 times
3. 'beautiful' - 1 times
4. 'outstanding' - 1 times
5. 'wonderful' - 1 times

😊 SENTIMENT ANALYSIS
--------------------
Overall Sentiment: Positive
Confidence: 100%
Positive indicators: 7
Negative indicators: 0
```

#### Web Interface

Open `text_analyzer.html` in any modern web browser, or serve it locally:

```bash
python3 -m http.server 8000
# Then visit: http://localhost:8000/text_analyzer.html
```

**Web Features:**
- Real-time character counter
- Sample texts for quick testing
- Interactive analysis with visual results
- Responsive design for mobile and desktop
- Color-coded sentiment indicators
- Statistics cards with hover effects

### Demo Screenshots

**Initial Interface:**
![Text Analyzer Demo](https://github.com/user-attachments/assets/f623aad5-7d54-4ba6-9d17-fc3e194e1f39)

**Analysis Results:**
![Text Analysis Results](https://github.com/user-attachments/assets/62db89f4-fdfb-466f-9b75-c78593c9b804)

### Technical Details

**Text Processing Capabilities:**
- Stop word filtering for meaningful word analysis
- Sentiment analysis using curated positive/negative word lists
- Reading time calculation based on 200 WPM average
- Sentence detection using punctuation patterns
- Complex text metrics for readability assessment

**Technologies Used:**
- **Backend**: Pure Python 3 (no external dependencies)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Design**: Responsive grid layout with CSS gradients and transitions
- **Cross-platform**: Works on Windows, macOS, and Linux

This text analysis utility demonstrates text processing, data analysis, and user interface design while providing practical functionality for content creators, writers, and anyone who needs to analyze text content.