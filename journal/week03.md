# COMPSCI 308 Design and Analysis of Algorithms Weekly Journal 3

Luyao Wang | April 7 2024

This week, I dived deeper into graph problems and greedy algorithms. I began by delving into the concepts of Greedy algorithms, understanding their key elements and the necessary steps for developing a greedy algorithm. It involves first determine the optimal substructure of the problem and develop an recursive solution, then try to use greedy choice and prove its correctness, in the end we can convert the recursive implementation to the iterative one.

We covered the Activity Selection problem as an example of greedy algorithms, which involves selecting the maximum number of compatible activities. I discovered a theorem that states by choosing the activity with the earliest finish time in each sub-problem, we can find a maximum-size subset of mutually compatible activities.

In the realm of Elementary Graph Algorithms, I familiarized myself with various graph representations, including the adjacency matrix and adjacency list. Understanding the advantages and disadvantages of these representations in terms of space and time complexities was crucial.

Furthermore, I delved into Breadth-First Search (BFS) and its implementation using a **queue**. I came to appreciate its applications in AI, particularly in searching for available solutions, as demonstrated in algorithms like AlphaGo.

The exploration continued with Uniform-Cost Search, a traversal algorithm that utilizes a **priority queue** to determine the lowest-cost path in a weighted graph. I gained a deeper understanding of how it efficiently explores different paths based on their costs.

I learned about Depth-First Search (DFS), and its implementation using a **stack** for traversal. DFS is not optimal for finding the shortest path. Additionally, I explored the time and space complexities associated with DFS, which vary depending on the chosen implementation.

Furthermore, we delved into Iterative Deepening Depth-First Search (IDDFS), a technique that combines the benefits of both BFS and DFS. It involves performing a series of depth-limited searches with increasing depths until the goal is reached.
