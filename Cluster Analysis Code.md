```sas
/* Read Data from bigblue */
filename webdat url 
    "http://bigblue.depaul.edu/jlee141/econdata/eco520/online_retail.csv" ;
PROC IMPORT DATAFILE= webdat OUT= online_retail
     DBMS=CSV REPLACE;
RUN;

proc surveyselect data=online_retail method=srs seed = 44044277
     n = 20000 out=mysales ;
run;


data sales1  ; set mysales ; 
   date = datepart(Invoicedate) ;
   yearmm = year(date)*100+month(date) ;
   totalsale = UnitPrice*Quantity ;
   logtotal = log(totalsale) ; 
   month = month(date) ;
   quarter = qtr(date) ; 
   itemID = 1*substr(StockCode,1,4) ;
   if itemID = . then delete ;
   l_date = '31DEC2011'D ;
   format date l_date mmddyy10.     ;
   if country = "United Kingdom" then UK = 1 ; else UK = 0 ;
   if totalsale = . then delete  ;
 run ;
proc means ; run ; 

PROC SQL;
Create table Customer_summary as
   select distinct CustomerID,
       max(Date) as Recent_date format = date9.,
       (l_Date - max(Date)) as Recency ,
       count(InvoiceDate) as Frequency,
       log(Sum(totalsale)) as Monetary format=dollar15.2
   from sales1 
   group by CustomerID;
quit;
proc means data=Customer_summary ; run ;

PROC SQL;
Create table item_summary as
   select distinct itemID,
       mean(l_Date - (Date)) as Recency ,
       count(InvoiceDate) as Frequency,
       log(Sum(totalsale)) as Monetary format=f5.2
   from sales1 
   group by itemID;
quit;

*1;
proc univariate data=Customer_summary;
	var Frequency Recency Monetary;
run;
*Frequency Analysis;
proc freq data=Customer_summary;
	tables Frequency;
run;

proc sgplot data=Customer_summary;
	vbox Frequency;
run;
*Monetary Analysis;
proc sgplot data=Customer_summary;
	vbox Monetary;
run;

*Frequency>90, Recency=none, Monetary>7;

data cust_summ; set Customer_summary;
	if Frequency>100 then delete;
	if Monetary>7 then delete;
	if 0>Recency then delete;
run;

proc sgplot data=cust_summ; 
	vbox Frequency;
run;

proc sgplot data=cust_summ;
	vbox Monetary;
run;
	
proc cluster data=cust_summ out=clsdat method=ward print=7 ccc pseudo;
	var Frequency Recency Monetary;
	copy CustomerID;
run;

proc tree data=clsdat ncl=3 out=clstree ;
  copy Frequency Recency Monetary Customerid  ;
run;

proc sgplot data=clstree;
	scatter y=Frequency x=Recency/group=cluster datalabel=CustomerID;
run;

proc sgplot data=clstree;
	scatter y=Frequency x=Monetary/group=cluster datalabel=CustomerID;
run;

proc sgplot data=clstree;
	scatter y=Monetary x=Recency/group=cluster datalabel=CustomerID;
run;
*Non-Hierarchical;
proc fastclus data=cust_summ out=fast_cls maxclusters=3;
	var Monetary Recency Frequency;
run;

proc sgplot data=fast_cls;
	scatter y=Monetary x=Recency / group=cluster datalabel=CustomerID;
run;
*Compare;
proc summary data=clstree print n mean median max min; var Frequency Recency Monetary; class cluster; title "Ward Method"; run;

proc summary data=fast_cls print n mean median max min; var Frequency Recency Monetary; class cluster; title "non-Hierarchical Method"; run;


*2;
proc univariate data=item_summary;
	var Frequency Recency Monetary;
run;

proc sgplot data=item_summary; 
	vbox Frequency;
run;

proc sgplot data=item_summary;
	vbox Recency;
run;

proc sgplot data=item_summary;
	vbox Monetary;
run;

*No Outliers need to be deleted;
	
proc cluster data=item_summary out=clsdat1 method=ward print=7 ccc pseudo;
	var Frequency Recency Monetary;
	copy itemID;
run;

proc tree data=clsdat1 ncl=4 out=clstree1 ;
  copy Frequency Recency Monetary itemID  ;
run ;

proc sgplot data=clstree1;
	scatter y=Frequency x=Recency/group=cluster datalabel=itemID;
run;

proc sgplot data=clstree1;
	scatter y=Frequency x=Monetary/group=cluster datalabel=itemID;
run;

proc sgplot data=clstree1;
	scatter y=Monetary x=Recency/group=cluster datalabel=itemID;
run;
*Non-Hierarchical;
proc fastclus data=item_summary out=fast_cls1 maxclusters=4;
	var Monetary Recency Frequency;
run;

proc sgplot data=fast_cls1;
	scatter y=Frequency x=Recency / group=cluster datalabel=itemID;
run;

proc sgplot data=fast_cls1;
	scatter y=Frequency x=Monetary / group=cluster datalabel=itemID;
run;

proc sgplot data=fast_cls1;
	scatter y=Monetary x=Recency / group=cluster datalabel=itemID;
run;

proc summary data=clstree1 print n mean median max min; var Frequency Recency Monetary; class cluster; title "Ward Method"; run;

proc summary data=fast_cls1 print n mean median max min; var Frequency Recency Monetary; class cluster; title "non-Hierarchical Method"; run;
```
