<!-----
Conversion notes:
* Docs to Markdown version 1.0β34
* Wed Oct 18 2023 16:29:52 GMT-0700 (PDT)
* Source doc: W6 Coachable Practice HW 2.0
----->

# W6 Coachable Practice HW


# Graphs


## Free Response Questions


### General

Figure 1:

6 - 2 

 |   |

 5 - 1 - 4 

     |

     3



1. _What are the differences between graphs and trees?_

    A graph is a set of vertices and edges. Some of the vertices have relationships with other vertices through edges. There is at least one vertex and one edge.


    A tree is a connected (every node connects to another node) and acyclic graph with a root node. Every node has one parent. Binary trees specifically max out at 2 children nodes.


    Edges in graphs can be one direction or both ways. Edges in tree are one way to the child.

2. _For the graph (Figure 1), write the Adjacency Matrix and Adjacency List representations._

Adjacency matrix:


    	1	2	3	4	5	6


    1	0	1	1	1	1	0


    2	1	0	0	0	0	1


    3	1	0	0	0	0	0


    4	1	0	0	0	0	0


    5	1	0	0	0	0	1


    6	0	1	0	0	1	0

Adjacency list:

1: [2, 3, 4, 5]

2: [1, 6]

3: [1]

4: [1]

5: [1, 6]

6: [2, 5]



3. _What does it mean for a graph to be directed?_

    Edges are one direction from a vertex to another vertex

4. _What does it mean for a graph to have a cycle?_

    A path that starts and ends at the same vertex

5. _How can you detect a cycle in a graph?_

    Do DFS. Track the current recursion stack. Add a vertex at the beginning of the recursive function to the current stack. If a neighbor of the current vertex has been visited and is in the current recursion stack, then there is a cycle. Otherwise once gone through all the neighbors, remove the current vertex from the current recursion stack.

6. _If you have a graph with <code>N</code> vertices, what is the maximum number of edges it could have?</em>

    (N * (N - 1)) / 2 for undirected graph


    N * (N - 1) for a directed graph

7. _Recall that a binary tree is an example of a graph. If a binary tree has N nodes, what is the maximum number of edges it can have?_

    N - 1. Every node can have one edge except the first has none



### Graph Traversals

_Assume the adjacency lists are in sorted order. For example, follow the edge <code>O → B</code> before <code>O → E</code>​. Similarly, follow <code>3 → 2</code> before <code>3 → 7</code></em>


```
Figure 2
Adj List (16 edges):
B: [E]
E: [S, W]
I: [W, Y]
M: [I]
O: [B, E, Y]
P: []
S: [B, E, I, M, O, P]
W: [M]
Y: []

```



1. _Give the postorder of the graph when visited by DFS. Start from <code>O</code>.</em>

    First run:


    Stack: [O, B, E, S, I, W, M]


    M -> 


    Stack: [O, B, E, S, I, W]


    M -> W


    Stack: [O, B, E, S, I, Y]


    M -> W -> Y


    Stack: [O, B, E, S, I]


    M -> W -> Y -> I


    Stack: [O, B, E, S]


    M -> W -> Y -> I -> P -> S


    Stack: [O, B, E]


    M -> W -> Y -> I -> P -> S -> E -> B -> O

2. _Give the preorder of the graph when visited by DFS. Start from <code>O</code>.</em>

    O -> B -> E -> S -> I -> W -> M -> Y -> P

3. _Give the BFS traversal of the graph. Start from <code>O</code>.</em>

    O ->


    B -> E -> Y -> 


    S -> W -> 


    I -> M -> P

4. _Is there a topological order starting from <code>O</code>? If there is not, why not? If there is one, write the topological order.</em>

    No


    Terminal nodes: P, Y


    Eventual safe nodes: None


    Lots of cycles like: O, B, E, S and M, I, W


    **Figure 3**


    Adj List (16 edges):


    1: []


    2: [1, 7]


    3: [2, 4, 7, 8]


    4: [5, 9]


    5: []


    6: [1]


    7: [1, 6, 8]


    8: []


    9: [3, 5, 8]


    10: [9]

