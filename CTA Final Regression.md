```ruby
clear
capture log using "C:\Users\Jack\Documents\School\Public Sector Economics.516\Research Paper\CTA Project Data_updated.txt", text replace

pause on


use "C:\Users\Jack\Documents\School\Public Sector Economics.516\Research Paper\CTA Project Data_Update.dta"

collapse (sum) rail_rides (mean) bus rail_boardings total_rides dow year month day bus_card_fare train_card_fare card_transfer population median_age white_per latino_per black_per asian_per operating_expenses adj_bus_card_fare adj_train_card_fare adj_card_transfer adj_operating_expenses adj_median_income daytype1 Uber_dummy Lyft_dummy, by(date1)

ssc install outreg2

drop if year<2010
gen race_ratio=white_per/(black_per+latino_per+asian_per)
tsset date1

*MODEL TESTING*
preserve 
sample 35

reg total_rides adj_median_income adj_operating_expenses adj_bus_card_fare adj_train_card_fare white_per latino_per black_per asian_per population i.Uber_dummy i.Lyft_dummy i.month i.dow i.day i.daytype1
vif
pause

stepwise, pr(.2): regress total_rides adj_median_income adj_operating_expenses adj_bus_card_fare adj_train_card_fare median_age latino_per black_per asian_per population i.Uber_dummy i.Lyft_dummy i.month i.dow i.day i.daytype1
vif
pause

reg total_rides adj_median_income adj_operating_expenses adj_bus_card_fare race_ratio population i.Uber_dummy i.Lyft_dummy i.month i.day i.daytype1
vif
pause

sort date1 
reg total_rides adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy i.month i.day i.daytype1
estimates store Test
vif
pause
restore

*REAL RESULTS*
reg total_rides adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy i.month i.day i.daytype1

outreg2 using final_res.doc, replace ctitle(Overall) keep(adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy)
estimates store Total

reg bus adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy i.month i.day i.daytype1

outreg2 using final_res.doc, append ctitle(Bus) keep(adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy)
estimates store Bus

reg rail_boardings adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy i.month i.day i.daytype1
estimates store Train

outreg2 using final_res.doc, append ctitle(Train) keep(adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy)

estimates table Total Test, b(%7.3f) stats(N r2 r2_a rmse) varwidth(30) star(0.15, 0.05, 0.01) title(CTA Ridership Analysis by City Side) d(i.month i.day i.daytype1)
pause
estimates table Total Bus Train, b(%7.3f) stats(N r2 r2_a) varwidth(30) star(0.15, 0.05, 0.01) title(CTA Ridership Analysis by City Side) d(i.month i.day i.daytype1)
pause


*BY NEIGHBORHOOD ANALYSIS*
reg rail_rides adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy i.month i.day i.daytype1
 
outreg2 using neighb_res.doc, replace ctitle(Overall) keep(adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy)

forvalues i = 1/9{
clear    	

use "C:\Users\Jack\Documents\School\Public Sector Economics.516\Research Paper\CTA Project Data_Update.dta"

drop if loop_var~=`i'

collapse (sum) rail_rides (mean) dow year month day bus_card_fare train_card_fare card_transfer population median_age white_per latino_per black_per asian_per operating_expenses adj_bus_card_fare adj_train_card_fare adj_card_transfer adj_operating_expenses adj_median_income daytype1 Uber_dummy Lyft_dummy, by(date1)
tsset date1

reg rail_rides adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy i.month i.day i.daytype1

outreg2 using neighb_res.doc, append ctitle(`i') keep(adj_median_income adj_operating_expenses d.adj_bus_card_fare white_per population i.Uber_dummy i.Lyft_dummy)
	
}

log close
```
