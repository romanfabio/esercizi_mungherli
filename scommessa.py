import random
random.seed()

def createBets(players: int, max: int) -> dict:
    bets = {}
    for i in range(players):
        bet = random.randint(0,max)
        if bet in bets:
            bets[bet] += 1
        else:
            bets[bet] = 1

    return bets

def removeDuplicates(bets: dict) -> list[int]:
    newBets = []
    count = 0
    for key in bets:
        if bets[key] == 1:
            newBets.append(key)
        else:
            count += 1
    print('Found and removed', count, 'duplicated bets')
    return newBets 

def whoWon(bets: list[int], winning_number: int) -> int:

    min = winning_number - bets[0]
    winner = bets[0]

    for bet in bets:
        diff = winning_number - bet
        if diff < min:
            min = diff
            winner = bet
    return winner


def play(players: int, winning_number: int) -> int:
    print('Number of players:', players)
    print('Maximum bet:', winning_number)

    bets = createBets(players, winning_number)
    bets = removeDuplicates(bets)
    print('Bets:',bets)

    if len(bets) == 0:
        return -1

    return whoWon(bets, winning_number)


def start():
    players = int(input('How many players? '))
    rounds = int(input('How many rounds? '))
    winning_number = 1000

    for round in range(rounds):
        print('*** [ ROUND', round, '] ***')
        winning_number = play(players, winning_number)

        if winning_number < 0:
            print('There are no more bets')
            break
        else:
            print('Winner:', winning_number)


start()