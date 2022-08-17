# Image Formation Filtering

### [Specification](resources/ass1-spec.pdf)



## Task 1 - Height of Sculpture 

* use pinhole projection
* ground plane is perfectly flat and horizontal
* camera is placed 56.35 m away from the statue at a height of 1.6 m
* optical axis is exactly parallel to the ground plane
* vertical axis is exactly aligned with the vertical axis in the world
* imaging sensor in this camera is 16.32 mm high by 9.77 mm wide
* image was taken with a focal length of 194 mm

Show your work and include a **diagram** to illustrate how you set up the problem in your written report. 

**Coding is optional** for this question, but if you do not submit code, you must provide the formulas used to compute your answer in your written report.



## Task 2 - Filters

Write an algorithm to count the number of **intersections** and **dead ends** in randomly-generated mazes.

* detect the intersections in the maze (points where the path branches into 2 or more paths) 
* detect the dead ends in the maze (points where the path ends, not counting the start/exit points) 

* Each maze consists of black lines on a white background and has a start/exit point at the top/bottom edge of the image.

* You can assume the line width, line spacing, line colour, and background colour will be the same for all mazes.
* Your algorithm should work correctly for any maze image from this generator.
* Importantly, your algorithm should also be efficient.
* You should only use **spatial filtering** and **matrix operations** to solve this problem.
* You can and should design your own filter kernels for this task.
* Your code should not iterate over pixels. Solutions that involve iterating over pixels will receive 0 marks for this problem.
* Your written report should give the intersection and dead end **counts** for the two sample mazes, and briefly explain your method.
* Show the **kernel values** that you used in your filtering steps and include **figures** to illustrate the result of each filtering step on a sample maze.
* [Maze Generator](https://www.mazegenerator.net/)



## Submission

* The response to each question should be no more than 500 words.
* Submission will be made via the Canvas LMS. Please submit your code and written report **separately** under the Assignment 1 link on Canvas.
* Your code submission should include the Jupyter Notebook (please use the provided template) with your code and any image files we will need to run your code. Please include the cell output in your notebook submission if possible.
* Your written report should be a .pdf with your answers to each of the questions. The report should address the questions posed in this assignment and include any images, diagrams, or tables required by the question.
