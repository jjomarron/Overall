# Clean Crime
This project sought to evaluate the effectiveness of Chicago Police Department's "stop and frisk" policy on crime. The analysis of the project was conducted in R but in order to combine all the datasets as quickly as possible to move forward in the project, I wrote this code in STATA.

I will be highlighting certain parts of the code to share particular insights but the full code is available [here](Clean Crime Code.md).

The goal of this cleaning was to end with a dataset that had counts for violent crimes, stops, and demographic data by year and zip code.

## CPD Stops Data

In this section, I cleaned the first year (2016) of stop data. I ended up running the exact script for each year so I am only sharing the first year for the sake of conciseness. 

I first looked through key data points and found that a fair amount of the information was redacted. Since this information was not available, I had no choice but to drop the observations that were redacted. This was a consideration in our data analysis because a significant percentage of the observations were redacted which might limit the efficacy of our analysis.

I dropped data that had no reported zip code as this information was not useful as it could have happened anywhere in the Chicagoland area. There were two observations without a race variable so I dropped those as well as the impacts were not significant and the missing values might distort our code.

Then, I had to convert certain variables from numerical to string. This would allow me to manipulate the strings and understand which block of the city the crimes were occurring. I did that by pulling a substring from the street number and adding "00" to the end of the partially redacted data.

I also cleaned and converted the date variables which were not in the correct format when I downloaded the data. We were limiting our analysis to various years and didn't want to doublecount so I dropped all observations that happened prior to 2017.

Finally, I had to convert all the categorical variables which were provided in Y/N format. I converted them to the numerical 1/0 format in order to evaluate them in trend or regression analysis. 

Ideally, I would have been able to run a loop and shorten my code significantly but due to the messy nature of the data and the overlapping time periods, I had to run the same code and adjust for the file path names. To avoid this, I might have renamed the file paths in STATA and then been able to run a loop but I wanted to be prioritize accuracy.

