# Analysis of Algorithms - Lab 04
## Yachay Tech University
### School of Mathematical and Computational Sciences

**Student:** Jefferson Daniel Lamiña Valencia
**Course:** Analysis of Algorithms [cite: 3]
**Date:** March 2026

---

## Overview
This repository contains the implementation of three fundamental algorithmic tasks focused on exhaustive search and graph traversal as part of Lab 04[cite: 3].

1. **0/1 Knapsack Problem:** Solving via Exhaustive Search to analyze exponential time complexity[cite: 4].
2. **Depth First Search (DFS):** Graph traversal using an adjacency list[cite: 8, 9].
3. **Breadth First Search (BFS):** Graph traversal using an adjacency list[cite: 10, 11].

---

## 1. 0/1 Knapsack Problem (Exhaustive Search)
The goal of this task was to solve the $0/1$ Knapsack problem by exploring every possible combination of items ($2^n$ subsets) and recording the execution time for varying problem sizes $n$[cite: 4, 7].

### Execution Time Results
The following data was gathered by running the algorithm on a Fedora-based system:

| $n$ | Time (s) | $n$ | Time (s) |
| :--- | :--- | :--- | :--- |
| 4 | 0.0000 | 16 | 0.0355 |
| 5 | 0.0000 | 17 | 0.0810 |
| 6 | 0.0000 | 18 | 0.1565 |
| 7 | 0.0001 | 19 | 0.3408 |
| 8 | 0.0001 | 20 | 0.7173 |
| 9 | 0.0003 | 21 | 1.5061 |
| 10 | 0.0006 | 22 | 3.2488 |
| 11 | 0.0013 | 23 | 6.8786 |
| 12 | 0.0039 | 24 | 14.9444 |
| 13 | 0.0052 | 25 | 30.1322 |
| 14 | 0.0077 | **26** | **60.9302** |
| 15 | 0.0168 | | |

### Analysis
* **Complexity:** The growth is clearly exponential, $O(2^n)$, as the time roughly doubles with each increment of $n$.
* **10-Minute Limit:** Based on the doubling trend, $n=29$ is the largest problem size solvable within the 10-minute (600s) limit[cite: 6].

---

## 2. & 3. Graph Traversals
I implemented both **DFS** and **BFS** using an **Adjacency List**[cite: 9, 11]. This data structure was chosen because it is more memory-efficient for sparse graphs and allows for faster iteration over a node's neighbors compared to an adjacency matrix.



* **DFS:** Explores as deep as possible along each branch before backtracking[cite: 8].
* **BFS:** Explores all neighbor nodes at the present depth before moving to the next level[cite: 10].

---

## How to Run
All implementations are written in **Python**.

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-username/Analysis-of-Algorithms-Lab04.git](https://github.com/your-username/Analysis-of-Algorithms-Lab04.git)