1. _Give the postorder of the graph when visited by DFS. Start from node <code>10</code>.</em>

    Stack: [10, 9, 3, 2, 1]


    1 -> 


    Stack: [10, 9, 3, 2, 7, 6]


    1 -> 6


    Stack: [10, 9, 3, 2, 7, 8]


    1 -> 6 -> 8


    Stack: [10, 9, 3, 2, 7]


    1 -> 6 -> 8 -> 7


    Stack: [10, 9, 3, 2]


    1 -> 6 -> 8 -> 7 -> 2


    Stack: [10, 9, 3, 4, 5]


    **1 -> 6 -> 8 -> 7 -> 2 -> 5 -> 4 -> 3 -> 9 -> 10**

2. _Give the preorder of the graph when visited by DFS. Start from <code>1O</code>.</em>

    10 -> 9 -> 3 -> 2 -> 1


    -> 7 -> 6


    -> 8


    -> 4 -> 5


    **10 -> 9 -> 3 -> 2 -> 1 -> 7 -> 6 -> 8 -> 4 -> 5**

3. _Give the level order of the graph. Start from <code>10</code>.</em>

    10


    -> 9


    -> 3 -> 5 -> 8


    -> 2 -> 4 -> 7


    -> 1


    -> 6


    **10 -> 9 -> 3 -> 5 -> 8 -> 2 -> 4 -> 7 -> 1 -> 6**

4. _Is there a topological order starting from <code>10</code>? If there is not, why not? If there is one, write the topological order.</em>

    No


    Terminal nodes: 1, 5, 8


    Eventual safe nodes: 2, 7, 6


    3, 4, 9 form a cycle. 10 only goes to 9



## Inorder for Graphs

_We have a preorder, inorder, and postorder for binary trees. However, an inorder traversal doesn't really make sense for graphs because it's unclear where you would process the node among multiple child nodes. For example, if you had a parent node <code>X</code> with children <code>A,B,C</code> , it's ambiguous which child you would process ​<code>X</code> after.</em>

_For this reason, graph DFS is usually postorder or preorder._

_For this exercise, we'll use **alphabetical ordering** to create our in-order traversal - the parent and children will be processed in alphabetical order. In the above DFS call on <code>X</code> would look like</em>

_dfs(X)_

_    dfs(A)_

_    dfs(B)_

_    dfs(C)_

_    process(x)_

_If <code>B</code> were the parent and <code>A,C,X</code> were the children, then the call would look like this.</em>

_dfs(B)_

_    dfs(A)_

_    process(B)_

_    dfs(C)_

_    dfs(X)_


### Determine the alphabetical in-order traversal for



* _The graph in figure 2 starting from** **​<code>O</code></em>


```
Adj List (16 edges):
B: [E]
E: [S, W]
I: [W, Y]
M: [I]
O: [B, E, Y]
P: []
S: [B, E, I, M, O, P]
W: [M]
Y: []

dfs(O)
	dfs(B)
	dfs(E)
	process(O)
	dfs(Y)

dfs(B)
	process(B)
	dfs(E)

dfs(E)
	process(E)
	dfs(S)
	dfs(W)

dfs(S)
	dfs(B)
dfs(E)
dfs(I)
dfs(M)
dfs(O)
dfs(P)
process(S)

dfs(I)
	process(I)
	dfs(W)
	dfs(Y)

dfs(W)
	dfs(M)
	process(W)

dfs(M)
	dfs(I)
	process(M)

B -> E -> I -> M -> W -> 

dfs(Y)
	process(Y)

dfs(P)
	process(P)

Final ordering:
B -> E -> I -> M -> W -> Y -> O -> P -> S
Explanation:
I started with dfs(O) which led to processing B, then E.
In dfs(E), S was next and B and E were done.
So dfs(I) is next. Process I and then W is next.
W has M go first which has dfs(I) first which is already done. Then dfs(W) with dfs(M) done has W processed.
Back to dfs(I), dfs(Y) is next. Nothing there except process Y.
Then we are back to dfs(S) since dfs(I) is done too. For dfs(S) the first couple of dfs are done so we are at dfs(O).
Everything is done for dfs(O)except to process O, then back to dfs(S).
dfs(P) is next which is just P. Then finally process S.

```



