```stata
clear

pause on

capture log using "C:\Users\Jack\Documents\School\508\Jomarron.Final Exam Log.txt", text replace

use "C:\Users\Jack\Downloads\dow_jones_data.dta"

gen date=mdy(month,day,year)
tsset date
format date %td
*1a
twoway line dji_close date
*1b
gen ln_dji_close=ln(dji_close)
dfuller ln_dji_close
*non-stationary
*1c
gen dln_dji_close=ln_dji_close-ln_dji_close[_n-1]
dfuller dln_dji_close
*stationary

*1d
arima dln_dji_close, arima(1,0,0)
*It is negative so a mean reversion

*1e
arima dln_dji_close if covid19_china==0, arima(1,0,0)

arima dln_dji_close if covid19_row==0, arima(1,0,0)
*Not different than 0 so it's a random walk

*1f
*I should invest my money because if it is mean reversion then and I would 
//predict an upswing

*1g
arima dln_dji_close, arima(1,0,0)
estimates store r1
arima dln_dji_close, arima(0,0,1)
estimates store r2
arima dln_dji_close, arima(1,0,1)
estimates store r3
arima dln_dji_close, arima(1,0,2)
estimates store r4
arima dln_dji_close, arima(1,0,3)
estimates store r5
arima dln_dji_close, arima(2,0,0)
estimates store r6
arima dln_dji_close, arima(2,0,1)
estimates store r7
arima dln_dji_close, arima(2,0,2)
estimates store r8
arima dln_dji_close, arima(2,0,3)
estimates store r9
arima dln_dji_close, arima(3,0,0)
estimates store r10
arima dln_dji_close, arima(3,0,1)
estimates store r11
arima dln_dji_close, arima(3,0,2)
estimates store r12
arima dln_dji_close, arima(3,0,3)
estimate store r13

estimates table r1 r2 r3 r4 r5 r6, stat(aic bic)
estimates table r7 r8 r9 r10 r11 r12 r13, stat(aic bic)
*Model R12 fits best because it has the lowest AIC and BIC

*1h
gen first_part=1 if day>30 | day<4
replace first_part=0 if first_part==.

tab day_of_week, gen(dow)
tab month, gen(month)

*i
reg dln_dji_close first_part dow1 dow2 dow3 dow4
*no turn of the month effects
*ii
reg dln_dji_close month1 month2 month3 month4 month5 month6 month7 month8 month9 month10 month11
*January/turn of year effects yes

*1i
*i
replace covid19_china=covid19_china/1000
replace covid19_row=covid19_row/1000
*ii
reg dln_dji_close covid19_china covid19_row i.day i.day_of_week
*1 for every increase in the coronavirus case the daily growth rate of the 
//change decreases by 0.01834%
//covid19_row is not different from 0
*2 Covid-19_china does
*iii
gen l1_covid19_china=covid19_china[_n-1]
gen l2_covid19_china=covid19_china[_n-2]

gen l1_covid19_row=covid19_row[_n-1]
gen l2_covid19_row=covid19_row[_n-2]

reg dln_dji_close covid19_china l1_covid19_china l2_covid19_china covid19_row l1_covid19_row l2_covid19_row i.day i.day_of_week
*ROW Covid cases are significant. The higher first lag follows the idea that it grows regularly after the first lag. However, after 2 days people are realizing the negative effect. It takes time for positive cases to 

*iv
*1 it should have a squared component because the variable follows an exponential growth rate
*2
gen sq_covid19_china=(covid19_china)^2
gen sq_covid19_row=(covid19_row)^2

reg dln_dji_close covid19_china sq_covid19_china covid19_row sq_covid19_row i.day i.day_of_week
*interpretation is that china cases were not relevant. rest of world show a negative impact on the stocks and squared means that 

log close

Final Do File.txt
Displaying Final Do File.txt.
```
