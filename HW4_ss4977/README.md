Assignment 1

Reviewed Tang's null hypothesis regarding citibike usage. Started by comparing the description of the null hypothesis with the formulation in the equation. Followed by describing how the what is in the citibike's data repository as it relates to what is needed to test the hypothesis and a review of Tang's data munging procedures. Finished with a discussion of how to use the output from the data munging to test the hypothesis, looking at the type of data and resultant test to use. Actual file is located in PUI2016_st1671 and has been merged into Tang's repository.

I discussed collaborating with Ben Alpert, Sofiya Elkurin, Jonathan Geis, Sebastian and Luis, but wound up working on my own for the rest.

Assignment 2

Selected the articles "Diabetes Mellitus Survey from Northeast China" and "Non-Breastfed Infants and Diarrhoeal Illnesses." Categorized the data, tests and results as presented in the tables of the two articles.

Assignment 3

Started with repeating what is in the skeleton notebook. Used the scipy.stats package to calculated p-value of the employment test using the Z-test, determining that the null hypothesis could be rejected. Tested the effect on recidivism using both chi square and Z-test finding that the null hypothesis could not be rejected. Finished by added chi square test for employment repeating the resulting of rejecting the null hypothesis.

Assignment 4

Tested the age distribution for citibike riders in 2015. First stage was to download each month of citibike data, read it into pandas, and append it to the DataFrame one-by-one. As each file was loaded, all fields that were unneeded for the tests were dropped. Remaining were start and stop time (for comparison of day and night), user type, birth year, and gender (for comparison of genders). Added age fields for each gender by subtracting birth year from the present year. Since gender and birth year are only available for subscribers, this is present only for subscribers. Aggregated the data to five-year age ranges, using professor's lines of code. Created visual representations of the distribution of ages for male and female riders. Ran the aggregate data through the scipy.stats routines for K-S, Pearson, and Spearman tests. Obtained p-values between 0 and 2.16e-11.

Repeated the test using 1 out of every 200 records in the DataFrame. Created the reduced DataFrame by building an array consisting of integers divisible by 200 up to the size of the DataFrame and selected for records with an index in the array. Repeated the processing from the full DataFrame on the reduced one as well as the three tests. Obtained p-values ranging from 1.09e-71 to 2.09e-11.

For testing age distribution by day and by night, added fields for starting hour and ending hour. Defined daytime as starting and finishing between 7 AM and 7 PM and nightime as both starting and finishing between 8PM and 6 AM. Created age fields for day and night in the manner that was done for gender. Repeated the aggregation and visualization tasks that were done for gender and ran the three tests with p-values ranging from 2.89e-106 to 2.36e-9.
