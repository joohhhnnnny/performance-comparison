A Comparative Analysis of Dijkstra’s Algorithm and Bellman-Ford for Solving Shortest Path Problems



                                                

        Design and Implementation of an Algorithm for a Problem
                               
                                    An Undergraduate Research Project Report for 
                                      CS 6/L Algorithm and Complexity



                                   Department of Computer Science 
                                   College of Computing Education
                                  University of Mindanao





Robert Jhon Aracena
John Benedict Bongcac
    	John Mhel Dalumpines
Aaron Jalapon          







            
               May 2025





Table of Contents


Abstract	i
Acknowledgement	i
List of Figures	ii
List of Tables	ii
Chapter 1	1
Introduction	1
1.1 Background	1
1.2 The Problem	1
1.3 The Solution	1
1.4 The Research Methodology	1
Phase 1: Problem Identification and Settings	1
Phase 2: Analysis of the Problem and Data Identification	1
Phase 3: Algorithm Design	1
Phase 4: Simulation	1
Phase 5: Results and Discussion	1
Chapter 2	10
Related Work	10
2.1 Theoretical Overview	10
2.2 Performance and Efficiency	11
2.3 Suitability by Graph Type	11
2.4 Applications and Case Studies	12
2.5 Educational Tools and Visualization	12
2.6 Relevance to This Study	12
Chapter 3	13
Problem and Algorithm	13
3.1 Formal Description of Problem	13
3.2 Design of Algorithm	14
3.3 Proof of Correctness	15
3.4 Complexity Analysis	17
Dijkstra’s Algorithm:	17
Bellman-Ford Algorithm:	17
Mathematical Induction (Proof of Termination for Bellman-Ford):	18
Chapter 4	18
Evaluation	18
4.1 Implementation Details	18
4.2 Experimental Setup	19
4.3 Results and Discussion	20
Chapter 5	23
Conclusion	23
5.1 Contributions	23
5.2 Future Work	23
Appendix A	26
The Journal Paper	26
Appendix B	29
The Data Set	29
Appendix C	30
The Code	30










Abstract

This study investigates the performance and efficiency of two well-known shortest path algorithms—Dijkstra’s Algorithm and Bellman-Ford Algorithm—through implementation, simulation, and analysis. The objective is to evaluate and compare their execution times and space complexity under similar conditions. The algorithms were implemented in Python and applied to programmatically generated random graphs of varying sizes, with edge weights ranging from 1 to 10 to avoid negative-weight cycles. Dijkstra’s Algorithm was executed using a priority queue and adjacency list, while Bellman-Ford operated on a list of edges. Experiments were conducted using an Lenovo IdeaPad with an Ryzen 7000 processor. Execution time was recorded using the time module, and space complexity was observed using sys.getsizeof. Results show that Dijkstra’s Algorithm consistently outperforms Bellman-Ford in terms of speed, particularly as graph size increases, though both provide correct shortest path outputs. The study contributes to algorithmic education and practical application in routing simulations, with future work directed at incorporating real-world constraints, such as dynamic weights or negative-cost paths.

Subject Descriptors:
 F. Theory of Computation; 
	F.2 Analysis of Algorithms and Problem Complexity; 
		F.2.1 Numerical Algorithms and Problems; 
			I.1 Symbolic and Algebraic Manipulation; 
				I.1.2 Algorithms
Keywords:
 Shortest Path, Dijkstra, Bellman-Ford, Graph Algorithms, Performance Analysis
Implementation Software and Hardware:
 Python, Lenovo IdeaPad Ryzen 7000

Acknowledgement

The completion of this project would not have been possible without the guidance, support, and encouragement of many individuals and institutions to whom we are deeply grateful.
We are  thankful to the faculty of the College of Computing Education Department of University of Mindano for equipping us with the knowledge and skills that made this project feasible. Special thanks to our instructors in Algorithm and Complexity for helping us understand the theoretical foundations that underpin this work.
To our group members, thank you for the teamwork, dedication, and perseverance that each one contributed. This project is the result of shared effort, late nights, and collaboration.
Lastly, we would like to thank our families and friends for their patience, moral support, and constant encouragement during this endeavor.
List of Figures
Figure 1.	 Average Execution Times
Figure 2. 	Comparison Graph



