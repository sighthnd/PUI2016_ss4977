#Su Siyang's Plot Review
<c>![Screenshot 1 Assignment 2: my .bashrc](https://github.com/sighthnd/PUI2016_ss4977/blob/master/HW8_ss4977/HW7_ss9558.png?raw=true)</c>
<br><br>
Su's plot clear shows that the number of riders peaks around age 30 for both genders and accurately conveys the relative scale of male and female ridership. The caption concisely and accurately describes the content of the plot, but does not mention the source of the data or time period. The plot is missing a title and the type size of the axis-labels is a bit small.
<br><br>
An additional improvement would be to equalize the age ranges for the male and female riders. Due to the oldest female rider being a few years younger than the oldest male rider, the bins for the female histogram are slightly narrower than those for the male historgram and are thus out of sync with each other. Another improvement which might be harder to implement would be to have the bars for male and female side-by-side instead of one on top of another. This would clear up a potential ambiguity as to whether the tops of the blue bars represent the male ridership or the total (male + female) ridership. A possible way to do so would be:
<br><br>
```
colors = ['Steelblue', 'Indianred']
labels = ['male', 'female']
df_male = df_age[df_age.gender == 1]
df_female = df_age[df_age.gender == 2]
plt.hist([df_male, df_female], bins=50, histtype='bar', color=colors, label=labels)
```
