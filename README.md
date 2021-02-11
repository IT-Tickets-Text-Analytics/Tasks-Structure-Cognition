# Tasks-Structure-Cognition
Under the task cognition aspect, we understand categorizing tasks into routine, semi-cognitive, and cognitive based on task clarity (clear rules) and automation potential. The cognition aspect is closely related to the structure aspect, as we organize the identified parts of speech (the structure aspect) – Resources, Techniques, Capacities, Choices (RTCC) – into the three levels of Decision-Making Logic (DML) with the help of the taxonomy vocabulary. Hereby, we distinguished the following three DML levels: (i) routine DML level tasks are those expressible in rules; (ii) semi-cognitive DML level tasks are those where no exact ruleset exists, and there is a clear need for information acquisition and evaluation; (iii) cognitive DML level tasks are the most complex ones where not only information acquisition and evaluation is required but also complex problem-solving. 

This repository contains the following files: Decision Making Logic (DML) taxonomy, python file for identifying the DML keywords (as an input for python file serve tasks textual desciptions and DML taxonomy), excel file with the motivating example, threshold rules, and illustrative DML vocabulary (as an input for excel file serve threshold rules).

Below, we describe the main stages of Step 2. Structure and Cognition Aspect Extraction. 

Python code:
STAGE 1. DML taxonomy (RTCC) reading and stemming.
STAGE 2. Tasks corpus reading, preprocessing and English language filtering.
STAGE 3. Find and count words in the task text that match the DML taxonomy keywords.
STAGE 4. Writing of the matched words and their number in the *.csv file.

Excel *.csv file computing:
STAGE 5. Structure aspects identification.
STAGE 6. Calculation of the relative occurrence of the keywords of each category.
STAGE 7. DML level identification.
