import nltk.sentiment
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()

def main():
    while True:
        user_text = input('? ')
        score = get_sentiment(user_text)
        reaction = get_reaction(score)
        print(reaction)
        print(score)
        print('')

def get_reaction(score):
    """
    Parameter score: a float between -1 and +1
    Return: An emoji as a string!
    """
    if score > 0.5:  
        return "🥰"
    if score > 0:    
        return "🙂"
    if score == 0:   
        return "😶"
    if score < -0.5: 
        return "😢"
    if score < 0:    
        return "😟"

def get_sentiment(user_text):
    """
    Parameter user_text: any text (string)
    Return: a sentiment score between -1 and +1 (float)
    """
    # 1. pass the text into the analyzer.polarity_scores function, part of the nltk package
    scores = analyzer.polarity_scores(user_text)
    # 2. extract the sentiment score. Scores is a "dictionary" (covered on May 17th)
    sentiment_score = scores['compound']

    return sentiment_score

if __name__ == '__main__':
    main()