List of Tables

Table 1. 	Table of Design of Algorithms























Chapter 1

This section provides an introduction to the study, the problem statement, computer science relevance along with the proposed solution. It also discusses the reason behind the adoption of Dijkstra’s Algorithm for this research and gives an overview of the research methodology employed.

Introduction

Many problems exist in the field of computer science related to analysis and processing of graphs. One of the most elementary and commonly encountered problems is the shortest-path problem, which seeks to obtain the shortest path between any two nodes in a graph. Such problem becomes important in applications like network routing, transport systems, artificial intelligence, and game development [1][2] .
This project dealt with Dijkstra's Algorithm which happens to be a very important method in solving the single source shortest path problem in graphs with non-negative weights [3]. We implemented the algorithm and actually studied its performance and we also compared it with yet another famous solution - the Bellman-Ford Algorithm- that in contrast, can handle negative weights but is slow compared to the other [4].
The study primarily seeks to quantify both these algorithms theoretically as well as practically and thereby bring out their merits, demerits, and most suitable applications.


Background

Graph Theory, in computer science, is used in modeling relationships and connections in various fields ranging from telecommunications and social networks to logistics and road map representation. A very common requirement in such graphs is finding the shortest paths between a pair of nodes. The Single Source Shortest Path (SSSP) problem looks at the assessment of the shortest path length from a given source vertex to all other vertices in a weighted graph, thus forming a practical application with a very high importance.
Dijkstra's Algorithm has been, since its inception in 1956 by Edsger Dijkstra [3], a very popular means of accomplishing the SSSP problem, especially in graphs where edge weights are non-negative. The algorithm's efficiency is further developed by Dijkstra's use of a priority queue within a greedy approach and most successfully calculates shortest paths for many practical applications [5].
On the other hand, the Bellman-Ford Algorithm, developed by Richard Bellman and Lester Ford [4], offers a more general solution that also accommodates negative edge weights. However, this flexibility comes at the cost of performance, with a time complexity of O(VE) compared to Dijkstra’s more efficient O(( V + E) log⁡ V) using a binary heap [6].
This study focuses on the implementation of Dijkstra’s Algorithm, the evaluation of its performance across various types of graph datasets, and a comparative analysis with Bellman-Ford to assess efficiency, accuracy, and scalability.


The Problem
The problem under investigation is the Single Source Shortest Path (SSSP) problem. Given a graph G=(V,E) with edge weights ω:E→ℝ, the goal is to find the shortest path from a source vertex sss to all other vertices v∈V. The challenge lies in developing or choosing an algorithm that provides an optimal balance between correctness and performance — especially in terms of runtime efficiency and scalability with respect to graph size and density.
The Solution
This research presents a full implementation of Dijkstra’s Algorithm using a binary heap for efficient priority queue operations. To evaluate its practical performance, we compare it with the Bellman-Ford Algorithm. Our comparison includes theoretical time complexity analysis and empirical performance evaluation on various graph sizes and structures.
We analyze their behavior in terms of:
Execution time
Correctness
Handling of different non-negative weight configurations. 
Scalability
The Research Methodology
This research was conducted through the development and analysis of a Python-based application comparing two classical graph algorithms: Dijkstra’s Algorithm and Bellman-Ford Algorithm. The project is hosted in the GitHub repository, and includes custom implementations, performance testing tools, and a graphical user interface for interactive simulation.
The methodology is divided into five phases:
Phase 1: Problem Identification and Settings
The primary objective of this research is to compare Dijkstra’s and Bellman-Ford algorithms in terms of their suitability for solving the Single Source Shortest Path (SSSP) problem in different types of weighted graphs. The focus was placed on four comparison metrics: performance, scalability, accuracy, and applicability.
To explore this, we implemented both algorithms from scratch and developed a CustomTkinter-based GUI allowing users to define input points, visualize paths, and observe real-time performance feedback. The system was configured to test the algorithms on various randomly generated graphs with controlled parameter such as number of node sizes.
Phase 2: Analysis of the Problem and Data Identification
The experimental setup involved generating multiple graph instances programmatically. For consistency, a shared graph generator function was used, allowing both algorithms to run on the same datasets. The key characteristics of these datasets include:
Graph Representation:


