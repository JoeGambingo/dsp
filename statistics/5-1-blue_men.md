[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 47.7% of U.S. men could be in Blue Man Group, but not me :(  
Below is my code.

```
# Behavioral Risk Factor Surveillance System
import brfss
df = brfss.ReadBrfss()

male_heights = df[df.sex == 1].htm3
height_cdf = thinkstats2.Cdf(male_heights)

blue_man_min = 177.8 #5'10'' in cm
blue_man_max = 185.4 #6'1'' in cm

100*(height_cdf[blue_man_max] - height_cdf[blue_man_min])
```
