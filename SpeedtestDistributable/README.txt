SpeedTracker
VERSION: 1.1

So you want to track your internet speeds?  Cool.

REQUIREMENTS:	Python installed

AUTHOR: Dylan Hahn, September 2016
LICENSE: Free to modify and distribute

WINDOWS:
Simply double-click on SpeedTracker.cmd to start the script.
	From there, leave it running in the background and it will run a speedtest every 15 minutes
	If you want to change the interval, I leave it up to you to modify the SpeedTracker.cmd

Once you have your data, double-click conversion.py
	This will propogate the data into testspeed.csv

Open testspeed.csv in your spreadsheet editor of choice (currently tested with MS Excel and LibreOffice)
	Now you have your data so you can make all the pretty graphs you want

UNIX: (currently tested on Fedora 21)
Run the SpeedTracker script
    ** NOTE ** You may need to add permissions to Speedtracker and speedtest_cli.py to allow them to run
    From there, leave it running in the background and it will run a speedtest every 15 minutes
    If you want to change the interval, I leave it up to you to modify the SpeedTracker

Once you have your data, run conversion.py
    ** NOTE ** You may need to add permissions to conversion.py to allow it to run
    This will propogate the data into testspeed.csv

Open testspeed.csv in your spreadsheet editor of choice (currently tested with MS Excel and LibreOffice)
	Now you have your data so you can make all the pretty graphs you want
