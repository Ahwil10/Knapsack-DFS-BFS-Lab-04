# Analysis of Algorithms - Lab 04
## Yachay Tech University
### School of Mathematical and Computational Sciences

**Student:** Jefferson Daniel Lamiña Valencia
[cite_start]**Course:** Analysis of Algorithms [cite: 3]
**Date:** March 2026

---

## Overview
[cite_start]This repository contains the implementation of three fundamental algorithmic tasks focused on exhaustive search and graph traversal as part of Lab 04[cite: 3].

1. [cite_start]**0/1 Knapsack Problem:** Solving via Exhaustive Search to analyze exponential time complexity[cite: 4].
2. [cite_start]**Depth First Search (DFS):** Graph traversal using an adjacency list[cite: 8].
3. [cite_start]**Breadth First Search (BFS):** Graph traversal using an adjacency list[cite: 10].

---

## 1. 0/1 Knapsack Problem (Exhaustive Search)
[cite_start]The goal of this task was to solve the $0/1$ Knapsack problem by exploring every possible combination of items ($2^n$ subsets) and recording the execution time for varying problem sizes $n$[cite: 4, 7].

### Execution Time Results
The algorithm was executed on a Fedora-based system, yielding the following results:

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
| 15 | 0.0168 | 

### Complexity Analysis
* **Growth Pattern:** The time complexity is $O(2^n)$. [cite_start]The doubling of execution time with each increment of $n$ confirms the exponential nature of exhaustive search[cite: 4].
* [cite_start]**10-Minute Limit:** Based on these results, the maximum problem size solvable within 10 minutes (600s) is approximately **$n=29$**[cite: 6].

---

## 2. & 3. Graph Traversals
I implemented both **DFS** and **BFS** using an **Adjacency List**. [cite_start]This data structure was chosen for its space efficiency and faster neighbor iteration compared to an adjacency matrix[cite: 9, 11].



### Execution Results
Using a test graph with nodes A through F, the algorithms produced the following traversal orders:

**Depth First Search (DFS):**
> `A B D E F C`
* [cite_start]*Behavior:* The algorithm explores as deep as possible along each branch (A -> B -> D...) before backtracking to visit remaining neighbors[cite: 8].

**Breadth First Search (BFS):**
> `A B C D E F`
* [cite_start]*Behavior:* The algorithm explores all neighbor nodes at the current depth (level by level: A -> neighbors B,C -> neighbors D,E,F) before moving deeper[cite: 10].

---

## How to Run
All implementations are written in **Python**.

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/ahwil10/
