from keybert import KeyBERT
kw_model = KeyBERT()
def keyword_extractor(text):
    keywords = [item[0] for item in kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', 
                                                                    use_mmr=True, diversity=0.5)]
    return keywords
