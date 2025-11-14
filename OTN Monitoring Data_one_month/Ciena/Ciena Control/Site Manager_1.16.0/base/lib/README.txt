#Date#
21-June-2016

#Description about#
controlsfx-8.40.11-SNAPSHOT.jar

#Website of the ControlFx Project#
http://fxexperience.com/controlsfx/

#ControlFX code can be found at#
https://bitbucket.org/controlsfx/controlsfx/downloads#tag-downloads 

#Build Process# 
The jar controlsfx-8.40.11-SNAPSHOT.jar has been build by using gradle build.

#History#
Site Manager was using the controlFx jar controlsfx-8.40.10-SNAPSHOT.jar since release 11.1,
to achieve the column filter on the Site Manager FX table.
Site Manager was having following customized classes which were internally using the ControlFx APIs
	CustomColumnFilter.java
	CustomTableFilter.java
	CustomFilterPanel.java

#Problem with the current implementation#
There was memory leakage observed when at the certain time interval table data keep on changing.
On long run, Site Manager consumes lot of heap memory and it reaches to the allocated memory after 5 to 6 hours of continuous run.

#Current Implementation#
Site manager uses the current version of ControlFX code controlsfx-98754286c1a7
The current version has optimized code which solve the maximum memory leakage.

#Changes done in current ControlFX code for the use in Site Manager#
Following three files has been modified which could be compared with the code present on the ControlFx repository
	ColumnFilter.java
	FilterValue.java
	TableFilter.java