* _The graph in figure 3 starting from <code>10</code></em>

    Adj List (16 edges):


    1: []


    2: [1, 7]


    3: [2, 4, 7, 8]


    4: [5, 9]


    5: []


    6: [1]


    7: [1, 6, 8]


    8: []


    9: [3, 5, 8]


    10: [9]



```
dfs(10)
	dfs(9)
	process(10)

dfs(9)
	dfs(3)
	dfs(5)
	dfs(8)
	process(9)

dfs(3)
	dfs(2)
	process(3)
	dfs(4)
	dfs(7)
	dfs(8)

dfs(2)
	dfs(1)
	process(2)
	dfs(7)

dfs(1)
	process(1)

–
So far:
1 -> 2 -> 
Continuing dfs(2) after processing which is dfs(7)
–
dfs(7)
	dfs(1)
	dfs(6)
	process(7)
	dfs(8)

dfs(6)
	dfs(1)
	process(6)

dfs(8)
	process(8)

–
dfs(7) had dfs(1) done so dfs(6) which processed 6. Then dfs(7) processed 7 and dfs(8) is just processing 8. So far:
1 -> 2 -> 6 -> 7 -> 8
–

–
Back to dfs(3) where next up is processing 3
1 -> 2 -> 6 -> 7 -> 8 -> 3
–

Then dfs(3) has dfs(4) next:
dfs(4)
	process(4)
	dfs(5)
	dfs(9)

dfs(5)
	process(5)

–
dfs(4) is processed and dfs(5) is next which is just processing 5.
1 -> 2 -> 6 -> 7 -> 8 -> 3 -> 4 -> 5
–

Next for dfs(4) is dfs(9) with 3, 5, 8 already processed.

Final ordering:
1 -> 2 -> 6 -> 7 -> 8 -> 3 -> 4 -> 5 -> 9 -> 10
```



### Shortest Path



1. _Supposes we have a graph <code>G</code> with vertices <code>s,t</code>​. How can you find the length of the shortest path from <code>s→t</code>​ in each of the following scenarios?</em>
1. <em>Every edge in <code>G</code> has weight 1.</em>

    BFS. It is single source shortest path.


    Runtime: O(V + E)


    Space: O(V)

2. _Every edge in ​<code>G</code> has uniform edge weight <code>e</code>​ where <code>e > 0</code>?</em>

    BFS. Same as (1). The only difference would be multiplying the number of edges `e` by the uniform weight `k`. For example if edge weight k = 5. The shortest path is the same as (1) but 5x.

3. _Edges in <code>G</code> have nonuniform but strictly positive edge weights?</em>

Dijkstra. Works with DAGs. Directed Acyclic Graphs. Dijkstra’s algorithm is greedy (verify what this is TODO). Like BFS, It is single source shortest path.

Runtime is: O(|E| + |V|log|V|)

Space: O(V)



4. _Edges in <code>G</code> have nonuniform negative/positive edge weights?</em>

Bellman-Ford algorithm. Works with DAGs with negative edge weights. Also single source shortest path. Algo is not greedy.

Relaxing is |V|-1. Vertexes - 1. Bellman-Ford does not assume a shorter path will not appear after a longer one. The relaxing handles that. If no changes happen for a relaxation iteration, doing another relaxation will also not change anything.

The reasoning is because with negative edges, paths that at first don’t seem as if they will become smaller with negative edges included, end up giving wrong answer with Dijisktra’s algo.

Runtime: O(|V|*|E|)

Space: O(|V|)



2. _How do any of these change if we want to return the path itself instead of the shortest path length?_

    For BFS, keep track of the predecessor of each node. Once the target node is reached, you can backtrack through the predecessors to construct the shortest path.


    For Dijkstra, maintain a predecessor array. As you relax the edges and update the distances, you also update the predecessor of each node. At the end, use the predecessor array to construct the shortest path from the source to any other node.


    For Bellman-Ford, maintain a predecessor array. When you relax the edges and update the distances, you also update the predecessor of each node.



### Valid Orderings



1. _If I have a directed acyclic graph (DAG) where <code>c1 -> c2</code> means that I need to take course <code>c1</code>​ before <code>c2</code>​</em>
1. <em>What algorithm can I use to sequence my coursework without skipping courses?</em>

    Topological sort

