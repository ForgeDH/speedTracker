import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace('\\', '/')

txtfilepath = str(dir_path) + '/testspeed.txt'
csvfilepath = str(dir_path) + '/testspeed.csv'

pingregex = re.compile(".*: (\d*\.\d*) ms.*")
downregex = re.compile(".*Download: (\d*\.\d*) Mbit/s.*")
upregex = re.compile(".*Upload: (\d*\.\d*) Mbit/s")
csvfile = open(csvfilepath, "w")
csvfile.write("Date Time,Ping (ms),Down (Mbps),Up (Mbps),,\n")

with open(txtfilepath) as f:
    lines = f.readlines()

date, time, ping, down, up = "", "", "", "", ""
for line in lines:
    if re.search(".*\d{2}/\d{2}/\d{4}.*", line):
        date = line[4:14]
    if re.search("(\d{1,2}:){2}\d{2}\.\d{1,9}", line):
        time = line[:8]
    if re.search("Hosted by", line):
        ping = pingregex.match(line).group(1)
    if re.search("Download:", line):
        down = downregex.match(line).group(1)
    if re.search("Upload:", line):
        up = upregex.match(line).group(1)
        csvfile.write("%s %s,%s,%s,%s,,\n" % (date, time, ping, down, up))

csvfile.close()


