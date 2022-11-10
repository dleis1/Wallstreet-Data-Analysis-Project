# Term Project Proposal 

## The Big Idea: 
### What is the main idea of your project? What topics will you explore and what will you generate? What is your minimum viable product? What is a stretch goal?

The main idea of our project is to create an app which pulls a wide-net of data for a given public or a soon to IPO company. To do this we will pull financial and text data from various API's (looking at 3-4 API's currently). One key generation for this project will be a sentiment analysis of the user inputted company using Reddit text data. Other generations will include a fractal analysis of the company's share price using the hurst exponent [Hurst exponent code](https://towardsdatascience.com/introduction-to-the-hurst-exponent-with-code-in-python-4da0414ca52e#:~:text=the%20Hurst%20exponent%20is%20a,the%20results%20can%20differ%20significantly.) Our minimum viable product will be a simple webpage where the user inputs a public company and the webpage returns a number of analytics on the company's share prices over a user inputted time period. A stretch goal may be to add more analytics to the webpage or return analytics for an entire industry. 
 
## Learning Goals 
### Since this is a team project, you may want to articulate both shared and individual learning goals.

We want to learn more about web development in this project. As well, we want to learn more about data science libraries in python as they apply to both numeric and text data. 


## Implementation Plan
### This will probably be pretty vague initially. Perhaps at this early juncture you will have identified a library or a framework that you think will be useful for your project. If you don't have any idea how you will implement your project, provide a rough plan for how you will determine this information.

We have identify a couple of libraries that will aid us in our project. First we will use the Natural Language Toolkit for our Reddit text processing and polarity output. Then we plan to use a number of other libraries such as pandas, seaborn, and numpy for data manipulation and visualization.   

## Project schedule
### You have 8 weeks (roughly) to finish the project. Sketch out a rough schedule for completing the project. Depending on your project, you may be able to do this in great specificity or you may only be able to give a broad outline. Additionally, longer projects come with increased uncertainty, and this schedule will likely need to be refined along the way.

In the next week we hope to get the API helper functions and inital webpage running. The webpage will initally return very basic information such as the share price and the head of the Reddit text data. Before Thanksgiving we hope to have the sentiment analysis module implimented into the webpage as well as one analysis of time series or numeric data. From here we hope to add an analysis per week over the next two weeks as well as functionality such as changing the local url. This should set us up to finish 


## Collaboration plan
### How do you plan to collaborate with your teammates on this project? Will you split tasks up, complete them independently, and then integrate? Will you pair program the entire thing? Make sure to articulate your plan for successfully working together as a team. This might also include information about any software development methodologies you plan to use (e.g. agile development). Make sure to make clear why you are choosing this particular organizational structure.


## Risks
### What do you view as the biggest risks to the success of this project?


## Additional Course Content
### What are some topics that we might cover in class that you think would be especially helpful for your project?