2. _How is this algorithm different from a standard BFS/DFS?_

    Topological sort looks for any vertices that have 0 outgoing edges. It queues these.


    Looping through the queue, the first vertex is taken out and added to the final result. This is the current vertex.


    Look through all the incoming vertices for the current vertex. Subtract each incoming vertex's outgoing edge count by 1. If the outgoing edge count of this vertex is now 0, append this to the queue too.


    - Topological sort is only for directed acyclic graphs (DAGs).


    - BFS and DFS are for traversing or searching a graph, while topological sort is for ordering the vertices of a DAG in a linear order.


    - BFS uses a queue data structure, DFS uses a stack. Topological sort can use a queue or stack depending on implementation. For the one learned in Teachable, it uses a queue as well as an incoming 2d array, and an outgoing array representing each vertex.

3. _What would happen if the directed graph was cyclic and I tried using the same algorithm?_

    The topological sort would do a partial output of the vertices that aren't part of the cycle. This isn't a valid topological ordering for the entire graph.



## Intermediate Processing BFS/DFS

Assume you have a digraph `G`​ with vertices represented with lowercase letters e.g. ​`s,v,w`. A counter-example here is a specific graph where the statement is false.

Hint: Once you have established any of the statements as true or false, you may use them to prove further ones. I.e. if you think (2) is true, you can use it to help you prove (1).


### **DFS.** For each of the following statements, indicate whether it is true or false in the context of a depth-first search on a digraph starting from vertex `s` starting with `dfs(G,s)` If it is false, provide a counterexample. If it is true, explain why.



1. _At the moment when <code>dfs(G, v)</code> is called, there must be a directed path from <code>s</code>​ to <code>v</code> in <code>G</code>.</em>

    True. s at some point is able to have edges connect with v. DFS only visits vertices that are reachable from the starting vertex.

2. _At the moment when <code>dfs(G, v)</code> is called, there must be a directed path from s to v in the function-call stack.</em>

    True. You can start at s and follow the edges to reach v with the vertices along the path being in the stack. The function-call stack keeps track of the vertices that the algo is currently exploring or has yet to finish exploring.

3. _At the moment when <code>dfs(G, v)</code> is called, if <code>G</code> includes an edge <code>v → w</code> for which <code>w</code> has been previously marked, then <code>G</code> must contain a directed cycle containing <code>v</code>.</em>

    False. If the edges are: [[s,w], [s, v], [v, w]], then the edges are: s -> w, s -> v, v -> w. w is a terminal node. It would be true if it is undirected or if w points to s.

