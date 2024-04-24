# COMPSCI 308 Design and Analysis of Algorithms Weekly Journal 5

Luyao Wang | April 21 2024

During this week's study, our focus was on shortest paths and the exploration of two popular greedy algorithms: the Bellman-Ford algorithm and Dijkstra's algorithm. Additionally, we gained an understanding of linear programming.

There are different types of shortest path problems, including single-source, single-destination, single-pair, and all-pairs problems. A key point was the **optimal substructure property** of shortest paths, indicating that they contain other shortest paths within them. We also examined the impact of negative edges on shortest path algorithms and noted that the problem remains well-defined unless **negative-weight** cycles are present.

The Bellman-Ford algorithm, a **dynamic programming** approach, was introduced as a method to establish optimal weights in the single-source shortest path problem. It achieves this by iteratively relaxing edges for $|V|-1$ times. In contrast, Dijkstra's algorithm, a **greedy** algorithm, works on graphs with **non-negative** edge weights. It employs a minimum priority queue to determine the next vertex to visit and relaxes outgoing edges accordingly.

Furthermore, we delved into the concept of linear programming, which involves optimizing linear objective functions while adhering to linear constraints. The simplex algorithm, known for iteratively improving solutions, was highlighted as an effective approach for solving linear programming problems.

Lastly, we discussed the applications of linear programming in the context of shortest path, maximum flow problems, etc. These applications demonstrated the versatility and usefulness of linear programming.
