# COMPSCI 308 Design and Analysis of Algorithms Weekly Journal 1

Luyao Wang March 24 2024

I learned terminology and basics of algorithm, computation tractability and efficiency, and asymptotic notations in this week.

The instructor did a good job in introducing the background of algorithms and provided many read-world examples. I learned the intuition of algorithms such as in routing on a map and recipes in cooking. I was also exposed to many algorithms that was extensively used, such as PageRank for website importance ranking used in search engines, and public-key cryptograph which was used in many aspects of computer science with applications such as SSL. I also first time got to know the great book series _The Art of Computer Programming_, which might be too complex for me at this time though.

I also learned ways to analyze algorithms in terms of performance and what does it mean for an algorithm to be efficient. I learned the abstraction of **random-access machine** (RAM) model to analyze algorithms. Polynomial algorithms are tractable because when the input size id doubled from $N$ to $2N$, the bound on the running time increases from $cN^d$ ti $c(2N)^d=c\cdot 2^dN^d$, which is a constant factor of $2^d$. However, it was emphasized that even though polynomial algorithms are generally tractable, extremely high degree polynomials may still lack efficiency.

I learned the notation of **order of growth**, which is a simple characterization of the asymptotic efficiency of algorithms. While I had heard of the $O$ notation before, I hadn't been aware of the precise definitions and distinctions among the notations $O$, $\Omega$, $\Theta$, $o$, and $\theta$. Through the course, I gained a thorough understanding of these asymptotic notations, including their properties and how to prove or disprove asymptotic relations between algorithms using these notations.
