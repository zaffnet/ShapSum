import networkx as nx
from nltk import word_tokenize, sent_tokenize, FreqDist,pos_tag
from nltk.corpus import stopwords, wordnet as wn
import re

# Utility functions
def clean(sent):
    '''
    A utility function that returns a a list of words in a sentence
    after cleaning it. Gets rid off uppper-case, punctuations, 
    stop words, etc.
    Returns: list (a list of cleaned words in sentence)
    '''
    words =  sent.lower() 
    words = re.findall(r'\w+', words,flags = re.UNICODE | re.LOCALE) 
    imp_words = filter(lambda x: x not in stopwords.words('english'), words)
    return imp_words
        
def semantic_score(word1, word2):
    '''
    Semantic score between two words based on WordNet
    Returns: float (the semantic score between word1 and word2)
    '''
    try:
        w1 = wn.synset('%s.n.01'%(word1))
        w2 = wn.synset('%s.n.01'%(word2))
        return wn.path_similarity(w1,w2,simulate_root = False)
    except:
        return 0
    
def draw_graph(connected, thresh):
    '''
    Draws graph as per weights and puts edges if 
    weight exceed the given thresh
    Returns: networkx Graph (nodes are sentences and edges
             are statistical and semantic relationships)
    '''
    nodes = set([n1 for n1, n2, n3 in connected] + \
                [n2 for n1, n2, n3 in connected])
    G=nx.Graph()
    for node in nodes:
        G.add_node(node)
    for edge in connected:
        if edge[2] > thresh:
            G.add_edge(edge[0], edge[1],weight = edge[2])
    return G