import glob
import csv

files = glob.glob(".\\*\\*\\goals.csv")

# continuar para contar quantos gols cada rodada, de cada ano, teve
with open('all goals.csv', 'w', newline = '') as all_goals:
    writer = csv.writer(all_goals)
    game = 1
    for file in files:
        year = file[-14:-10]
        print(file[2:-10])
        games = 0
        with open(file, newline = '') as csvfile:
            read = csv.reader(csvfile)
            for line in read:
                games = line[-1]

        games = int(games) + 1
        for igame in range(1, games):
            goals = 0
            with open(file, newline = '') as csvfile:
                read = csv.reader(csvfile)
                for line in read:
                    if line[-1] != 'Game' and int(line[-1]) == igame:
                        goals += 1

            # game = int(igame) + 380 * (int(year) - 2013)
            if game < 10:
                game = '0000' + str(game)
            elif game < 100:
                game = '000' + str(game)
            elif game < 1000:
                game = '00' + str(game)
            elif game < 10000:
                game = '0' + str(game)
            else:
                game = str(game)
            writer.writerow([year, game, str(goals)])
            game = int(game) + 1

            

files = glob.glob(".\\Copa do Brasil\\*\\goals.csv")

# continuar para contar quantos gols cada rodada, de cada ano, teve
with open('all goals - CdB.csv', 'w', newline = '') as all_goals:
    writer = csv.writer(all_goals)
    game = 1
    for file in files:
        year = file[-14:-10]
        print(file[2:-10])
        games = 0
        with open(file, newline = '') as csvfile:
            read = csv.reader(csvfile)
            for line in read:
                games = line[-1]

        games = int(games) + 1
        for igame in range(1, games):
            goals = 0
            with open(file, newline = '') as csvfile:
                read = csv.reader(csvfile)
                for line in read:
                    if line[-1] != 'Game' and int(line[-1]) == igame:
                        goals += 1

            # game = int(igame) + 380 * (int(year) - 2013)
            if game < 10:
                game = '000' + str(game)
            elif game < 100:
                game = '00' + str(game)
            elif game < 1000:
                game = '0' + str(game)
            else:
                game = str(game)
            writer.writerow([year, game, str(goals)])
            game = int(game) + 1

            

files = glob.glob(".\\Serie A\\*\\goals.csv")

# continuar para contar quantos gols cada rodada, de cada ano, teve
with open('all goals - SA.csv', 'w', newline = '') as all_goals:
    writer = csv.writer(all_goals)
    game = 1
    for file in files:
        year = file[-14:-10]
        print(file[2:-10])
        games = 0
        with open(file, newline = '') as csvfile:
            read = csv.reader(csvfile)
            for line in read:
                games = line[-1]

        games = int(games) + 1
        for igame in range(1, games):
            goals = 0
            with open(file, newline = '') as csvfile:
                read = csv.reader(csvfile)
                for line in read:
                    if line[-1] != 'Game' and int(line[-1]) == igame:
                        goals += 1

            # game = int(igame) + 380 * (int(year) - 2013)
            if game < 10:
                game = '000' + str(game)
            elif game < 100:
                game = '00' + str(game)
            elif game < 1000:
                game = '0' + str(game)
            else:
                game = str(game)
            writer.writerow([year, game, str(goals)])
            game = int(game) + 1

            

files = glob.glob(".\\Serie B\\*\\goals.csv")

# continuar para contar quantos gols cada rodada, de cada ano, teve
with open('all goals - SB.csv', 'w', newline = '') as all_goals:
    writer = csv.writer(all_goals)
    game = 1
    for file in files:
        year = file[-14:-10]
        print(file[2:-10])
        games = 0
        with open(file, newline = '') as csvfile:
            read = csv.reader(csvfile)
            for line in read:
                games = line[-1]

        games = int(games) + 1
        for igame in range(1, games):
            goals = 0
            with open(file, newline = '') as csvfile:
                read = csv.reader(csvfile)
                for line in read:
                    if line[-1] != 'Game' and int(line[-1]) == igame:
                        goals += 1

            # game = int(igame) + 380 * (int(year) - 2013)
            if game < 10:
                game = '000' + str(game)
            elif game < 100:
                game = '00' + str(game)
            elif game < 1000:
                game = '0' + str(game)
            else:
                game = str(game)
            writer.writerow([year, game, str(goals)])
            game = int(game) + 1

            

files = glob.glob(".\\Serie C\\*\\goals.csv")

# continuar para contar quantos gols cada rodada, de cada ano, teve
with open('all goals - SC.csv', 'w', newline = '') as all_goals:
    writer = csv.writer(all_goals)
    game = 1
    for file in files:
        year = file[-14:-10]
        print(file[2:-10])
        games = 0
        with open(file, newline = '') as csvfile:
            read = csv.reader(csvfile)
            for line in read:
                games = line[-1]

        games = int(games) + 1
        for igame in range(1, games):
            goals = 0
            with open(file, newline = '') as csvfile:
                read = csv.reader(csvfile)
                for line in read:
                    if line[-1] != 'Game' and int(line[-1]) == igame:
                        goals += 1

            # game = int(igame) + 380 * (int(year) - 2013)
            if game < 10:
                game = '000' + str(game)
            elif game < 100:
                game = '00' + str(game)
            elif game < 1000:
                game = '0' + str(game)
            else:
                game = str(game)
            writer.writerow([year, game, str(goals)])
            game = int(game) + 1

            

files = glob.glob(".\\Serie D\\*\\goals.csv")

# continuar para contar quantos gols cada rodada, de cada ano, teve
with open('all goals - SD.csv', 'w', newline = '') as all_goals:
    writer = csv.writer(all_goals)
    game = 1
    for file in files:
        year = file[-14:-10]
        print(file[2:-10])
        games = 0
        with open(file, newline = '') as csvfile:
            read = csv.reader(csvfile)
            for line in read:
                games = line[-1]

        games = int(games) + 1
        for igame in range(1, games):
            goals = 0
            with open(file, newline = '') as csvfile:
                read = csv.reader(csvfile)
                for line in read:
                    if line[-1] != 'Game' and int(line[-1]) == igame:
                        goals += 1

            # game = int(igame) + 380 * (int(year) - 2013)
            if game < 10:
                game = '000' + str(game)
            elif game < 100:
                game = '00' + str(game)
            elif game < 1000:
                game = '0' + str(game)
            else:
                game = str(game)
            writer.writerow([year, game, str(goals)])
            game = int(game) + 1