Skip code to [next comments](#Appending-Loop)

```ruby
clear
pause on


import delimited "C:\Users\Jack\Documents\School\Business Analytics.520\Final\01-JAN-2016 to 28-FEB-2017 - ISR - JUV Redacted.csv", varnames(1)

drop if contact_card_id=="REDACTED" //dropped redacted
replace zip_cd=trim(zip_cd) //tabbed zip_code and some are null
replace zip_cd=lower(zip_cd)
drop if zip_cd=="null"
drop if race_code_cd=="" //only 2 observations so I dropped them


destring contact_card_id contact_hour zip_cd cpd_unit_no created_by modified_by age height weight district sector beat area ward res_district res_sector res_beat res_area submitting_unit v_year fo_employee_id so_employee_id supv_employee_id dispersal_time number_of_persons_dispersed, replace

***ADDRESS ISSUES****
replace street_no=substr(street_no, 1, length(street_no)-2)
replace street_no=street_no+"00"
split street_nme

****DATE ISSUES****
split contact_date
split created_date
split modified_date
gen contact_date3=date(contact_date1, "MDY")
gen created_date3=date(created_date1, "MDY")
gen modified_date3=date(modified_date1, "MDY")
format contact_date3 created_date3 modified_date3 %td
gen year=year(contact_date3)
drop if year>=2017

***CATEGORICAL VARIABLES***
gen juvenile=0
replace juvenile=1 if juvenile_i=="Y"
replace juvenile=. if juvenile_i==""
gen sex=0
replace sex=1 if sex_code_cd=="M"
replace sex=. if sex_code_cd==""
gen black=0
replace black=1 if race_code_cd=="BLK"
gen hispanic=0
replace hispanic=1 if race_code_cd=="WBH" | race_code_cd=="WWH"
gen white=0
replace white=1 if race_code_cd=="WHT"
gen asian=0
replace asian=1 if race_code_cd=="API"
gen other=0
replace other=1 if race_code_cd=="I" | race_code_cd=="U" | race_code_cd=="P"
gen handcuffed=0
replace handcuffed=1 if handcuffed_i=="Y"
replace handcuffed=. if handcuffed_i==""
gen vehicle_involved=0
replace vehicle_involved=1 if vehicle_involved_i=="Y"
replace vehicle_involved=. if vehicle_involved_i==""
gen gang_lookout=0
replace gang_lookout=1 if gang_lookout_i=="Y"
replace gang_lookout=. if gang_lookout_i==""
gen gang_security=0
replace gang_security=1 if gang_security_i=="Y"
replace gang_security=. if gang_security_i==""
gen intimidation=0
replace intimidation=1 if intimidation_i=="Y"
replace intimidation=. if intimidation_i==""
gen suspect_narcotic_activity=0
replace suspect_narcotic_activity=1 if suspect_narcotic_activity_i=="Y"
replace suspect_narcotic_activity=. if suspect_narcotic_activity_i==""
gen enforcement_action_taken=0
replace enforcement_action_taken=1 if enforcement_action_taken_i=="Y"
replace enforcement_action_taken=. if enforcement_action_taken_i==""
gen indicative_drug_transaction=0
replace indicative_drug_transaction=1 if indicative_drug_transaction_i=="Y"
replace indicative_drug_transaction=. if indicative_drug_transaction_i==""
gen indicative_casing=0
replace indicative_casing=1 if indicative_casing_i=="Y"
replace indicative_casing=. if indicative_casing_i==""
gen proximity_to_crime=0
replace proximity_to_crime=1 if proximity_to_crime_i=="Y"
replace proximity_to_crime=. if proximity_to_crime_i==""
gen fits_description=0
replace fits_description=1 if fits_description_i=="Y"
replace fits_description=. if fits_description_i==""
gen fits_description_offender=0
replace fits_description_offender=1 if fits_description_offender_i=="Y"
replace fits_description_offender=. if fits_description_offender_i==""
gen gang_narcotic_related=0
replace gang_narcotic_related=1 if gang_narcotic_related_i=="Y"
replace gang_narcotic_related=. if gang_narcotic_related_i==""
gen other_factor=0
replace other_factor=1 if other_factor_i=="Y"
replace other_factor=. if other_factor_i==""
gen pat_down=0
replace pat_down=1 if pat_down_i=="Y"
replace pat_down=. if pat_down_i==""
gen pat_down_consent=0
replace pat_down_consent=1 if pat_down_consent_i=="Y"
replace pat_down_consent=. if pat_down_consent_i==""
gen pat_down_receipt_given=0
replace pat_down_receipt_given=1 if pat_down_receipt_given_i=="Y"
replace pat_down_receipt_given=. if pat_down_receipt_given_i==""
gen verbal_threats=0
replace verbal_threats=1 if verbal_threats_i=="Y"
replace verbal_threats=. if verbal_threats_i==""
gen knowledge_of_prior=0
replace knowledge_of_prior=1 if knowledge_of_prior_i=="Y"
replace knowledge_of_prior=. if knowledge_of_prior_i==""
gen actions_indicative_violence=0
replace actions_indicative_violence=1 if actions_indicative_violence_i=="Y"
replace actions_indicative_violence=. if actions_indicative_violence_i==""
gen violent_crime=0
replace violent_crime=1 if violent_crime_i=="Y"
replace violent_crime=. if violent_crime_i==""
gen suspicious_object=0
replace suspicious_object=1 if suspicious_object_i=="Y"
replace suspicious_object=. if suspicious_object_i==""
gen other_reasonable_suspicion=0
replace other_reasonable_suspicion=1 if other_reasonable_suspicion_i=="Y"
replace other_reasonable_suspicion=. if other_reasonable_suspicion_i==""
gen weapon_or_contraband_found=0
replace weapon_or_contraband_found=1 if weapon_or_contraband_found_i=="Y"
replace weapon_or_contraband_found=. if weapon_or_contraband_found_i==""
gen firearm=0
replace firearm=1 if firearm_i=="Y"
replace firearm=. if firearm_i==""
gen cocaine=0
replace cocaine=1 if cocaine_i=="Y"
replace cocaine=. if cocaine_i==""
gen heroin=0
replace heroin=1 if heroin_i=="Y"
replace heroin=. if heroin_i==""
gen other_contraband=0
replace other_contraband=1 if other_contraband_i=="Y"
replace other_contraband=. if other_contraband_i==""
gen other_weapon=0
replace other_weapon=1 if other_weapon_i=="Y"
replace other_weapon=. if other_weapon_i==""
gen cannabis=0
replace cannabis=1 if cannabis_i=="Y"
replace cannabis=. if cannabis_i==""
gen other_ctrl_sub=0
replace other_ctrl_sub=1 if other_con_sub_i=="Y"
replace other_ctrl_sub=. if other_con_sub_i==""
gen search=0
replace search=1 if search_i=="Y"
replace search=. if search_i==""
gen search_consent=0
replace search_consent=1 if search_consent_i=="Y"
replace search_consent=. if search_consent_i==""
gen search_contraband_found=0
replace search_contraband_found=1 if search_contraband_found_i=="Y"
replace search_contraband_found=. if search_contraband_found_i==""
gen search_firearm=0
replace search_firearm=1 if search_firearm_i=="Y"
replace search_firearm=. if search_firearm_i==""
gen search_cocaine=0
replace search_cocaine=1 if search_cocaine_i=="Y"
replace search_cocaine=. if search_cocaine_i==""
gen search_heroin=0
replace search_heroin=1 if search_heroin_i=="Y"
replace search_heroin=. if search_heroin_i==""
gen search_other_contraband=0
replace search_other_contraband=1 if search_other_contraband_i=="Y"
replace search_other_contraband=. if search_other_contraband_i==""
gen search_other_weapon=0
replace search_other_weapon=1 if search_other_weapon_i=="Y"
replace search_other_weapon=. if search_other_weapon_i==""
gen search_cannabis=0
replace search_cannabis=1 if search_cannabis_i=="Y"
replace search_cannabis=. if search_cannabis_i==""
gen search_other_con_sub=0
replace search_other_con_sub=1 if search_other_con_sub_i=="Y"
replace search_other_con_sub=. if search_other_con_sub_i==""
gen body_camera=0
replace body_camera=1 if body_camera_i=="Y"
replace body_camera=. if body_camera_i==""
gen car_camera=0
replace car_camera=1 if car_camera_i=="Y"
replace car_camera=. if car_camera_i==""
gen vehicle_stopped=0
replace vehicle_stopped=1 if vehicle_stopped_i=="Y"
replace vehicle_stopped=. if vehicle_stopped_i==""
gen information_refused=0
replace information_refused=1 if information_refused_i=="Y"
replace information_refused=. if information_refused_i==""
gen gang_other_c=0
replace gang_other_c=1 if gang_other_i=="Y"
replace gang_other_c=. if gang_other_i==""
gen alcohol=0
replace alcohol=1 if alcohol_i=="Y"
replace alcohol=. if alcohol_i==""
gen para=0
replace para=1 if para_i=="Y"
replace para=. if para_i==""
gen stolen_property=0
replace stolen_property=1 if stolen_property_i=="Y"
replace stolen_property=. if stolen_property_i==""
gen search_property=0
replace search_property=1 if search_property_i=="Y"
replace search_property=. if search_property_i==""
gen s_alcohol=0
replace s_alcohol=1 if s_alcohol_i=="Y"
replace s_alcohol=. if s_alcohol_i==""
gen s_para=0
replace s_para=1 if s_para_i=="Y"
replace s_para=. if s_para_i==""
gen s_stolen_property=0
replace s_stolen_property=1 if s_stolen_property_i=="Y"
replace s_stolen_property=. if s_stolen_property_i==""
gen s_other=0
replace s_other=1 if s_other_i=="Y"
replace s_other=. if s_other_i==""

save "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Stop Year 2016.dta", replace
```
## Appending Loop

In this section, I had to combine the Stop Data I had cleaned for 2016, 2017, and 2018 into one complete dataset. I utilized a forvalues loop which appended the code easily and accurately. I generated a count variable so I could easily drop the data in the future when I was matching it with the Crime Data. I then saved this complete Stop Data as separate file.

```ruby
use "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Stop Year 2016.dta"
forvalues i = 2017/2018{
append using "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Stop Year `i'.dta", force
}
gen count=1

