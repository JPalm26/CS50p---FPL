# Fantasy Football Engine
#### Video Demo:  <URL https://youtu.be/egfLQc_7aVo>
#### Description:
My project is a programme that allows the user to search players, teams or positions in fantasy football, and outputs tables showing data on the players. It uses the fantasy football api database, and the fpl class as well.

The project was completed in the project.py file. Because of the nature of the FPL class used, the asyncio and aiohttp libraries had to be used to work with the fpl database, and async functions were used. Numerous functions were used to get the player or team ids in order to search through the database. I originally was going to use the fpl class functionality, but found that in order for that to work, it required you to know the player name id. I therefore created a function, get_id which loads every player from the database and searches their name in order to return their id. This was then passed into my search_player function, where the fpl class could then be used to find the player cost, goals, assists and more.

A similar thing was done in search_team, where by finding the index of each team in a list and adding 1, I could get the team id. This meant that I could do a similar process in get_team, where I iterated over the database again, returning all the player ids from that team which could then be passed into the fpl class terms.

Search position also let users select the position from the list, and from the list index, their position id could be found. I again iterated over the database to find the id of players who shared that position id, and the same could be done again.

To save redundancies I created a create_table function, which took a list of lists of player information, and outputted it in a PrettyTable with headers for name, cost , goals, assists, points per game and total points.

Finally, the choice function used the inquirer library to allow the user to select options from a list, such as position or team name, to make user input easier and save the need for error checking.

