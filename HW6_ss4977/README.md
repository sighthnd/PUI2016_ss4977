## Assignment 1
Discussed project with Sofiya Elyukin, Ben Alpert and Luis Melchor. Also provided some guidance to Adrian.

PLUTO shape file was downloaded manually, copied into PUIDATA, and loaded with GeoPandas.
Energy usage was accessed using the API and imported using Pandas. Separate DataFrames nrg and bldgs were created on
building energy and base layer respectively containing just the fields of potential interest. Scatter plot created
on nrg.

Converted column BBL to type string in both nrg and bldgs. Converted data in nrg columns "number of buildings",
"dof property floor area", "reported floor area", and "site eui kbtu/ft2" to float or NaN where not a valid number.
Joined the two DataFrames into bblnrgdata and created a scatter plot on bblnrgdata. Created column TotalEnergy1 by multiplying
energy/ft2 by "reported floor area" and TotalEnergy2 by multiplying energy/ft2 by LotArea. Discovered that LotArea was not
useful, so only use TotalEnergy1.

Looked if there was anything to see with residential usage before deciding to just look at total usage. Produced scatter
plot of TotalEnergy1 and UnitsTotal. Produced scatter plots on a logarithmic scale of TotalEnergy1 and UnitsTotal both with
TotalEnergy1 and UnitsTotal on the x-axis.

Created reduced dataset bblnrg_cut with only records in with more than 10 units and
consuming more than 1000 kbtu. Created columns logEnergy and logUnits as the log10 of TotalEnergy1 and UnitsTotal
in bblnrg_cut. Ran OLS with logEnergy and dependent and logUnits as independent
and plotted logEnergy and logUnits with a trend line. Ran OLS with logUnits and dependent and logEnergy as independent
and plotted with trend line. Created logUnSq containing constant, logUnits, and square of logUnits, and ran OLS with logEnergy
as dependent and logUnSq and independent. Plotted with 2nd-degree polynomial trend line.

Printed summaries of linear model and 2nd-degree polynomial regressions. Polynomial has higher adjusted R^2, but linear has
higher AIC and BIC. Calculated chi^2 statistic for the regression using the unlogged data. Whereas log(Energy-hat) = a +
b * log(Units), Energy-hat = 10^a * Units^b. Compared that to actual energy consumption to calculate residuals and divided
by square root of energy consumption to calculate the chi^2 for each individual lot and added them up for the chi^2 statistic.
Compared the log-likelihood ratios of the linear and polynomial models.

Wrote a procedure to calculate the sum of squared residuals in the linear model for any given value of x-intercept and slope
and used that to plot a log-likelihood surface.

## Assignment 2
The write up of my citibike experiment can be found at https://www.authorea.com/users/106728/articles/134506/_show_article

# FBB very goodere
simple idea, clean execusion, intsting result