save "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Stop Year 2016-2019.dta", replace
```

## CPD Crime Data

In this section, I used the City of Chicago's Data Portal's Crimes dataset and immediately dropped the majority of the dataset as it was outside of the range that we had stop data for. The crime data did not include the zip code so in order to aggregate crimes by zip code I extracted the address information from the Crime dataset to match that of my Stops dataset. From there, I used a bysort command to match addresses and fill thousands of missing zip codes at once.   

I then made a small date adjustment and compiled the crimes which we categorized as violent. From there, I collapsed the data in order to provide us a dataset to perform descriptive statistics on violent crime by year and zip code. We ended up using this for a cluster analysis in SAS.

```ruby
clear

import delimited "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Crimes_-_2001_to_Present.csv", varnames(1) clear

drop if year<2016
split block
replace block1=substr(block1, indexnot(block1, "0"),.)
replace block1=subinstr(block1, "X", "0",.)
replace block1="0" if block1=="00"
rename block1 street_no
rename block2 street_direction_cd
rename block3 street_nme1

append using "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Stop Year 2016-2019.dta"

bysort street_no street_direction_cd street_nme1 (zip_cd) : replace zip_cd=zip_cd[1] if mi(zip_cd)

drop if count==1
gen missing_zip=0
replace missing_zip=1 if zip_cd==.
drop count

