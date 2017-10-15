# Created by: David Wang
# Created on: 13-Oct-2017
# Created for: ICS3U
# Daily Assignment - Unit3-04
# This program displays the leap year program

import ui

def check_touch_up_inside(sender):
    #Check if entered year is an integer
    
    #input
    year = view['year_textbox'].text
    try:
        year = int(year)
    except:
        view['outcome_label'].text = '"' + str(year) + '"' + ' is not an integer.'
    
    # check for leap year
    
    # process
    if (int(year) % 4) == 0:
        if (int(year) % 100) == 0:
            if (int(year) % 400) == 0:
    # output
                view['outcome_label'].text = 'The year ' + str(year) + ' is a leap year.'
            else:
                view['outcome_label'].text = 'The year ' + str(year) + ' is not a leap year.'
        else:
            view['outcome_label'].text = 'The year ' + str(year) + ' is a leap year.'
    else:
        view['outcome_label'].text = 'The year ' + str(year) + ' is not a leap year.'

view = ui.load_view()
view.present('full_screen')
