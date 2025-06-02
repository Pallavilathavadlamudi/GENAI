# PRODUCT ADOPTION MODEL

PROBLEM STATEMENT: 
To analyze and predict the likelihood of customers liking, purchasing, and responding to a new product and its related variants?

# Questions:
    1. Do customers like this product?
    2. Do customers get (buy) this product?
    3. What is the probability that a customer will return to buy again?
    4. What’s the chance a person will recommend this product to others?
    5. What’s the probability of profit/loss after launching the product?
    6. What happens when we implement a family of this product in the market?
    
    Later if the product is liked by the customers:
    1. If we increase the price, what is the probability that purchases will drop?

# BASIC IDEA 

1. PROBABILITY: 

    Is a meaasure of how likely something is to happen 
        1. It is a number bwtween 0 and 1  
            0 is not likely to happen
            1 is likely to happen
            0.5 (between) there is an equal chance of event happening or not happening

    Explaning the above questions:

    Consider a survey taken from the 100 customers. 

    1. Do customers like this product? (this question estimates how many customers liked the product)

            Probability :  Number of customers liked the product / Total number of customers visited the product
                = 75/100 = 0.75

    2. Do customers get (buy) this product? (this question estimates how many customers actually purchased the product)

            Probability : Number of customers purchased/ Number of customers liked the product
                = 30/75 = 0.4

    3. What is the probability that a customer will return to buy again? (this question estimates whether the customer rebuys the product or not)

            Probability : Number of customers wanted to rebuy / number of customers once purchased
                = 15/30 = 0.5

    4. What’s the chance a person will recommend this product to others?(this question estimates do really customer suggest to the other customers)

             Probability : Number of customers suggested / Number of customers purchased
                = 10/30 = 0.33

2. RANDOM EXPERIMENT: 

    It is process that leads to one outcome from possible outcomes. where we dont know in advance which outcome will occur.

    Related to the problem statement:
       
        Each customer interaction with the product can be seen as a Random Experiment (Notice, Like, buy, rebuy, recommend)

        Each Question = A random Experiment 
            The outcome would be 
                1. Noticed / Didnot Noticed 
                2. Liked / Didnot Liked
                3. Buy / Didnot Buy
                4. Recommend / willnot recommend

3. RANDOM VARIABLE:

        Is a function that assigns a numerical value to each outcome of a random experiment. 
    
    TYPES: 
    1. DISCRETE RANDOM VARIABLES: 

        Variables that can take countable values such as 1,2,3,...

            Related to the problem statement:
            
                1. Number of customers liked product
                2. Number of purchases
                3. Number of Recommendations

    2. CONTINUOUS RANDOM VARIABLES:
     
        Variables that can take an infinite number of values in a given range.
    
            Related to the problem statement:

                1. Money Spent
                2. Customer Satisfaction

