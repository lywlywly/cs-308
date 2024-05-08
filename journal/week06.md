# COMPSCI 308 Design and Analysis of Algorithms Weekly Journal 6

Luyao Wang | April 28 2024

This week we studied randomized algorithms and hash tables.

We began by discussing randomized algorithms through a hiring problem scenario. By enforcing a random order of candidates, we learned that we could hire approximately $\ln n$ candidates on average. It highlighted the importance of carefully considering the distribution of inputs in solving problems. While for some problems, assuming a reasonable input distribution allows for probabilistic analysis, for others, it may not be feasible.

Quicksort relies on randomized input to achieve efficient sorting. By randomly selecting a pivot element during each partitioning step, Quicksort achieves an average-case time complexity of $O(n \log n)$.

Moving on, we studied hash tables. A hash table, also known as a hash map, is a data structure that implements an associative array, mapping keys to values. We explored the concept of _direct addressing_, which works well when the universe of keys is reasonably small. However, we also learned that collision resolution becomes crucial when dealing with larger universes.

To address collisions, we discussed various hash functions, including division, multiplication, and universal hashing. These hash functions help distribute the keys evenly across the hash table, reducing the likelihood of collisions.

Additionally, we explored two primary collision resolution techniques: _chaining_ and _open addressing_.

Chaining involves using linked lists to handle collisions. It offers efficient insertion, search, and deletion operations, all with a time complexity of $O(1)$. However, we also noted that the worst-case behavior of chaining can be quite poor.

Alternatively, open addressing is a collision resolution technique suitable for load factors less than or equal to 1. We explored three methods of open addressing: _linear probing_, _quadratic probing_, and _double hashing_. Linear probing, although easy to implement, suffers from primary clustering. On the other hand, quadratic probing performs better by reducing primary clustering but introduces secondary clustering. Double hashing emerged as one of the best methods for open addressing, offering improved performance by utilizing two hash functions.

Lastly, we touched upon the concept of _perfect hashing_, which is suitable for __static__ sets of keys. With perfect hashing, we can avoid collisions entirely by carefully selecting hash functions at the secondary level.
