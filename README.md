# Project 6: Brevet time calculator Service

Project 5 with an added API and consumer program.

Credits to Michal Young for the initial version of this code.(project 4)

# Author:
---------
- Austin Mello

#Contact Information:
----------------------
- Email: amello3@uoregon.edu

- Phone: 530-276-1662

- Zoom: amello3@uoregon.edu

# NEW ADDITIONS:
---------------
- A RESTful API that provides MongoDB info in various ways and formats from 
  the MongoDB after being submitted via the Brevet Calculator.
- A consumer program that automatically calls the API (RESTfully, of course)
  and returns information in various ways and formats.

# Description:
--------------
- Information requested as a CSV will be returned as a block of text.
- API's are located on port 5000, while the consumer program is located on 
  port 5001.
- To use the consumer program, check the bubbles for /json or /csv, or leave
  the bubbles empty for just the default.
- To add a ?top=k, just put the integer you want into the text box next to its
  corresponding button.
- This algorithm does its best to follow RUSA regulations to the letter.  If 
  certain cases were not clarified, certain assumptions were implemented.  
  Assumptions are described in further detail below.

# Notes:
--------
- There is a total of 4 containers.  One doesn't do much at all, but I was 
  quite frankly scared to get rid of it.  The functionality overall has not
  been changed by its presence, which was mentioned in the lecture as the 
  overall thing I would be graded on..  

# Built-in Tests:
----------------
- 1) The text box can only be filled in with a field greater than 0, or a 404
  will be thrown.


#Links to official RUSA regulations:
-------------------------------------
- Official Algorithm: https://rusa.org/pages/acp-brevet-control-times-calculator
- Sample calculator: https://rusa.org/octime_acp.html
- Official RUSA rules/regulations: https://rusa.org/pages/rulesForRiders

#Project 5 Assumptions:
-----------------------
- 1) If the user hits 'submit' while the table is empty, they will be directed
     to a 404 page.
- 2) If the user hits 'display' while the table is empty, if it is the first
     the user has accessed the site, it will return a 404.  Otherwise, it will
     return the contents of the previous entry.  This provides a quick, easy
     way for the user to check times they have already calculated.  It's 
     totally a feature and not a bug.
- 3) If the user inputs entries in nonconsecutive fields, the server will skip
     the blank cells and only collect the inputs.  However, the first entry 
     must always be input into the top row.
- 4) All error cases and assumptions made from project 4 STILL APPLY!


#Project 4 Assumptions:
--------------
- 1) ALL NON-NUMERICAL INPUT WILL RESULT IN A 404.

- 2) Overlap of certain distances in the table will refer to the speed in the
     previous range.
     - Example: A control at 600km will have a minimum speed of 15km/hr and a
       max of 30km/hr.

- 3) Any control that is located 20% further than the brevet distance will 
     result in a redirect to an error page.
     - Example: One cannot place a control further than 240km in a 200km brevet

- 4) Closing times at the final control point will have a set time accordance
     with Article 9 of the RUSA regulations linked above.  

- 5) The sample calculator linked above has set control points at or beyond the 
     total brevet distance at a set time.  These fixtures are not stated 
     explicitly in the RUSA regulations, so I left them out.  Instead, the final
     control point will open IN ACCORDANCE WITH THE TOTAL BREVIT DISTANCE.
     - Example: In a 200km brevet, a control point at 205km will open at 6 
       hours, 2 minutes, while a control at 200km would open at 5 hours, 53
       minutes.

- 6) Controls under 60km follow the RUSA algorithm outlined in the "oddities"
     section of the official algorithm page linked above.