4. BASIC OUTCOME, SAMPLING SPACE, EVENT: 

    1. BASIC OUTCOME: 

        Is a most specific result of a random experiment(any one of the possible outcome from a random experiment)
    
    2. SAMPLING SPACE(S): 

        The set of all possible outcomes for any random experiment is called Sampling Space.
    
    3. EVENT(E):
    
        The outcome of any experiment is called an event. (E)

    Related to the problem statement:

        1. Do customers like this product?
            Basic outcome: {like},{Don't like}
            Sampling Space: S = {like, Don't like}
            Event: E = {Like} -> customer like the product.
        
        2. Do customers buy this product?
            Basic outcome: {Buy},{Don't buy}
            Sampling Space: S = {buy, Don't buy}
            Event: E = {Buy} -> Customer buys the product.

        3. Will customer buy again?
            Basic outcome: {rebuy},{Don't rebuy} / return
            Sampling Space: S = {rebuy, Don't rebuy} / return
            Event: E = {rebuy} -> customer rebuys the product.

        4. Will customer recommend?
            Basic outcome: {recommend},{Don't recommend}
            Sampling Space: S = {recommend, Don't recommend}
            Event: E = {Dont recommend} -> Customer doesnot recommend the product.

        5. How much will a customer spend?
            Basic outcome: {10},{20},{30}
            Sampling Space: S = {any real number > 0 }
            Event: E = {30} -> Customer spends 30$ on the product.

        6. What rating will customer give?
            Basic outcome: {1},{2},{3}
            Sampling Space: S = {1,2,3,...,10}
            Event: E = {8} -> Customer gives rating for product as 8. 

# FUNCTIONS 

1. PROBABILITY MASS FUNCTION: 
       
        Is a function that gives the probability that a discrete random variable is exactly equal to some value.(FOR discrete values)
        
                        pX(x)=P(X=x)

            Related to the problem statement:

            Consider the Survey of 100 customers
                Consider the results as 
                    1. 20 customers didn’t buy at all (0 times)
                    2. 50 customers bought once
                    3. 20 customers bought twice
                    4. 10 customers bought three times

                Consider the result as 
                    1. 10 customers didnot rate the product
                    2. 20 customers gave 1 star rating
                    3. 20 customers gave 2 star rating
                    4. 15 customers gave 3 star rating
                    5. 30 customers gave 4 star rating
                    6. 5 customers gave 5 star rating
                    
            Question

            1. How many times did the customers buy the product?

                Consider X = Number of times a person bought the product in month
                Possible values(0,1,2,3)

                pX(x)=P(X=x)= Number of customers who bought x times/Total number of customers surveyed

                p(0) = 20/100 = 0.2 (didnot buy) 
                p(1) = 50/100 = 0.5 (bought once)   
                p(2) = 20/100 = 0.2 (bought twice)
                p(3) = 10/100 = 0.1 (bought thrice)

            2. How did customers rate the product?
                
                pX(x)=P(X=x)= total number of customers rate the product / Total number of customers surveyed

                p(0) = 10/100 = 0.10
                p(1) = 20/100 = 0.2
                p(2) = 20/100 = 0.2
                p(3) = 15/100 = 0.15
                p(4) = 30/100 = 0.30
                p(5) = 5/100 =  0.05

2. CUMULATIVE DISTRIBUTION FUNCTION:

        It gives the probability that a random variable is less than or equal to a certain value.(for discrete values)

        Related to the problem statement:
        
        Consider the ratings given by the customers:
            P(X≤3) means the customers has given the rating 1,2 or 3

                                    x
            Formula =  F(x)=P(X≤x)= ∑ P(X=k)
                                   k=1

            exclude the customer who didnot rate the product?
            
                    100 - 10 = 90

                p(1) = 20/90 = 0.222
                p(2) = 20/90 = 0.222
                p(3) = 15/90 = 0.166

                        P(X≤3)=P(X=1)+P(X=2)+P(X=3)
                        = P(X≤3) = 0.222+0.222+0.166 = 0.61

                    so, 61% of the customers gave 3 star or less

3. PROBABILITY DENSITY FUNCTION: 

        The area under the curve between two values tells us the probability that a value lies in that range.(for continuous values).

                               x2
                P(x1 ≤ X ≤ x2)=∫ f(x)dx
                               x1

            Related to the problem statement:
            
                Consider the Price of the Product

                    X1 and X2 can be the range of values 

4. PROBABILITY DISTRIBUTIONS

    That gives the probabilities of occurrence of possible events for an experiment.

    1. Discrete Probability Distribution:

        (To count the things) the probability distribution of a random variable that can take on only a countable number of values.

            Related to the problem statement:

                1. Do customers like this product? 
                    each person can answer yes(1) or no (0)

                        75 Customers liked the product!! So, we can say exactly the number.

    2. Continuous Probability Distribution:

        (To measure the things) which can take on any value within a given range. 
        The outcomes can be any number -> including decimals within a range.

            Related to the problem statement:

                1.What’s the profit after the product launch?
                    Profit could be $10,000 or $10,000.75 