split date
gen test_date=date(date1,"MDY")
format test_date %td

drop contact_date3
rename test_date contact_date3

gen violence=0
replace violence=1 if primarytype=="ARSON"
replace violence=1 if primarytype=="ASSAULT"
replace violence=1 if primarytype=="BATTERY"
replace violence=1 if primarytype=="CRIM SEXUAL ASSAULT"
replace violence=1 if primarytype=="CRIMINAL SEXUAL ASSAULT"
replace violence=1 if primarytype=="HOMICIDE"
replace violence=1 if primarytype=="KIDNAPPING"
replace violence=1 if primarytype=="ROBBERY"
replace violence=1 if primarytype=="SEX OFFENSE"
replace violence=1 if primarytype=="THEFT"

collapse (sum) violence, by(year zip_cd)

save "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Crimes 2016 to Present wsomeZip", replace
```
## Final Dataset

In this section, I compiled all the datasets I created to make one final dataset which we used for the bulk of our analysis.

I first called the complete Stops dataset and collapsed the data to provide us with the number of "Stop and Frisks" per zip code per day. Then, I merged this with our Zip dataset which contained demographic data for all the zip codes in Chicago. I did some quick calculations to generate key variables of interest and dropped if there were any data points with no zip code. I saved this as a new file and merged this with my cleaned Crime Data.  

After merging the two main datasets, I created a variable that would count the yearly difference between stops, and violent crimes by zip code. I dropped a few outlier zip codes and the final dataset was complete!

```ruby
clear


use "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Stop Year 2016-2019.dta", replace

*** command collapsing (aka after we're done with descriptive statistics)

collapse (sum) count , by(year zip_cd)	//	the # of SQF per day per zip code

merge m:1 zip_cd using "C:\Users\Jack\Documents\School\Business Analytics.520\Final\zip_data.dta"

gen white_per=ajwne002/ajwne001
gen hs=(ajype017+ajype018)/ajype001
gen unemp_rate=(aj1ce006/aj1ce002)
rename ajwne001 population
gen eng_only_speak=ajy2e002/ajy2e001
gen rent_per=aj1ue002/aj1ue001


drop if zip_cd==.
drop if zip_cd==60301 | zip_cd==60302 | zip_cd==60805

drop _merge

save "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Stop Counts Year 2016-2019", replace

merge 1:1 year zip_cd using "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Crimes 2016 to Present wsomeZip"
replace count=0 if count==.
drop if zip_cd==.
replace violence=0 if violence==.

replace violence=0 if violence==.
drop if zip_cd>70000 | zip_cd==61108  | zip_cd==60068 | zip_cd==60171 | zip_cd==60191 | zip_cd==60301 | zip_cd==60304 | zip_cd==60402 | zip_cd==60438 | zip_cd==60466 | zip_cd==60302 | zip_cd==60202

keep zip_cd year count count_crimes white_per hs violence unemp_rate population eng_only_speak rent_per

drop if year>2017

sort zip_cd year

gen d_violence=violence-violence[_n-1]
replace d_violence=. if year==2016

gen d_count=count-count[_n-1]
replace d_count=. if year==2016

save "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Collapsed Crimes and Stops Data-Final", replace

export delimited using "C:\Users\Jack\Documents\School\Business Analytics.520\Final\Collapsed Crimes and Stops Data-final.csv", replace
```

## Before and After
### Before
The datasets are too large to share on GitHub directly but are available for public download:

[Here](https://home.chicagopolice.org/statistics-data/isr-data/) for the Stops Data.
[Here](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2) for the Crime Data.


Here are screenshots of the untouched original datasets:
Stop Year 2016

![image](https://user-images.githubusercontent.com/80477575/111401468-58077700-8697-11eb-8610-08799251e5ad.png)

Stop Year 2017

![image](https://user-images.githubusercontent.com/80477575/111401600-943ad780-8697-11eb-869f-f3f8ff0a43d6.png)


Stop Year 2018 (290,000+ observations)

![image](https://user-images.githubusercontent.com/80477575/111401705-cd734780-8697-11eb-8c47-7f0ad7c4587f.png)

Crime Data

![image](https://user-images.githubusercontent.com/80477575/111401805-fdbae600-8697-11eb-986a-fc163d53a0f8.png)




### After

[Here](https://github.com/jjomarron/Overall/files/6153105/Collapsed.Crimes.and.Stops.Data-final.xlsx) is the final dataset

![image](https://user-images.githubusercontent.com/80477575/111401299-02cb6580-8697-11eb-88d8-8be51f12b324.png)
