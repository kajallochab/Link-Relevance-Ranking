# Link-Relevance-Ranking

# Web Page Ranking Algorithms: HITS and PageRank

This project implements two popular web page ranking algorithms: HITS (Hypertext Induced Topic Search) and PageRank. These algorithms analyze the link structure of a web graph to determine the importance or relevance of individual web pages.

## Features

- **HITS Algorithm**: Calculates authority and hub scores for each node in the web graph.
- **PageRank Algorithm**: Determines the importance of web pages based on their inbound links and the importance of the linking pages.
- **Graph Class**: Manages the nodes and edges of the web graph.
- **Node Class**: Represents a node in the web graph and stores relevant information such as authority, hub, and PageRank scores.
- **Utility Functions**: Provides functions to initialize the graph from a file, perform iterations of HITS and PageRank algorithms, and retrieve ranking lists.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/kajallochab/Link-Relevance-Ranking
cd Link-Relevance-Ranking
```

2. Install dependencies:

```bash
# If using pip
pip install numpy
# If using conda
conda install numpy
```

3. Run the algorithms:

```bash
# Run HITS algorithm
python hits.py

# Run PageRank algorithm
python pg_rank.py
```