from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd




def generate_word_cloud(text_list, image_mask=None, background_color="white", max_words=200, colormap="viridis"):
    """
    Generate and display a word cloud from a list of texts.
    
    Args:
        text_list (list): List of strings containing the text for the word cloud.
        image_mask (ndarray, optional): A mask for shaping the word cloud. Defaults to None.
        background_color (str): Background color of the word cloud. Defaults to "white".
        max_words (int): Maximum number of words to display. Defaults to 200.
        colormap (str): Color map for the word cloud. Defaults to "viridis".
    
    Returns:
        None: Displays the word cloud.
    """
    # Combine the list of texts into a single string
    combined_text = " ".join(text_list)
    
    # Define stopwords to exclude common words
    stopwords = set(STOPWORDS)
    
    # Create the WordCloud object
    wordcloud = WordCloud(
        background_color=background_color,
        max_words=max_words,
        mask=image_mask,
        stopwords=stopwords,
        contour_width=1,
        contour_color='steelblue',
        colormap=colormap
    ).generate(combined_text)
    
    # Display the word cloud
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# Example usage
texts = [
    "Usable security ensures that security features are intuitive and user-friendly.",
    "Privacy tools must balance user experience with robust protection.",
    "Phishing detection relies on educating users about secure practices.",
    "Designing interfaces for security involves understanding user behavior.",
    "Two-factor authentication is a cornerstone of secure systems, improving user trust."
]
#generate_word_cloud(texts)