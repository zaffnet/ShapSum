from operator import itemgetter
import networkx as nx

# Convergence threshold is the maximum error in score convergence of TextRank
CONVERGENCE_THRESHOLD = 0.0001

def textrank_weighted(graph, initial_value=None, damping=0.85):
    '''
    Calculates PageRank for an undirected graph
    Returns: A list of tuples representing sentences and respective
    scores in descending order
    '''
    if initial_value == None: initial_value = 1.0 / len(graph.nodes())
    scores = dict.fromkeys(graph.nodes(), initial_value)

    iteration_quantity = 0
    for iteration_number in xrange(100):
        iteration_quantity += 1
        convergence_achieved = 0
        for i in graph.nodes():
            rank = 1 - damping
            for j in graph.neighbors(i):
                neighbors_sum = sum([graph.get_edge_data(j, k)['weight'] for k in graph.neighbors(j)])
                rank += damping * scores[j] * graph.get_edge_data(j, i)['weight'] / neighbors_sum

            if abs(scores[i] - rank) <= CONVERGENCE_THRESHOLD:
                convergence_achieved += 1

            scores[i] = rank

        if convergence_achieved == len(graph.nodes()):
            break
    return sorted(scores.items(), key=itemgetter(1), reverse=True)