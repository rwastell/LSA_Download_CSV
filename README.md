WLMNS DASHBOARD AUTOMATION DOCUMENTATION


Intro:
The goals of the code are to update the following fields in TDX: Serial Number, Model, Processor, Memory, Operating System, Storage, and down the line Location. Currently the only fields that are being run and updated are the model and operating system. Serial number is attached to the CSV housing these changes only for the reason of finding the correct asset.

Google Scripts Portion:
The google scripts application takes in the data from sheet1 of a google spreadsheet named Automation TDX Test. Currently all the google sheets and google scripts are in my account (rwastell@umich.edu) however they will be moved into a shared drive upon full completion. Additionally the google script takes in input from two other spreadsheets responsible for mapping the models and operating systems to their TDX counterparts. The Google script takes in the data from Sheet1, then performs the mapping for model and operating system. From here the output is added into a new sheet named Output within the Automation TDX Test spreadsheet. Upon completion an email will be sent out to specified moderators of this automation, containing the models and operating systems that it was unable to map. (See the mapping spreadsheets sections for what to do to map).

OS Mapping Spreadsheet:
This is the spreadsheet for mapping the Operating systems in the WLMNS dashboard to their TDX operating systems. All of the TDX names for the Operating Systems are in the FIRST column of the spreadsheet. Every cell within the same row will be mapped to the value listed in the first column of that row. IN ORDER TO ADD: Simply copy and paste value to map to the first empty column in the row of desired operating system.

Model Mapping Spreadsheet:
This is the spreadsheet for mapping the models in the WLMNS dashboard to their TDX models. All of the TDX names for the models are in the FIRST column of the spreadsheet. Every cell within the same row will be mapped to the value listed in the first column of that row. IN ORDER TO ADD: Simply copy and paste value to map to the first empty column in the row of desired model.

Python Script:
There is an additional python script that is housed (possibly at this point, waiting to get confirmation from jess and alex) within the same folder as the tool created to update the TDX records (created by Jesse and Alex). This script is only an infinite while loop that carries out the download when the day and time matches the day and time specified in the line of code below the schedule download comment. This script will download the output sheet in the Automation TDX Test file as a csv, thus allowing the TDX updater to match TDX records to the records in the now downloaded csv.

