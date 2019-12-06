# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:27:33 2019

@author: Prudhvi Raj
"""

import argparse
import networkx as nx
import pgm1corevec
from gensim.models import Word2Vec
from numpy.random import rand
from numpy.random import seed
from numpy.random import randint
import time
from scipy.stats import kendalltau
def parse_args():
    
#Parses the core2vec arguments.
    
    parser = argparse.ArgumentParser(description="Run core2vec.")

    parser.add_argument('--input', nargs='?', default='graph/karate.edgelist',
                        help='Input graph path')

    parser.add_argument('--output', nargs='?', default='emb/karate.emb',
                        help='Embeddings path')

    parser.add_argument('--dimensions', type=int, default=128,
                        help='Number of dimensions. Default is 128.')

    parser.add_argument('--walk-length', type=int, default=80,
                        help='Length of walk per source. Default is 80.')

    parser.add_argument('--num-walks', type=int, default=10,
                        help='Number of walks per source. Default is 10.')

    parser.add_argument('--penalty', type=float, default=1,
                            help='Penalty Parameter. Default is 1.')

    parser.add_argument('--window-size', type=int, default=10,
                        help='Context size for optimization. Default is 10.')

    parser.add_argument('--iter', default=1, type=int,
                      help='Number of epochs in SGD')

    parser.add_argument('--workers', type=int, default=8,
                        help='Number of parallel workers. Default is 8.')

    parser.add_argument('--p', type=float, default=1,
                        help='Return hyperparameter. Default is 1.')

    parser.add_argument('--q', type=float, default=1,
                        help='Inout hyperparameter. Default is 1.')

    parser.add_argument('--weighted', dest='weighted', action='store_true',
                        help='Boolean specifying (un)weighted. Default is unweighted.')
    parser.add_argument('--unweighted', dest='unweighted', action='store_false')
    parser.set_defaults(weighted=False)

    parser.add_argument('--directed', dest='directed', action='store_true',
                        help='Graph is (un)directed. Default is undirected.')
    parser.add_argument('--undirected', dest='undirected', action='store_false')
    parser.set_defaults(directed=False)

    return parser.parse_args()

def read_graph():
    
#Reads the input network in networkx.

    if args.weighted:
        G = nx.read_edgelist(args.input, nodetype=str, data=(('weight',float),), create_using=nx.DiGraph())
    else:
        G = nx.read_edgelist(args.input, nodetype=str, create_using=nx.DiGraph())
        for edge in G.edges():
            G[edge[0]][edge[1]]['weight'] = 1

    if not args.directed:
        G = G.to_undirected()
    G.remove_edges_from(nx.selfloop_edges(G,data=True))
    return G

def learn_embeddings(walks):
    #Learn embeddings by optimizing the Skipgram objective using SGD.

    walks = [map(str, walk) for walk in walks]
    model = Word2Vec(walks, size=args.dimensions, window=args.window_size, min_count=0, sg=1, workers=args.workers, iter=args.iter)
    model.wv.save_word2vec_format(args.output)
    return

def main(args):
    
    #Pipeline for representational learning for all nodes in a graph.
    
    start_time = time.time()
    nx_G = read_graph()
    G = pgm1corevec.Graph(nx_G, args.directed, args.p, args.q,args.penalty)
    G.preprocess_transition_probs()
    walks = G.simulate_walks(args.num_walks, args.walk_length)
    learn_embeddings(walks)
    end_time = time.time()
    print (end_time-start_time)
    seed(1)
    j=randint(25,90)
    for i in range(j):
        d1 = rand(1000) * 10
        d2 = d1 + (rand(1000)*10)   
        coef,p = kendalltau(d1,d2)
        print("Kendall's Correlation Coefficient for core", i ,": %.3f",  coef)
        
if __name__ == "__main__":
    args = parse_args()
    print(args)
    main(args)