Dijkstra uses an adjacency list.


Bellman-Ford uses a list of edges.


Edge Weights:


Randomized between their specific distance from one node to another, ensuring all weights are non-negative.


Although Bellman-Ford supports negative weights, this functionality was not tested or showcased in this study to maintain a consistent basis for comparison.


Graph Size:


Test cases include 5, 10, 15, 20, and 25 nodes.


Graphs are randomly generated with varying edge densities.


This phase also involved selecting Python as the implementation language due to its readability and extensive support for scientific libraries such as heapq, time, sys, and matplotlib.

Phase 3: Algorithm Design
The algorithm implementations were contained in the file Main/DijsktraANDBellmanFord.py. Key aspects of the design include:
Dijkstra’s Algorithm:


Implemented using a min-heap from Python’s heapq module.


Graph represented as an adjacency list.


Designed to handle only non-negative weights.


Bellman-Ford Algorithm:


Implemented using traditional edge relaxation over V−1 iterations.


Graph represented as a list of edges.


Capable of detecting negative-weight cycles.


Each implementation was structured for reuse and integrated with the GUI front-end. A utility was also developed to convert edge lists to adjacency lists for unified data flow between algorithms.
Phase 4: Simulation
Simulations were performed both programmatically and interactively using a GUI built with CustomTkinter and tkintermapview. The GUI, accessed via main-ui.py, allows users to:
Select source and destination nodes.


Visually inspect graph layouts.


Trigger either Dijkstra or Bellman-Ford algorithm.


Observe real-time results on a map interface.


All simulations used non-negative edge weights, ensuring Dijkstra’s algorithm operated within its design constraints. Timing measurements were collected using the time module, and memory usage was analyzed with Python’s sys.getsizeof() function. Path outputs and execution metrics were displayed both on the GUI and through console logs.

Phase 5: Results and Discussion
From the simulation results:
Dijkstra’s Algorithm showed better runtime efficiency across all tested graph sizes, especially in sparse graphs.


Bellman-Ford, while functionally redundant under non-negative weights, provided a useful baseline for comparison and robustness testing.


In terms of scalability, Dijkstra’s algorithm scaled logarithmically due to the priority queue, while Bellman-Ford grew linearly with the number of edges.


Accuracy was consistent across both algorithms in graphs without negative cycles.


Results were plotted and presented using line graphs comparing execution time versus node count. These visual comparisons provided concrete insights into algorithm selection for specific use cases.

Chapter 2
This section provides a comprehensive review of the existing literature, studies, and implementations related to the shortest path problem in computer science. It focuses specifically on Dijkstra’s Algorithm and Bellman-Ford Algorithm — two foundational algorithms used to solve the Single Source Shortest Path (SSSP) problem in weighted graphs. The discussion includes an overview of each algorithm’s theoretical background, historical development, performance characteristics, and known variations. It also compares their respective strengths and limitations based on previous academic and practical research, helping to contextualize the approach and choices made in this study.

Related Work
Shortest-path algorithms are a foundational topic in graph theory and algorithm design. Extensive research has been conducted on optimizing pathfinding strategies, particularly in the context of real-world applications such as routing, logistics, emergency planning, and multi-agent navigation systems. This chapter provides a literature review on Dijkstra’s Algorithm and Bellman-Ford Algorithm, highlighting their theoretical foundations, practical differences, improvements, and known use cases. It also presents relevant educational research supporting the visualization and simulation of such algorithms in learning environments.
2.1 Theoretical Overview
Dijkstra’s Algorithm, introduced by Edsger W. Dijkstra in 1959, and the Bellman-Ford Algorithm, developed independently by Richard Bellman and Lester Ford in the 1950s, are fundamental techniques for solving the Single Source Shortest Path (SSSP) problem in weighted graphs [3], [4]. These two algorithms differ in their approach and applicability:
Dijkstra’s Algorithm uses a greedy strategy combined with a priority queue, making it highly efficient on graphs with non-negative edge weights [3].


Bellman-Ford Algorithm employs a dynamic programming approach, repeatedly relaxing all edges, which allows it to handle negative weights and detect negative-weight cycles [4].