4. _At the moment when <code>dfs(G, v)</code> is called, if <code>G</code> includes an edge <code>v → w</code> for which <code>w</code> is currently a vertex on the function-call stack, then <code>G</code> must contain a directed cycle containing <code>v</code>.</em>

    True. If w is on the function-call stack, it means that there is a path from w to v (since we're currently exploring v). So if there's an edge from v to w, then there is indeed a cycle.



### **BFS.** For each of the following statements, indicate whether it is true or false in the context of a breadth-first search on a digraph starting from vertex `s`. If it is false, provide a counterexample. If it is true, explain why.



1. _At the moment when <code>v</code> is removed from the queue during BFS, there must be a directed path from <code>s</code> to ​<code>v</code> in ​<code>G</code>.</em>

    True. BFS is level ordering so all the [unseen] neighbors of each current vertex are added to the queue. In order for v to be in the queue, it would have had to have been a neighbor of s or a neighbor of a vertex on a different level that originally came from s.

2. _At the moment when v is removed from the queue during BFS, there must be a directed path from s​ to v in the queue._

    False. s would have been de-queued already at the beginning before its neighbors were added and then any other further levels.


    The queue in BFS doesn't necessarily represent a path from the starting vertex to the current vertex. It's just a collection of vertices that are waiting to be visited.

3. _At the moment when v is removed from the queue during BFS, if G includes an edge v → w for which w has been previously marked, then G must contain a directed cycle containing v._

      False. The instructions say we start with bfs(G, s). s could have both w and v as directed edge neighbors and gone to w first. When v comes up, there can be an edge from v to w without a cycle. Like: [[(s, w), (s, v), (v, w)]


    The presence of an edge from v to a previously marked vertex w doesn't necessarily imply a cycle

4. _At the moment when v is removed from the queue during BFS, if G includes an edge v → w for which w is currently a vertex in the queue, then G must contain a directed cycle containing v._

False. Same example as before with [[(s, w), (s, v), (v, w)], if s points to both v and w, then both would be added to the queue. v could get de-queued before w. So the data could be:

Current node: v

Visited: s

Queue: w


## (Optional Section) MSTs



1. _What is a minimum spanning tree?_

    The smallest amt of weighted edges that connects all the vertices of a graph

2. _How do I generate an MST for a graph with edge weights? Explain the algorithm in a few sentences instead of giving just the algorithm name._

    Prim’s algorithm


    Step 1: Determine an arbitrary starting vertex of the MST.


    Step 2: Repeats steps 3 and 4 while there are fringe vertices (fringe vertices--those not in the tree, but adjacent to some vertex that is)


    Step 3: Find edges connecting any tree vertex with the fringe vertices (ignore visited)


    Step 4: Find the minimum among these edges and add that 1 chosen edge to the MST. Continue from this vertex.

3. _If the graph is not connected, can I still create an MST? Why or why not? What about a Minimum Spanning Forest_

    No. An MST requires the graph to be connected. However a MSF is a collection of unconnected MSTs so that works.



# Heaps


### Free Response Questions



1. _What underlying data structure(s) can a heap use?_

    An array


    - An array allows us to use the index to quickly access, insert, and delete nodes.


    - The heap is a complete binary tree so there are no gaps in the array.


    - The mathematical relationship between parent and child nodes (parent at index k, left child at 2k, right child at 2k+1) work well

2. _What is the difference between a min and a max heap?_

    A min-heap is where the parent is smaller than or equal to the child. While max heap as said before is where the parent is larger or equal to children.


    When inserting or deleting nodes, min-heaps will move smaller elements upwards (or downwards when deleting), while max-heaps will do the opposite.

3. _What is the runtime of pushing an element into a heap?_

    O(log n)

4. _What is the runtime of popping an element out of a heap?_

    O(log n)

5. _We can store integers in a heap. What about an arbitrary object? Which ones can we keep, and which ones can’t we?_

    We can store anything that can be compared

6. _If we wanted to store some of those objects we can’t keep, what concept do we need to add to those objects?_

    Three ways:

1. 

Add comparator functions like __lt__, __gt__.



2. 

We can wrap each element in a tuple then add that to our heap. What we do is make the first element of the tuple the variable that we want to compare. See the code snippet below for how we use student_id.


```
        students_heap_tuple = []
        heapq.heappush(students, (amy.student_id, amy))
        heapq.heappush(students, (bob.student_id, bob))
        heapq.heappush(students, (carl.student_id, carl))
        heapq.heappush(students, (sam.student_id, sam))

        # We print the student names in order of student_id.
        while students_heap_tuple:
        	print(heapq.heappop(students_heap_tuple)[1].student_name)

```



3. 

Using a priority queue (MaxPQ or MinPQ) where each object is associated with a priority.


```
        import MaxPQ
        students_heap = MaxPQ()
        students_heap.heap_push(amy)
        students_heap.heap_push(bob)
        while students_heap:
            print(students_heap.heap_pop().student_name)
```


Now if you try to actually run this code, you'll notice that MaxPQ doesn't exist and that's okay! When interviewing and you need to use something like a heap, what you should do is ask your interviewer, \
"Is it alright if I import a MaxPriorityQueue class that knows to use the student_id as the custom comparator?"



7. _If I wanted to find the K smallest elements in a stream, would I use a min or a max heap of size K? Why?_

    Max heap. Keep popping until there are K elements left.


    Once K elements have been added to the max heap, any further elements can be compared to the max/root element. If it's smaller than the max element, remove the max to insert the next one. Max heap allows the max element (Kth smallest) to be easily accessible.

8. _What if I wanted to find the <code>K</code> most significant elements in a stream? Why?</em>

    Min heap. Once K elements are in the min heap, each element that tries to be added can be compared to the smallest/root element. If it’s larger, pop out the min/root element to insert the larger element.

9. _If I have a collection of N elements, and I insert each of them into a min heap, and then <code>pop</code>​ + <code>print</code> each element from the heap. What did I just do?</em>

    You would pop and print the smallest to the largest elements. Like: 3, 7, 10

10. _What if I inserted each of them into a max heap and did the same thing?_

    It would print largest to smallest. Like: 10, 7, 3

11. _Suppose I insert the following sequence of numbers into a min heap: 5, 7, 9, 2, 4._
1. _What does the min heap look like?_

[, 5]

[, 5, 7]

[, 5, 7, 9]

At this point 5 is the root, 7 and 9 are children

[, 2, 5, 7, 9]

At this point, 2 is root. 5 and 7 are children. 9 is a child of 5.

**Final: [, 2, 4, 5, 7, 9]**

4 and 5 are children of 2. 7 and 9 are children of 4.



2. _Now suppose I pop twice. What does the heap look like now?_

First pop of 2:

[, 4, 5, 7, 9]

4 is root. 5 and 7 are children. 9 is a child of 5.

Second pop of 4:

**[, 5, 7, 9]**

5 is root. 7 and 9 are children.



3. _Now suppose I insert 3, 9, 12. What does the heap look like now?_

    [, 3, 5, 7, 9]


    3 is root. 5 and 7 are children. 9 is child of 5.


    [, 3, 5, 7, 9, 9]


    3 is root. 5 and 7 are children. Both 9s are children of 5.


    **[, 3, 5, 7, 9, 9, 12]**


    3 is root. 5 and 7 are children. Both 9s are children of 5. 12 is a child of 7.



### True or False

Determine if the statements are true or false. If false, provide a counter-example. If true, explain why.



1. _Let <code>a[]</code> be a max-oriented binary heap that contains the <code>N</code> distinct integers <code>1, 2, . . . , N</code> in <code>a[1]</code> through <code>a[N]</code>. Then, key <code>N</code> must be in <code>a[1]</code>; key <code>N − 1</code> must be in either <code>a[2]</code> or <code>a[3]</code>; and key <code>N − 2</code> must be in either <code>a[2]</code> or <code>a[3]</code>​.</em>

    True. As the 3 largest elements in a max heap, the 3 largest elements would be at the top with the largest as root and the next 2 as its children.

2. _The order of growth of the total number of compares to insert <code>N</code> distinct keys in descending order into an initially empty max-oriented binary heap is <code>N</code>.</em>

    True. In a max heap, when we insert elements in descending order, each new element will be the smallest and will not need to "bubble up". However, it still needs to be compared with its parent to check if the heap property is maintained. So, for each insertion, there is at least one comparison, leading to N comparisons for N insertions.

3. _A 3-heap is an array representation (using 1-based indexing) of a complete 3-way tree, where the key in each node is greater than (or equal to) its children’s keys. In the worst case, the number of compares to insert a key in a 3-heap containing N keys is <code>∼ 1 log3 N.</code></em>

    True because for a binary heap, it is log2 N. For a 3 heap, it will analogously be log3 N. The number of comparisons is proportional to the height of the 3-heap, log3 N. A newly inserted key might have to bubble up from the bottom of the heap to its correct position, which would require traversing the height of the heap.



### Number of Comparisons



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")




1. _If we insert a new element <code>y</code> into the heap. How many positions could it end up in?</em>

    5 positions. Any of the following spots: child of 22, 22, 32, 35, 38. So root, root.right, root.right.right, root.right.right.right, or root.right.right.right.left.


    _Coachable-AI keeps saying it can end up anywhere, but I don’t think that’s right. The questioning is at the end of the “W6 Binary Heaps (almost all of it)” thread in my Coachable-AI_

2. _See the binary heap in Figure A. Supposed the last operation was <code>insert(x)</code>. How many values could it possibly have been? Hint: Try to identify which values specifically would be possible.</em>

    Any of the parent or grand parents of 19. So 19, 26, 32, 35, 38 (root).

3. _Suppose you delete the maximum key from the binary heap in figure A. How many keys are involved in one or more comparisons?_

When you delete the maximum key from a binary heap, you typically replace it with the last key in the heap, and then "bubble down" that key until the heap property is restored. This involves comparing the key with its children, swapping it with the larger child if necessary

After swapping with the root, the last key, 19 would swap with 37 (the greater child of the root), then 36. Now 19 is the parent of 14 and 17.

So 4 keys are involved: 38, 19, 37, 36
