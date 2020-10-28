# Core2Vec

This project was developed as part of my Masters course study in Principles of Database Systems.

Group Name: Data Techies

Authors: Prudhviraj Sheela, Aman Masipeddi

This project is an implementation based project which is been inherited from a research paper published by authors "Soumya Sarkar, Aditya Bhagawat, Animesh Mukherjee" on the concept of Core2Vec. Using the implementation techniques suggested in that particular paper I had added some additional techniques to measure different performance metrics and analyze the Core2Vec system based on the results it generates within the embedding network.

Softwares Used:
1. Language Used: Python 3.7
2. IDE Used: Jupyter Notebook
3. Libraries Used: Networkx, Numpy, Gensim Models, Scipy
   (Command Used to install the libraries on command prompt: pip install networkx numpy, gensim, scipy) --> For Windows System

Program Filename:

pgm1core2vec.py : Consists the algorithm implementation for Core2Vec

pgm2.py : Consists the python code for main program calling the core2vec algorithm

Input Data Files:
Word Association Projects: University of South Florida Word Association Projects & Small World of Word Projects (SWOW).
1. Words Associated Input Files: wordsim1.txt, wordsim2.txt, mtukrt.txt, simlex.txt
2. Number Associated Input Files: lesm.txt

Output data files obtained:
1. Words Associated Output Files: outputworsim1.txt, outputworsim1.txt, outputmtukrt.txt, outputsimlex.txt
2. Number Associated Output Files: outputlesm.txt


Command Used to Run the code:
--> Inputs consist of,
Input file name (--input) --> Of the dataset considered

Output File name (--output) --> Where the result is to be obtained

Dimensions (--dimensions) --> Number of dimensions of given data, default value is 128

Walk Length (--walk-length) --> Length of the walk per source, default value is 80

Number of walks (--num-walks) --> Number of walks per source, default value is 10

Peanlty Parameter (--peanlty) --> Penalty parameter, default value is 1

Window Size (--window-size) --> Window Size (or) Context Size for optimization, default value is 10

Iterations (--iter) --> Number of epochs involved in the Stochastic Gradient Descent for smoothening the function, default value is 1

Parallel Workers (--workers) --> Number of parallel workers involved in analysing the adjacent nodes for obtaining a core, default value 
                                 is 8

Proximity level (--p) --> Return hyperparameter, default value is 1

Distant Hop Size (--q) --> Inout hyperparameter, default value is 1

Weighted (--weighted) --> To indicate whether given input data is a weighted graph

UnWeighted (--unweighted) --> To indicate whether given input data is a unweighted graph

Directed (--directed) --> To indicate whether given input data is a directed graph

Undirected (--undirected) --> To indicate whether given input data is a directed graph

--> Open the command prompt and execute the following command,

Example: python pgm2.py --input simlex.txt --output outputsimlex.txt --dimensions 128 --iter 1 --directed --weighted --walk-length 20 --num-walks-7 --p 0.8 --q 5 --penalty 4.8
