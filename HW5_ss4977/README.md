{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Assignment 1\n",
    "Discussed with Sebastian Gutierrez, Sofiya, Ben Alpert, but mostly wrote the code myself.\n",
    "\n",
    "Stated null hypothesis of normal distribution and another null hypothesis of poisson distribution.\n",
    "\n",
    "Reused code for importing bike ridership data from previous homeworks.\n",
    "\n",
    "Drop all columns that do not either provide age information or geographic information (the latter for if I had managed to get to separating by boroughs) and all rows that are non-subscribers, which do not have birth years.\n",
    "\n",
    "Created 4-year bins from age 10 to age 98 and created a bar graph showing number of rides in each age bracket in order to visualize the distribution. Generated normal and poisson distributions. Using a parameter of 2 would have given higher moments closer to that of the age distribution, but since poisson is a discrete distribution, doing so and scaling to the mean and variance of the age distribution created a disjointed distribution, so I switched to using a parameter of 39, the mean of the age distribution. Binned the generated distributions and built a normalized cumulative distribution of the age distribution and the generated distribution and plotted them.\n",
    "\n",
    "From the scipy.stats package, ran the Kolmogorov-Smirnov and $\\chi^2$ tests for the age distribution against both normal and poisson distribution. Ran the Anderson-Darling test against the normal distribution and attempted to run it, using anderson_ksamp, against the poisson distribution.\n",
    "\n",
    "### Assignment 2\n",
    "Through Cell 15, wrote everything on my own. Subsequent to that, exchanged some ideas with Pune Famili.\n",
    "\n",
    "Created dictionaries to facilitate writing a loop to import each race/gender combination as opposed to writing the commands separately for each combination. Imported each spreadsheet and viewed what was in the contents.\n",
    "\n",
    "Made the first attempt at creating a scatter plot. The median income and gini ratio did not plot because those columns had rows with invalid data. Did some further looking through the data, in particular, the Median income column.\n",
    "\n",
    "Tested setting invalid data to NaN on a column and then created a loop to go through all columns in all sheets. With invalid values set to NaN, created the scatter plots.\n",
    "\n",
    "Started collabortion with Pune. Created plots of median income for total group population by race. First plot had a line showing male median = female median. Then ran OLS using the matrix algebra definition of $\\beta=(X^TX)^{-1}X^TY$ to obtain x-intercept and slope and plotted showing that line. Ran the spearman test to obtain an alternate regression line and plotted showing both the spearman and the OLS lines.\n",
    "\n",
    "Created lists holding all male and all female median incomes. Then created a mask which would indicate which elements are NaN in either list and used that to create a lists of valid data. Using those lists, ran OLS, zero-intercept OLS, and spearman regression. Finally, plotted all the median income data points and the three regression lines.\n",
    "\n",
    "### Assignment 3\n",
    "Wrote statements and equations to describe null and alternate hypotheses for each of the four questions."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PUI2016_Python2",
   "language": "python",
   "name": "pui2016_python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