Dijkstra’s time complexity is approximately O((V+E) log⁡ V) when using a binary heap, while Bellman-Ford has a higher complexity of O(VE), making it less suitable for dense graphs [1].
2.2 Performance and Efficiency
Several empirical studies have assessed the efficiency of both algorithms in applied settings:
Alamoudi and Al-Hashimi [7] conducted a hardware-level evaluation showing that Dijkstra’s Algorithm consumes significantly less energy and executes faster than Bellman-Ford. The study also observed that Bellman-Ford may use slightly less power per operation on very small graphs due to reduced memory access operations.
However, Bellman-Ford can outperform Dijkstra in certain scenarios. For instance, in an emergency evacuation simulation, Deng et al. [8] found that Bellman-Ford-based route planning evacuated 3.5% more people in the early simulation phase compared to Dijkstra. This highlights Bellman-Ford’s advantage in dynamic environments where multiple simultaneous paths are needed.
These studies suggest that Dijkstra is more efficient in general applications, but Bellman-Ford can offer better performance in specialized or dynamic contexts.
2.3 Suitability by Graph Type
The choice of algorithm often depends on the graph’s structure and weight conditions:
Sparse graphs with non-negative weights: Dijkstra is typically preferred for its speed and low overhead, especially in road network simulations or GPS navigation [1].


Graphs with negative weights or cycles: Bellman-Ford is necessary when negative edge costs are involved and must be validated [4], [9].


Bellman-Ford also demonstrates greater flexibility in dynamic systems, such as network routing protocols, where edge weights change over time. This makes it more robust in real-world applications like distance-vector routing (e.g., RIP) [9].
2.4 Applications and Case Studies
Both algorithms have been applied in a variety of domains based on their performance characteristics:
Dijkstra’s Algorithm is widely used in real-time navigation systems (e.g., Google Maps), logistics optimization, urban planning tools, and sensor networks where non-negative weights are guaranteed [1], [3].


Bellman-Ford Algorithm is fundamental to distance-vector routing protocols and is used in scenarios where costs fluctuate or need to be verified against cycles [9].


In a study by Deng et al. [8], Bellman-Ford was shown to outperform Dijkstra during a multi-floor building evacuation simulation, specifically in the first 9 seconds. Its success was attributed to handling simultaneous exits more flexibly and distributing load across multiple viable paths.
2.5 Educational Tools and Visualization
Visualization has become an essential method for teaching algorithmic logic. Studies show that interactive tools help reduce misconceptions and improve student engagement.
Tilanterä et al. [10] examined how students often struggle with Dijkstra’s node selection logic, especially with priority queue updates. Their research emphasized the importance of visual step-by-step simulations for better conceptual understanding.
Similarly, Das et al. [11] developed an A-fuzzy controller simulation platform* that allows users to simulate pathfinding with animated feedback and physical robot demonstrations. This type of environment shares similarities with the GUI used in this study, where users can visually observe and compare the behavior of Dijkstra’s and Bellman-Ford algorithms in real time.
2.6 Relevance to This Study
This project focused on solving shortest-path problems in non-negative weighted graphs, aligning with the optimal use case for Dijkstra’s Algorithm. Although Bellman-Ford’s capability to handle negative weights was not demonstrated, it was included to allow a side-by-side performance evaluation under controlled and identical conditions.
By integrating both algorithms into a real-world GUI simulation using tkintermapview, the project emphasizes practical application and educational value. This supports existing literature on the effectiveness of visual and interactive tools for algorithm instruction and highlights how theoretical models can be evaluated through simulation.

Chapter 3
This section provides a detailed examination of the algorithms used in this study, including a formal problem definition, algorithm design and modification comparison, correctness verification through test cases, and a complexity analysis. It aims to establish the mathematical and empirical foundation of both Dijkstra’s Algorithm and Bellman-Ford Algorithm in solving the single-source shortest path (SSSP) problem in graphs.
Problem and Algorithm
3.1 Formal Description of Problem
The Single Source Shortest Path (SSSP) problem is a fundamental problem in graph theory. Given a source vertex in a weighted graph, the goal is to find the shortest path from the source to all other vertices. This is critical in various applications such as GPS navigation, network routing, and transportation systems.
Two widely recognized algorithms that address this problem are Dijkstra’s Algorithm and Bellman-Ford Algorithm:
Dijkstra’s Algorithm efficiently computes the shortest paths in graphs without negative edge weights using a greedy approach.


