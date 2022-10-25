Capstone Proposal

Name: Invade

Project Overview: Display "cool" data from Riot Games API focused on League of Legends

-What are the major features of your web application? Display interesting data/results from Riot Games API into a Django project
-What problem is it attempting to solve? Improve gameplay via knowledge of historical play
-What libraries or frameworks will you use? Riot Games API (https://developer.riotgames.com/), RiotWatcher (https://github.com/pseudonym117/Riot-Watcher), and more that I'll discover

Functionality:

-What will they see on each page? Index page will have a field to input user name and region of user (start off with just myself as the user), pulls match history
-What can they input and click and see? Fields to input user name and region
How will their actions correspond to events on the back-end? Pull data from API

-Data Model:

I envision that some key findings will be from lots of historical data on one user and I also find it interesting to get data from a friend that the primary user plays with. Not sure how the two data models will intersect yet - never worked on that before.

Schedule:

-Week 1/Milestone 1: Get index.html working with match history for 1 player (5 games)
-Week 2/Milestone 2: See how much total data I can pull from 1 player and pick the -relevant data to present
-Week 3/Milestone 3: Evaluate if I can pull data from 2 players and then compare them in a relevant way (Stretch Goal)
-Week 4/Milestone 4: CSS, make everything look better

List of things done so far:
1. Get Riot Games API key
2. Created getchampions.py to get list of champions and their respective data but realized that data dragon already does this
3. Converted list of champions from a string into a json file
4. Created a champions model
5. Created a custom management command to load champions.json into the database
6. Created a vue app to list all champions and their respective images
7. Created views for four key stats and display the top 10 champions per stat
8. Created an API to replace previous hard-coded data view; couldn't get top 10 list to work now