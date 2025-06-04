# Graph Theory

1. Social Networking:

        Social networking can be analyzed using graph theory by representing individuals as nodes and relationships as edges.

        Example:

        Social networks (like Facebook, Twitter, LinkedIn, etc.) can be modeled as graphs:

            📌 Graph Structure

            Nodes (Vertices): People or users.
            Edges (Links): Connections like friendships, followers, messages, etc.
            
2.  Graph Theory:

        Graph Theory is the study of relationships between different objects.

        Graph:
            A graph is a collection of various vertexes also known as nodes, and these nodes are connected with each other via edges. 

            Nodes (also called vertices) — represent objects (e.g., people, places, computers).
            Edges (also called links) — represent relationships or connections between those objects.

    Basic Terms of a graph:

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/GraphTheory.png">

3. Degree in Graph Theory:

        Degree of a Node: The degree of a node is the number of edges connected to it.

        1. In a Undirected Graph:

                        A
                       / \
                      B - C

            Node A → degree = 2 (connected to B and C)
            Node B → degree = 2 (connected to A and C)
            Node C → degree = 2 (connected to A and B)

        2. In a Directed Graph:

            In-degree: Number of edges coming into a node
            Out-degree: Number of edges going out from a node

                    A → B ← C

                A: out-degree = 1, in-degree = 0
                B: out-degree = 0, in-degree = 2
                C: out-degree = 1, in-degree = 0

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Examplesfordirectedgraph.png">

 4. Types of graphs:

    1. Undirected Graph:

        Edges have no direction — the relationship goes both ways.
    
        Example: Facebook Friends
    
        If Alice is friends with Bob, then Bob is friends with Alice.
        
                Alice — Bob
            (One line, no arrow) 

    2. Directed Graph:

        Edges have a direction — like one-way streets.
    
        Example: Twitter Followers
        
        If Alice follows Bob, Bob doesn’t have to follow back.

                Alice → Bob
            (Arrow shows direction)
   
    3. Weighted Graph:

        Edges have weights or values — like distance, cost, or strength.
    
        Example: Google Maps or Flight Routes
    
        Road from City A to City B is 100 km
        Flight from A → B costs $300

            A —(100km)— B

    4. Unweighted Graph
        
        All edges are equal — no weights or values.

        Example: Basic Relationship Graph
    
        Just showing who is connected to whom — no distances or strength

            A — B — C
    
    5. Cyclic Graph
    
        The graph contains cycles — you can start at a node, follow a path, and come back to the same node.
        
        Example: Round trip routes , feedback loops

            A → B → C → A
            (Back to starting point)

    6.  Acyclic Graph
        
         A graph with no cycles — you can’t return to the same node by following the direction of edges.
        
        Example: Task Scheduling / To-Do Lists

            (Each task depends on the previous one)
        
        Special Case: DAG (Directed Acyclic Graph)
        
        Used in:
            Project planning 
            Git commit history

            Start → Task 1 → Task 2 → Task 3
    
# Centrality:   
    
    In graph theory indicators of centrality assign numbers or rankings to nodes within a graph corresponding to their network position.

    Consider a realtime example: 

    Real time example:

    let us consider an Amazon shopping page (E-Commerce Directed Graph Example: Customer Journey)

    [Homepage] → [Search Page] → [Product Page] → [Add to Cart] → [Checkout] → [Payment] → [Thank You]
      ↑                               ↓               ↓
      └───────────────────────────────┘         [Back to Product]

    
      Let’s say we analyze real user data and see:

        1000 users visit Homepage
        900 users visit Searchpage
        800 go to Product Page
        400 go to Add to Cart
        200 reach Checkout
        180 make Payment
        160 reach Thank You Page
    
    The directed graph clearly shows drop-off rates and helps in optimizing the funnel by improving design or marketing at weak spots.

        Node (Vertex)	Each webpage or step
        Directed Edge	User clicking/transitioning
        Path	Complete journey to purchase
        Cycle	User going back to Product Page
        In-degree	Popularity of a page
        Out-degree	Number of options/paths from page
        Betweenness	Pages that serve as key transition

1. Degree Centrality:

        Measures how many direct links a node has.

        In our case:

        Homepage has high out-degree (links to Search Page , Product Page)
        Product Page has in-degree from Search Page, Cart Page, and out-degree to Cart Page and Homepage.
        
        💡 Meaning in e-commerce:

        Pages with high degree are popular or busy pages.
        
        Use case: You may want to optimize Product Pages with better design, faster load time, and promotions since they are highly trafficked.

2. Betweenness Centrality:

        Measures how often a node lies on the shortest path between others.

        In our case:

        Product Page (P) lies between Search Page and Cart Page.
        Cart (C) lies between Product Page and Checkout.
        Checkout (O) connects Cart to Payment.
        
        💡 Meaning in e-commerce:

        Pages with high betweenness are critical connectors.
        If they fail, the user flow breaks.
        
        Use case: Make sure pages like Cart and Product Page are robust (no crashes, fast).

3. Closeness Centrality
        
        Measures how close a node is to all other nodes (via shortest paths).

        In our case:

        Cart Page can quickly reach Checkout, Product Page, and back.
        Product Page can reach Checkout in 2 steps, Payment in 3.

        💡 Meaning in e-commerce:

        Pages with high closeness are efficient at navigating to other parts.
    
        Use case: Make sure high-closeness pages have strong CTAs (call-to-action) since users land there often and move on quickly.

4. Eigenvector Centrality

        Measures how important a node is by being linked to other important nodes.

        In our case:

        Product Page is linked to by Search Page and Cart Page.
        Both Search Page and Homepage are high-value pages.
        So Product page gets high eigenvector score.
    
        💡 Meaning in e-commerce:

        High eigenvector centrality = page is influential in the network.

        Use case: Invest in analytics & A/B testing on Product Pages — small changes have big impact because these pages drive user behavior.

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Centralitybasic.png">

# Graph Database:

    A graph database is a non-relational database designed to store data in nodes (entities) and edges (relationships) — like a network.

    Types of Data:

    Structured Data:
        organized in rows and columns like in tables	
        Relational databases (e.g., SQL)
    
    Semi-structured: 
        Doesn’t fit strict tables, but has tags or markers	
        JSON, XML, CSV
    
    Unstructured:
        No predefined format	
        Text files, emails, images, videos

    Graph Database:(Fraud Detection)

    ✔️ It works well with:
    Data Type	How Graph Databases Handle It
    Structured	Can import data from SQL databases into graphs
    Semi-structured	Naturally maps to nodes and edges (e.g., JSON → nodes/links)
    Unstructured	Can store metadata or tags as graph properties

    Example:

    Customer	Node                      Customer
    Product	Node                         Product
    Purchase	Edge              Customer → buys → Product
    Review	Edge                  Customer → reviews → Product
    Recommendation	Edge       Product → also_bought_with → Product  