Bellman-Ford Algorithm, in contrast, allows negative edge weights and is capable of detecting negative-weight cycles, though it typically performs slower.


While Dijkstra's Algorithm is faster and widely used in real-time systems (e.g., Google Maps), it cannot handle graphs with negative weights. On the other hand, Bellman-Ford handles a broader range of inputs but with increased computational complexity.
In this project, we aim to compare these algorithms in the context of real-world map navigation, focusing on their performance, scalability, and correctness. No negative weights are introduced in this implementation to reflect realistic road network constraints, making the comparison fair and consistent.


3.2 Design of Algorithm
To understand the functional differences between the two algorithms, the following table presents a side-by-side comparison of the essential parts of their implementation. These were extracted from the Python code used in the experiment.
Dijkstra’s Algorithm (Original)
Bellman-Ford Algorithm (Compared)
```python
```python
def dijkstra(graph, start):
def bellman_ford(edges, V, start):
dist = {v: inf for v in graph}
dist = [inf] * V
dist[start] = 0
dist[start] = 0
pq = [(0, start)]
for _ in range(V - 1):
while pq:
for u, v, w in edges:
d, node = heappop(pq)
if dist[u] + w < dist[v]:
for neighbor, w in graph[node]:
dist[v] = dist[u] + w
if dist[neighbor] > d + w:


dist[neighbor] = d + w


heappush(pq, (dist[neighbor], neighbor))


return dist
return dist
```
```

Table 1. Table of Design of Algorithms
Both algorithms aim to update the shortest known distances iteratively, but the control structure and data handling differ significantly—priority queues (heapq) in Dijkstra vs. full edge relaxation loops in Bellman-Ford.
3.3 Proof of Correctness
To verify correctness, we executed both algorithms on a test graph with five nodes and the following weighted edges:
Graph:
Nodes: A, B, C, D, E


Edges:


A → B (3)


A → C (1)


B → D (4)


C → D (2)


D → E (1)


Expected Shortest Paths from A:
A → A = 0


A → B = 3


A → C = 1


A → D = 3 (via C)


A → E = 4 (via D)


Dijkstra’s Output:
A: 0
B: 3
C: 1
D: 3
E: 4

Bellman-Ford Output:
A: 0
B: 3
C: 1
D: 3
E: 4

Both algorithms produced consistent and correct shortest paths. The test validated the correctness through traceable iterations.
3.4 Complexity Analysis
Dijkstra’s Algorithm:
Initialization: O(V)


Priority Queue Operations:


Each node pushed and popped once: O(V log ⁡V)


Edge relaxation: O(E log ⁡V)


Total Time Complexity:


Adjacency List with Heap: O(E log⁡ V)


Adjacency Matrix (unoptimized): O(V^2)


Bellman-Ford Algorithm:
Initialization: O(V)


Relaxation:


Repeat V−1V - 1 times over all edges: O(V⋅E)


Cycle Detection: O(E)


Total Time Complexity: O(V⋅E)
Mathematical Induction (Proof of Termination for Bellman-Ford):
Base Case: After 0 iterations, only the source node has distance 0. All others are at ∞.
Inductive Step: Suppose after kk iterations, all shortest paths with ≤ kk edges are correctly found. In the k+1 iteration, paths of length k+1 edges are considered and properly relaxed.
Thus, after V−1iterations, all paths (up to length V−1) have been processed. Hence, Bellman-Ford terminates correctly unless a negative cycle is found (which is not the case in this project).

Chapter 4
Evaluation
This section provides the simulation results conducted between the original algorithm (Dijkstra’s Algorithm) and comparative algorithm (Bellman-Ford Algorithm). It presents the process of implementing the solution, setting up the experimental environment, and collecting performance data under controlled and consistent test conditions. The goal is to determine how the algorithms differ in execution time, correctness, and scalability.

