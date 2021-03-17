```ruby
filename webdat url "http://bigblue.depaul.edu/jlee141/econdata/eco520/airbnb2019.csv" ;

/* Import Chicago Community data*/
PROC IMPORT OUT= airbnb0 DATAFILE= webdat DBMS=CSV REPLACE;
     GETNAMES=YES;   DATAROW=2; 
RUN;
proc contents ; run ;

/* Create your own random sample data. Make sure type your student ID as seed number Replace your_depaul_id with your student id (only numbers)      */
proc surveyselect data= airbnb0 method=srs seed = 44044277
     n = 3000 out=airbnb1 ;
run;

data airbnb2 ; set airbnb1 ;
     logprice = log(price) ;
     logaccomodates = log(accommodates) ;
     if           host_total_listings_count < 2  then hostclass = 1  ; 
     else if 2 <= host_total_listings_count < 50 then hostclass = 2  ; 
     else                                             hostclass = 3  ;
run ;

proc means ; run ; 


*1;

proc sgscatter data=airbnb2;
	plot price*(accommodates bathrooms bedrooms beds review_scores_rating number_of_reviews);
run;

data airbnb3; set airbnb2;
	rev_score_rat_sq=(review_scores_rating)**2;
	beds_sq=(beds)**2;
	bathrooms_sq=(bathrooms)**2;
run;

*2
I want to transform price because prices will not be normally distributed (it is right skewed).;

*3;
proc reg data=airbnb2;
	model price=accommodates;
	model logprice=logaccomodates;
run;

*4;
data airbnb4; set airbnb3;
	if hostclass=1 then dum1=1; else dum1=0;
	if hostclass=2 then dum2=1; else dum2=0;
	if hostclass=3 then dum3=1; else dum3=0;
run;

proc reg data=airbnb4;
	model price=accommodates dum1-dum3;
	model logprice=logaccomodates dum1-dum3;
run;

proc glm data=airbnb4;
	class hostclass;
	model price=accommodates hostclass accommodates*hostclass / solution;
run;

proc glm data=airbnb4;
	class hostclass;
	model logprice=logaccomodates hostclass logaccomodates*hostclass / solution;
run;		

*5;
proc sort data=airbnb3;
	by logprice;
run;

%let indep_var=ListingMonth host_total_listings_count accommodates bathrooms bedrooms beds cleaning_fee guests_included 
			   extra_people minimum_nights number_of_reviews review_scores_rating calculated_host_listings_count reviews_per_month;

proc surveyselect data= airbnb3 method=srs seed = 123456
				  outall out=airbnb_train samprate=0.7;
				  strata logprice;
run;

data airbnb_train; set airbnb_train;
	y=logprice;
	if selected = 0 then y=.;
run;

proc reg data=airbnb_train;
	model y=&indep_var / selection=adjrsq;   output out=r1(where=(y=.)) predicted=yhat1;
	model y=&indep_var / selection=stepwise; output out=r2(where=(y=.)) predicted=yhat2;
	model y=accommodates bathrooms bathrooms_sq bedrooms beds_sq review_scores_rating rev_score_rat_sq minimum_nights number_of_reviews;                                
	                                                output out=r3(where=(y=.)) predicted=yhat3;
run;

*6;
data allr; merge r1 r2 r3;
	yorg=logprice;
	e1=yorg-yhat1;
	e2=yorg-yhat2;
	e3=yorg-yhat3;
	mse1=((e1)**2);
	mse2=((e2)**2);
	mse3=((e3)**2);
	rmse1=((e1)**2)**0.5;
	rmse2=((e2)**2)**0.5;
	rmse3=((e3)**2)**0.5;
	mpe1=abs((e1)/yorg);
	mpe2=abs((e2)/yorg);
	mpe3=abs((e3)/yorg);
	mae1=abs(e1);
	mae2=abs(e2);
	mae3=abs(e3);
run;	

proc means n mean data=allr; var mse:;
run;

proc means n mean data=allr; var rmse:;
run;

proc means n mean data=allr; var mpe:;
run;

proc means n mean data=allr; var mae:;
run;
	
proc sgscatter data = allr;
    plot (yhat1 yhat2 yhat3)*yorg;
    run;
```
