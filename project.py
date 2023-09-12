from fpl import FPL
import aiohttp
import sys
import asyncio
import requests
from prettytable import PrettyTable
import inquirer
from time import sleep

menu = ["Search for Player", "Get Team Info", "Search by Position","Quit"]

try:
    response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
except requests.RequestException:
    sys.exit("Request Exception")
else:
    r = response.json()
    players = r['elements']

async def main():
    while True:
        search = choice(menu)
        if search == menu[0]:
            await search_player()
            sleep(1.0)
        elif search == menu[1]:
            await search_team()
            sleep(1.0)
        elif search == menu[2]:
            await search_position()
            sleep(1.0)
        else:
            sys.exit()

async def search_player():
    p = []
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    while True:
        try:
            player = input("Input Player Choice: ")
            id = await get_id(player)
            player_choice = await fpl.get_player(id)
        except ValueError:
            print("Invalid player")
            continue
        else:
            break
    p.extend([[player_choice.web_name, player_choice.now_cost/10, player_choice.goals_scored, player_choice.assists,player_choice.points_per_game, player_choice.total_points]])
    print(await create_table(p))
    await session.close()

async def search_team():
    teams = ["Arsenal", "Aston Villa","Bournemouth","Brentford","Brighton","Burnley","Chelsea", "Crystal Palace", "Everton", "Fulham","Liverpool","Luton","Man City","Man Utd", "Newcastle","Nott'm Forest","Sheffield Utd","Spurs","West Ham","Wolves" ]
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    selection = choice(teams)
    id = teams.index(selection) + 1
    ids = await get_team(id)
    info = []
    total = 0
    for x in ids:
        player = []
        player_choice = await fpl.get_player(x)
        player.extend([player_choice.web_name, player_choice.now_cost/10, player_choice.goals_scored, player_choice.assists,player_choice.points_per_game, player_choice.total_points])
        info.append(player)
        total += player_choice.total_points
    table = await create_table(info)
    table.title = 'Team Name: '+ selection
    print(table)
    print("Team Points:", total)
    await session.close()

async def search_position():
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    positions = ["Goalkeepers", "Defenders", "Midfielders", "Forwards"]
    position = choice(positions)
    index = positions.index(position) + 1
    info = []
    for i in range(606):
        player = []
        if players[i]['element_type'] == index:
            player_choice = await fpl.get_player(players[i]["id"])
            player.extend([player_choice.web_name, player_choice.now_cost/10, player_choice.goals_scored, player_choice.assists,player_choice.points_per_game, player_choice.total_points])
            info.append(player)
    table = await create_table(info)
    table.title = "Position: " + position
    print(table)
    await session.close()


async def get_id(player):
    for i in range(606):
        if players[i]['second_name'] == player:
            return players[i]['id']


async def create_table(table):

    player_table = PrettyTable()
    player_table.field_names = ["Player", "£", "G", "A","PPG", "TP"]
    player_table.align["Player"] = "l"
    for i in table:
        player_table.add_row(i)
    player_table.reversesort = True
    player_table.sortby = "TP"
    return player_table

async def get_team(id):
    ids = []
    for i in range(606):
        if players[i]['team'] == id:
            ids.append(players[i]['id'])
    return ids



def choice(option):
    questions = [
    inquirer.List('size',
    message = "Please make selection",
    choices = option,),
    ]
    answers = inquirer.prompt(questions)
    selection = answers['size']
    return selection


if __name__ == "__main__":
    if sys.version_info >= (3, 7):
        asyncio.run(main())