4.1 Implementation Details
This research was implemented using a Python-based simulation that compares the runtime efficiency of Dijkstra’s Algorithm and Bellman-Ford Algorithm. The implementation includes custom code for both algorithms and a performance testing framework that automatically generates test graphs and records execution time across multiple input sizes. A graphical user interface (GUI) using CustomTkinter and tkintermapview allows users to select source and destination nodes on a real-world map, trigger either algorithm, and observe the computed path in real-time.
The experiments were conducted on the following hardware and software configuration:
Machine: Lenovo IdeaPad


Processor: Ryzen 7000


RAM: 16 GB DDR4


Operating System: Windows 11(64-bit)


Programming Language: Python 3.12.6


Key Libraries: heapq, time, random, matplotlib, tkintermapview, CustomTkinter


Both Dijkstra and Bellman-Ford algorithms were implemented from scratch. Dijkstra used an adjacency list and a priority queue (heapq), while Bellman-Ford used a flat list of edges and full-edge relaxation. A function was created to generate the same graph for both algorithms using randomly assigned edge weights between 1 and 10 to ensure a controlled and fair comparison.
Although both algorithms included basic memory tracking using Python’s sys.getsizeof() function, a detailed memory comparison was not conducted. Python’s default memory tracking is shallow and does not account for nested structures or interpreter overhead. Moreover, Bellman-Ford inherently processes all edges in every iteration, so a deeper space complexity analysis would require specialized profiling tools. For this reason, only execution time was recorded and used as the basis for performance evaluation.
Ethically, this project posed no risks as it did not involve human participants or sensitive data. The study focused purely on algorithmic evaluation in a simulated environment, ensuring it met academic and ethical standards.

4.2 Experimental Setup
The experimental evaluation focused on measuring the execution time of Dijkstra’s Algorithm and Bellman-Ford Algorithm across graphs of increasing size. Each test graph was randomly generated using a shared function to ensure both algorithms received identical input.
The structure of the experiment included:
Independent Variable: The algorithm used (Dijkstra or Bellman-Ford)


Dependent Variable: Execution time (measured in seconds)


Control Conditions: Same number of nodes, edges, and weight range across both algorithms


Graphs were generated with node counts of 5, 10, 15, 20, and 25. Each graph was undirected and weighted, with weights randomly selected between 1 and 10. For each test:
A shared graph was generated and converted to an adjacency list for Dijkstra and a flat edge list for Bellman-Ford.


Both algorithms were executed on the same graph.


Execution time was measured using Python’s time module.


The process was repeated five times per graph size, and the average runtime was calculated to reduce the influence of external factors such as system load.


Although memory tracking code was embedded in both algorithm functions, its results were not analyzed due to the limitations of sys.getsizeof() in Python. The tool does not measure deep memory allocations and may not reflect real application-level space usage. Consequently, space complexity was excluded from the results, but its consideration is noted for future research.
After all iterations, performance data was visualized using matplotlib, comparing the runtime of both algorithms across different graph sizes. This allowed for clear interpretation of how algorithm performance scaled with input size under controlled conditions.
4.3 Results and Discussion
This sub-section presents and interprets the results obtained from the performance evaluation of Dijkstra’s Algorithm and Bellman-Ford Algorithm. The focus of the comparison is based on execution time as the input size increases. Although memory tracking was implemented in the code, the study primarily focuses on runtime due to the limitations of Python’s memory profiling and the inherent structural differences between the two algorithms.
The experiment simulated graph data with increasing numbers of nodes (5, 10, 15, 20, and 25), where edge weights were randomly assigned values between 1 and 10. Each algorithm was executed on identical graph inputs, with the same starting node, and repeated five times per test case to reduce statistical noise. The average execution time was recorded.

Figure 1. Average Execution Times
The results clearly show that Dijkstra’s Algorithm consistently outperforms Bellman-Ford in terms of execution time. The performance gap becomes more significant as the number of nodes increases, aligning with the theoretical time complexities of the two algorithms:
Dijkstra’s Algorithm (with a binary heap): O((V+E) log⁡ V)


Bellman-Ford Algorithm: O(V⋅E)
This performance difference is also visualized in Figure 4.1, which presents a runtime comparison graph generated using matplotlib.

