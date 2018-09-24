soccer_team = {
        'team_name': ': Atlanta United FC',
        'team_color': ': red',
        'team_players': {'forward_1':'Josef Martínez',
                         'mid_1':'Miguel Almirón',
                         'mid_2':'Ezequiel Barco',
                         'mid_3':'Héctor Villalba',
                         'kepper_1':'Brad Guzan',
                         'defen_1':'Leandro González Pírez',
                         'defen_2':'Michael Parkhurst',
                         'defen_3':'Greg Garza',
                         'mid_4':'Eric Remedi',
                         'mid_5':'Darlington Nagbe',
                         'defen_4':'Franco Escobar'
                         }
        }
while True:
        cmd = input("Do you wanna change the team name and team color, press y, if not press n.? ")
        if cmd == 'y':
           new_name = 'team_name'
           new_name = input("what would you like to name it: " )
           soccer_team['team_name'] = new_name
           new_color = 'team_color'
           new_color = input("what would you like to change the color to: " )
           soccer_team['team_color'] = new_color
        elif cmd == 'n':
           for k,v in soccer_team.items():
                print(k,v)
        else:
           break
current_score = []
def sub_player(team_players):
              sub_change = input('press C to sub players')
              if cmd == 'c':
               new_player = 'team_players'
               soccer_team['team_players']= new_player
               
        
