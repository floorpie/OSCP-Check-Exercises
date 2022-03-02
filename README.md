# TO DO - Alter script to check exercise number based on the Offsec Training Library (OTL) exercise numbering.

# About this script
This is a python script that checks your lab report to see if there are any unincluded/missing exercises. It DOES NOT check whether the exercise(s) are completed, it simply checks if the exercise number is included in your lab report.

# Pre-requisites
- docx2txt library (will be required to read your .docx lab report)
```text
$ pip install docx2txt
```
# Running the script
Run this python script with the absolute path to your .docx file as the first argument.
```text
$ python OSCP-Check-Exercises.py [file.docx]
```