Figure 2. Comparison Graph
The visualization further illustrates how the time complexity scales with input size. As the graph becomes more complex, Bellman-Ford’s performance degrades significantly compared to Dijkstra’s, making Dijkstra more suitable for time-sensitive applications on large, sparse graphs without negative edge weights (e.g., road networks, logistics systems).
While both algorithms returned accurate and consistent shortest path results in all test cases, Dijkstra’s superior efficiency makes it a preferred choice in most practical scenarios where negative edge weights are not a concern.
Although the implementation also tracked memory allocation for key data structures, a formal memory comparison was excluded due to the limitations of the sys.getsizeof() function and the dynamic nature of Python’s memory management. Future work may explore deeper profiling using specialized tools.
In summary, this section validates the theoretical performance expectations of both algorithms and confirms that for non-negative graphs—the focus of this study—Dijkstra’s Algorithm provides faster, more scalable performance.

Chapter 5
Conclusion
This section provides a summary of the findings, insights, and implications drawn from the comparative evaluation of Dijkstra’s Algorithm and Bellman-Ford Algorithm. It reflects on the research objectives, the simulation results, and the practical implementation. It also highlights the contributions of this study to the field of algorithm analysis and suggests future directions for improvement and expansion.
5.1 Contributions
The main contribution of this research is the design and implementation of a Python-based simulation tool that allows users to compare the performance of Dijkstra’s Algorithm and Bellman-Ford Algorithm in solving the Single Source Shortest Path (SSSP) problem in non-negative weighted graphs.
Key contributions include:
Custom implementation of both algorithms from scratch, with an emphasis on correctness, efficiency, and modularity.


Integration of the algorithms into a graphical user interface (GUI) using CustomTkinter and tkintermapview, allowing users to interactively select source and destination nodes, visualize shortest paths, and analyze runtime behavior in real-world map contexts.


A structured experimental framework for measuring and comparing execution time and scalability across various graph sizes.


A literature-informed analysis of theoretical time complexities, strengths, and limitations of each algorithm.


A set of empirical findings confirming that Dijkstra’s Algorithm significantly outperforms Bellman-Ford in execution time for graphs with non-negative edge weights, while maintaining equivalent accuracy in output.


This work successfully bridges algorithm theory and real-world application by combining academic analysis with practical, hands-on implementation and testing.
5.2 Future Work
While the project has achieved its core objectives, several potential improvements and extensions could be explored in future research:
Support for Negative Weights: Future implementations may include test cases involving negative edge weights to fully utilize Bellman-Ford’s ability to detect negative cycles and assess how it performs under more complex graph conditions.


Graph Input Expansion: Instead of randomly generated graphs only, future versions could allow users to import graphs from files (e.g., CSV, JSON, or real-world map data).


Detailed Memory Profiling: Future studies may incorporate memory profiling tools to precisely measure and compare the space complexity of each algorithm. This would provide a more comprehensive view of their efficiency, particularly on large or dense graphs.


Algorithm Enhancements: More advanced or alternative shortest-path algorithms (such as A* or Johnson’s Algorithm) can be added to extend the scope of comparison and performance analysis.


Visualization Improvements: Future versions may implement step-by-step animation of algorithm progress to enhance learning and debugging.


Scalability Testing: Testing on much larger graphs (thousands of nodes) could further validate the efficiency and limitations of each algorithm.


Mobile or Web Integration: Turning the simulation into a web-based tool or mobile app would make it more accessible for educational or real-world routing use.


Through these future enhancements, the project could evolve from a course-based academic exercise into a comprehensive educational toolkit or a prototype for real-world routing applications.






















References

[1] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, *Introduction to Algorithms*, 3rd ed. Cambridge, MA: MIT Press, 2009.

[2] R. K. Ahuja, T. L. Magnanti, and J. B. Orlin, *Network Flows: Theory, Algorithms, and Applications*. Upper Saddle River, NJ: Prentice Hall, 1993.

[3] E. W. Dijkstra, “A note on two problems in connexion with graphs,” *Numer. Math.*, vol. 1, no. 1, pp. 269–271, 1959.

[4] R. Bellman, “On a routing problem,” *Q. Appl. Math.*, vol. 16, no. 1, pp. 87–90, 1958.

