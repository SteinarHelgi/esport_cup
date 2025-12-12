# Brackenizer Hópur 8

## Introduction
The following system is designed for organizing esports tournaments and accessing information regarding teams, tournaments, and players competing in esports.

## Assignment and Group Information
This README file is for an educational assignment in "Verklegt námskeið 1", a course in Computer Science at Reykjavík University.

### Students Involved
- Agnar Bjarki Garðarsson - [agnar24@ru.is]
- Hilmir Ægir Ómarsson - [hilmiro25@ru.is]
- Sigrún Viðarsdóttir - [sigrunv24@ru.is]
- Steinar Helgi Halldórsson - [steinarh25@ru.is]
- Þröstur Hrafnkelsson - [throstur25@ru.is]

## Instructions
To run this system, you need to have Python installed. Then, run the `main.py` file inside the zip folder. 

Using the system requires no login. However, if you want to edit a team, you need to type in the team captain's handle (e.g., to view the team "WhileTrue Tryhards," use the handle "WhileTrueWendy").

##Structure
Data:
"""The CSV files contain files which we use for data about everything involving the system, teams, tournaments, players, matches etc.
│──────────────Repo 		
├── CSV files 		#CSV files(8 in total) 
├── api_data.py
├── club_data.py
├── contact_person_data.py
├── game_data.py
├── match_data.py
├── player_data.py
├── team_data.py
├── team_registry_data.py
└── tournament_data.py


Logic:				#These files handle the logic for everything
│
├── api_ll.py
├── club_ll.py
├── game_ll.py
├── main_ll.py
├── player_ll.py
├── team_ll.py
└── tournament_ll.py
└── validators_ll.py
Models:				#Model classes for everything in the system
├── club.py
├── contact_person.py
├── game.py
├── match.py
├── models.py
├── organizer.py
├── player.py
├── team_captain.py
├── team_registry.py
├── team.py
└── tournament.py

UI:				#Everything that the user sees and how it connects 				the system together
│
├── functions.py
├── main_ui.py
├── menu_management.py
├── organiser_ui.py
├── shrek.py
├── ui_functions.py
└── user_ui.py

main.py
README.md
contract.md


## Educational Video
Below is a link to the educational tutorial video for this system:
[Educational Tutorial](https://youtu.be/-Ji6JJOAhek)

## Features
- Organizes esports tournaments.
- Provides information on teams and players.
- No login required for basic access.



## Contact
For further questions, please contact the team members listed above.