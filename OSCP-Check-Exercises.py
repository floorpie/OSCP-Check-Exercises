# Forked from original mushroom-hat script - https://github.com/mushroom-hat/OSCP-Check-Exercises
# All credit to mushroom-hat
#
# The exercise numbers WILL BE updated to reflect the exercise numbering used in the Offensive Security Training Library (Learn One subscription)
# floorp.ie - 07032022

import docx2txt
import sys

def check_exercises(filename):
    exercises = [
        '2.4.4.1', 
        '2.4.4.2',
        '2.4.4.3',
        '2.4.4.4',
        '2.4.4.5',
        '3.1.4.1',
        '3.1.4.2', 
        '3.2.6.1',
        '3.2.6.2',
        '3.3.6.1', 
        '3.3.6.2', 
        '3.3.6.3', 
        '3.5.4.1',
        '3.5.4.2',
        '3.6.4.1',
        '3.6.4.2',
        '3.6.4.3',
        '3.6.4.4',
        '3.6.4.5',
        '3.7.3.1',
        '3.7.3.2',
        '3.8.4.1',
        '3.9.4.1',
        '3.9.4.2',
        '4.2.5.1',
        '4.2.5.2',
        '4.2.5.3',
        '4.2.5.4',
        '4.3.9.1',
        '4.3.9.2',
        '4.3.9.3',
        '4.4.6.1',
        '4.4.6.2',
        '4.4.6.3',
        '4.4.6.4',
        '4.4.6.5',
        '4.5.3.1',
        '4.5.3.2',
        '4.5.3.3',
        '4.5.3.4',
        '5.7.4.1',
        '5.7.4.2',
        '5.7.4.3',
        '5.7.4.4',
        '6.3.1.1',
        '6.4.1.1',
        '6.5.1.1',
        '6.5.1.2',
        '6.7.1.1',
        '6.12.3.1',
        '6.13.2.1',
        '7.1.7.1',
        '7.1.7.2',
	  '7.1.7.3',
        '7.2.3.1',
        '7.2.3.2',
        '7.2.3.3',
        '7.2.3.4',
        '7.2.3.5',
        '7.3.3.1',
        '7.3.3.2',
        '7.3.3.4',
        '7.3.3.1',
        '7.4.3.1',
        '7.4.3.2',
        '7.5.1.1',
        '7.5.1.2',
        '7.6.4.1',
        '7.6.4.2',
        '8.2.5.1',
        '8.2.5.2',
        '8.2.5.3',
        '8.2.7.1',
        '8.2.7.2',
        '8.2.9.1',
        '8.2.9.2',
        '8.2.9.3',
        '8.3.1.1',
        '9.3.3.1',
        '9.5.2.1',
        '9.6.6.1',
        '9.6.6.2',
        '9.6.6.3',
        '9.7.2.1',
        '9.8.5.1',
        '9.8.5.2',
        '9.8.6.1',
        '9.8.6.2',
        '9.8.6.3',
	  '9.9.4.1',
	  '9.9.4.2',
	  '9.9.4.3',
	  '9.9.4.4',
	  '9.9.9.1',
	  '9.9.9.2',
	  '9.9.9.3',
	  '9.9.11.1',
	  '9.9.11.2',
	  '9.9.13.1',
	  '9.9.13.2',
        '10.2.5.1',
        '10.2.5.2',
        '11.1.1.1',
        '11.1.1.2',
        '11.2.4.1',
        '11.2.4.2',
        '11.2.4.3',
        '11.2.8.1',
        '11.2.8.2',
        '11.2.10.1',
        '11.2.10.2',
        '11.2.13.1',
        '11.2.13.2',
        '11.2.13.3',
        '11.2.15.1',
        '12.2.1.1',
        '12.2.1.2',
        '12.2.1.3',
        #YOU ARE HERE
	    '12.3.1.1',
        '12.5.1.1',
        '12.6.1.1',
        '12.7.1.1',
        '13.2.2.1',
        '13.3.2.1',
        '13.3.3.1',
        '13.3.4.1',
        '14.3.1.1',
        '15.1.3.1',
        '15.1.4.1',
        '15.1.5.1',
        '15.1.6.1',
        '15.1.7.1',
        '15.2.3.1',
        '15.2.4.1',
        '17.3.3.2',
        '17.3.3.4',
        '18.1.1.13',
        '18.1.2.1',
        '18.2.3.1',
        '18.2.4.1',
        '18.3.2.1',
        '18.3.3.1',
        '19.4.2.1',
        '20.1.1.1',
        '20.2.1.1',
        '20.2.2.1',
        '20.2.3.1',
        '20.3.1.1',
        '20.4.1.1',
        '20.5.1.1',
        '21.2.1.1',
        '21.2.2.1',
        '21.2.3.1',
        '21.2.4.1',
        '21.2.5.1',
        '21.3.3.1',
        '21.3.4.1',
        '21.3.5.1',
        '21.4.2.1',
        '21.4.3.1',
        '21.4.4.1',
        '21.5.1.1',
        '22.1.3.1',
        '22.2.1.1',
        '22.3.3.1',
        '22.3.7.1',
        '22.4.1.1',
        '22.5.4.1',
        '22.6.1.1',
        '23.1.3.1',
        '23.3.1.1',
        '24.2.2.1',
        '24.5.1.1',

    ]
    print(len(exercises))
    completed_exercise = []
    text = docx2txt.process(filename)

    # checks each line in the .docx file to see if the line contains the exercise number
    # if the line contains the exercise number, append it to another list called "completed_exercise"
    for line in text.splitlines():
        if line != '':
            for exercise in exercises:
                if exercise in line:
                    completed_exercise.append(exercise)

    # compares the PWK Exercise list with the "completed_exercise" list
    uncompleted_exercises = [ex for ex in exercises if ex not in completed_exercise]
    if uncompleted_exercises:
        print("[+] These exercises are in the PWK course but NOT in your report")
        for ex in uncompleted_exercises:
            print("Exercise {}".format(ex))
    else:
        print("[+] All exercises are included in both the PWK course and your report!")

def main(args):
    if args:
        filename = args[0]
        try:
            check_exercises(filename)
        except:
            print("Something went wrong! Check your input file path or file permissions.")
    else:
        print("File path is missing!")

if __name__ == '__main__':
    main(sys.argv[1:])