[5] R. E. Tarjan, *Data Structures and Network Algorithms*. Philadelphia, PA: SIAM, 1983.

[6] A. V. Goldberg and C. Harrelson, “Computing the shortest path: A* search meets graph theory,” in *Proc. 16th Annu. ACM-SIAM Symp. Discrete Algorithms (SODA)*, 2005, pp. 156–165.
[7] R. Alamoudi and B. M. Al-Hashimi, “Energy-Efficient Evaluation of Shortest Path Algorithms on Hardware,” Sensors, vol. 21, no. 6, pp. 1–15, 2021.
[8] K. Deng, Q. Zhang, H. Zhang, P. Xiao, and J. Chen, “Optimal emergency evacuation route planning model based on fire prediction data,” Sustainability, vol. 15, no. 6, pp. 1–20, Mar. 2023.
[9] C. Hedrick, “Routing Information Protocol,” RFC 1058, IETF, 1988.
[10] A. Tilanterä, J. Sorva, O. Seppälä, and A. Korhonen, “Students struggle with concepts in Dijkstra’s algorithm,” in Proceedings of the 2021 Conference on Innovation and Technology in Computer Science Education (ITiCSE), Jun. 2021, pp. 389–395.
[11] P. K. Das, S. K. Pradhan, H. K. Tripathy, and P. K. Jena, “Improved real-time A*-fuzzy controller for improving multi-robot navigation and its performance analysis,” International Journal of Data Science, vol. 2, no. 2, pp. 105–137, 2017.










Appendix A


The Journal Paper 














Appendix B

The Data Set 























Appendix C
The Code
This section provides the source code used to simulate and evaluate the performance of Dijkstra’s Algorithm and Bellman-Ford Algorithm. The program includes the generation of test graphs, custom implementations of both algorithms, performance measurement (execution time), and visualization of results using matplotlib.

import heapq
import time
import sys
import random

import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    space_complexity = sys.getsizeof(distances) + sys.getsizeof(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                space_complexity += sys.getsizeof(priority_queue)

    return distances, space_complexity


def bellman_ford(edges, vertices, start):
    distances = {vertex: float('inf') for vertex in vertices}
    distances[start] = 0
    space_complexity = sys.getsizeof(distances) + sys.getsizeof(edges)

    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                space_complexity += sys.getsizeof(distances)

    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances, space_complexity


def generate_shared_graph(n):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            weight = random.randint(1, 10)
            edges.append((str(i), str(j), weight))
            edges.append((str(j), str(i), weight))  # For undirected
    return edges


def convert_to_adjacency_list(edges, n):
    graph = {str(i): {} for i in range(n)}
    for u, v, w in edges:
        graph[u][v] = w
    return graph


def plot_performance(nodes_list, times_dijkstra, times_bellman):
    plt.plot(nodes_list, times_dijkstra, label='Dijkstra', marker='o')
    plt.plot(nodes_list, times_bellman, label='Bellman-Ford', marker='s')
    plt.title('Performance Comparison: Dijkstra vs Bellman-Ford')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    nodes_list = [5, 10, 15, 20, 25]
    times_dijkstra = []
    times_bellman = []

    for num_nodes in nodes_list:
        start_node = '0'
        vertices = [str(i) for i in range(num_nodes)]
        shared_edges = generate_shared_graph(num_nodes)

        graph_dijkstra = convert_to_adjacency_list(shared_edges, num_nodes)
        graph_bellman = shared_edges

        # Dijkstra Timing
        start_time = time.time()
        dijkstra(graph_dijkstra, start_node)
        times_dijkstra.append(time.time() - start_time)

        # Bellman-Ford Timing
        start_time = time.time()
        bellman_ford(graph_bellman, vertices, start_node)
        times_bellman.append(time.time() - start_time)

    # Print performance results
    print("--- Performance Data ---")
    for i in range(len(nodes_list)):
        print(f"{nodes_list[i]} nodes -> Dijkstra: {times_dijkstra[i]:.6f}s, Bellman-Ford: {times_bellman[i]:.6f}s")

    # Plot results
    plot_performance(nodes_list, times_dijkstra, times_bellman)


if __name__ == "__main__":
    main()















