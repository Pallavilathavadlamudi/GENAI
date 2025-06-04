# SET THEORY

PROBLEM STATEMENT:
To analyze and predict the likelihood of customers liking, purchasing, and responding to a new product and its related variants?

1. SET THEORY:

        Set theory is a branch of mathematical logic that studies collections of objects, called sets. 
        A set is simply a group of distinct elements considered as a whole. 
        Sets are usually denoted using curly braces, 
        
        e.g.,

        {apple, banana, orange}

# Basic Terms

    Set: 
    A collection of distinct elements, e.g., A = {1, 2, 3}
    
    Element: 
    An object in a set. For example, 1 is an element of set A
    
    Subset: 
    A set whose elements are all contained in another set. If B = {1, 2}, then B is a subset of A
    
    Union (A ∪ B): 
    All elements in A, in B, or in both
    
    Intersection (A ∩ B): 
    Elements common to both A and B
    
    Difference (A - B): 
    Elements in A but not in B

        Related to the Problem statement:

        Context:
        An online store launches a new fitness smartwatch.

            📦 Sets:
            A = Customers who liked the product
            B = Customers who bought the product
            C = Customers who recommended it to others
    
    Example:
    Let’s say:

            A = {Ravi, Sneha, Arjun, Meena, John}
            B = {Arjun, Meena, John, Priya}
            C = {Meena, John, Aditya}
    
        🔹 Operations:
        A ∪ B (Liked or Bought) = {Ravi, Sneha, Arjun, Meena, John, Priya}
        A ∩ B (Liked & Bought) = {Arjun, Meena, John}
        A - B (Liked but not Bought) = {Ravi, Sneha}
        A ∩ B ∩ C (Liked, Bought, and Recommended) = {Meena, John}

# CONDITIONAL PROBABILITY – Real-time Example

        Question:
    
        If a customer liked the smartwatch, what’s the probability they actually bought it?

        Given:
            1000 customers visited the product page
            300 liked it → P(A) = 300/1000 = 0.3
            180 liked and bought it → P(A ∩ B) = 180/1000 = 0.18

         Formula:
        
            P(B∣A) = P(A∩B)/P(A) = 0.18/0.3 = 0.6

​	    📌 Interpretation:
    If a customer likes the product, there’s a 60% chance they will buy it.

# VARIANCE & STANDARD DEVIATION – Real-time Example

        Context:
        You collect 5-star ratings for the smartwatch:

        Ratings = {5, 4, 4, 3, 4}

        Mean: 5+4+4+3+4/5 = 20/5 = 4


        Variance: (5−4)^2+(4−4)^2+(4−4)^2+(3−4)^2+(4−4)^2/5 = 2/5 = 0.4 
 
        Standard Deviation:  Square root(0.4) ≈ 0.63

# Distributions:

1. Bernoulli Distribution:
    
    ➡️ Each customer can either buy (1) or not buy (0) the smartwatch.

    Example:
    
    Out of 5 users: {1, 0, 1, 1, 0}
    Each is one Bernoulli trial.

2. Binomial Distribution:

    A binomial distribution models the number of successes in n independent Bernoulli trials.

    Where:

    n = number of trials
    k = number of successes
    p = probability of success

    📦 E-commerce Example:
    
    Out of 10 visitors, how many will buy the smartwatch if the buy probability (p) is 0.3?
    n = 10 (trials = 10 visitors)
    p = 0.3
    
    Find the probability that exactly 3 buy (k = 3)

        P(X=3)=( 10/3)(0.3)^3(0.7)^7 = 0.2668

3. Normal Distribution:

    A normal distribution is a continuous probability distribution with a bell-shaped curve, where values are symmetrically distributed around the mean.

    ➤ Properties:
    
    Mean (μ): Center of the distribution
    Standard Deviation (σ): Spread of data around the mean

    Delivery time for the smartwatch follows a normal distribution:
    
    Mean delivery time = 3 days (μ = 3)
    SD = 0.5 days (σ = 0.5)
    
    This means:

    Most customers receive the product in 2.5 to 3.5 days
    Very few receive it in less than 2 or more than 4 days
    
    You can also use normal distribution for:

    Customer ratings
    Order amounts
    Time spent on product page

    <img src = "https://github.com/Pallavilathavadlamudi/GENAI/blob/main/STATISTICS/Assets/Distributions.png">
    