Contains a plot of demonstrating the Central Limit Theorem on the $\chi^2(1)$ distribution. The plot shows the behavior of the variance and other behavior of the distribution of the means of samples of $\chi^2(1)$ variables resembling the normal distribution as the sizes of the individual samples increases.

## Assignment 2
Borrowed some ideas from Sebastian Gutierrez and shared some with Ben Alpert, Sofiya Elyukin, and Jonathan Geis.

#### 311 complaints
Imported the 311 complaints data file and previewed the first few records. Grouped and aggregated by borough to get a listing of boroughs in the DataFrame and a count of how many of each. Repeated that for Community Board, identifying genuine and spurious Community Boards. Counted number of rows with a unique value for "Unique Key", produced a list of duplicated records, printed the list, and removed the duplicates. Identified how many records had missing values for each column. Added a column to identify which records did not have a valid community board and deleted those records. Grouped and aggregated the remainder of the DataFrame by Community Board.

#### Demographics and internet access
Imported the file for Community Board demographics and printed a list of columns. Verified that the DataFrame has 59 rows, one for each Community Board. Created a field to add up the income categories below $30,000. Created a reduced DataFrame that only has columns I anticipated to affect rates of calling 311, including that might affect the prevalence of inducements to call 311 and what might affect one's propensity to act on those inducements. Changed the cd_id field to conform to the format in the 311 complaints DataFrame.

Imported the file for internet access by Community Board. Printed list of columns and list of Community Board descriptors. Added column cd_id and set its value to the Community Board name in the format of the 311 complaints DataFrame. Added column Mobile add set it to the sum of the columns identified as "with Mobile Broadband".

#### Drawing inferences from the three datasets
Merged the three DataFrames. Printed a few rows and listed the columns of the merged DataFrame. Added a column for complaints per 1000 people. Ran a regression of complaints per 1000 against English speaker, density, education, low income, and mobile internet access and reported results.
