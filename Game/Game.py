import random
import sys
import unittest


PLAYER_NAME_PREFIX = "player"
MESSAGE_PENALTY = "Oops! one penalty has been added to your account."
MESSAGE_SKIP = "Sorry! You have to skip the next chance!"
MESSAGE_SAFE = "Thank God! You're now safe from penalty."
MESSAGE_EXTRA_CHANCE = "Awesome! You got one extra chance to roll the dice."
MESSAGE_FORMAT_NO_POINTS = "{} has to skip this chance as a penalty! No points awarded"
MESSAGE_FORMAT_ONE_ROUND_SCORE = "player: {} current score {} total score: {}"
MESSAGE_FORMAT_CONGRATS_WIN = "Congrats to player {} for winning"
MESSAGE_GAME_COMPLETE = "Game is completed!"
MESSAGE_ERROR_SWW = "Something Went Wrong: {}"
MESSAGE_ERROR_NUM_PLAYER_INTEGER = "Must provide positive integer value to Num of Players"
MESSAGE_ERROR_TARGET_SCORE_INTEGER = "Must provide positive integer value to target score"


class CustomException(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

        # __str__ is to print() the value

    def __str__(self):
        return repr(self.value)


class Dice:
    """

    faces: number of faces of dice
    choices: all the choices for a dice
    """

    def __init__(self, faces=None):
        self.faces = 6
        self.choices = list(range(1, 7))
        if faces is not None and type(faces) is int:
            self.faces = faces
            self.choices = list(range(1, faces + 1))

    def roll(self):
        """

        gives random value everytime based on the choices available
        :return: number
        """
        return random.choice(self.choices)


class Players:
    """

    number_of_players: total number of players playing a game
    players: list of player names
    scores: a dictionary of players with their scores
    turn: index of the players list that gives who's the turn this time
    """

    def __init__(self, count=None):
        self.number_of_players = 2
        self.players = ["player1", "player2"]
        self.scores = {
            "player1": 0,
            "player2": 0
        }
        self.turn = 0

        if count is not None and type(count) is int:
            temp_players = []
            temp_scores = {}
            for i in range(1, count + 1):
                player = PLAYER_NAME_PREFIX + str(i)
                temp_players.append(player)
                temp_scores.update({player: 0})
            self.players = temp_players
            self.scores = temp_scores

    def getPlayersList(self):
        """

        :return:
        """
        return self.players

    def getScores(self):
        """

        :return:
        """
        return self.scores

    def shufflePlayers(self):
        """

        :return:
        """
        random.shuffle(self.players)
        return self.players

    def getNextPlayer(self):
        """

        :return:
        """
        curr_turn = self.turn
        self.turn = (self.turn + 1) % len(self.players)
        return self.players[curr_turn]

    def getScoreOfPayer(self, player):
        """

        :param player:
        :return:
        """
        if player is None or player not in self.players:
            return 0
        return self.scores[player]

    def updatePlayerScore(self, player, points, target_score):
        """

        :param player:
        :param points:
        :param target_score:
        :return:
        """
        if player is not None and player in self.players:
            new_score = self.scores[player] + points
            if new_score >= target_score:
                new_score = target_score
            self.scores.update({player: new_score})
            return new_score
        return 0


class ScoreBoard:
    """

    winners: a set of all winners names
    max_rank: a pointer to point to the next winner rank to be assigned on runtime
    locked_ranks: a list of tuples of the winners with rank and score. format of tuple (rank, name, score)
    win_score: target score of game
    """

    def __init__(self, win_score):
        """

        :param: win_Score: The target score of game
        """
        self.winners = set([])
        self.max_rank = 1
        self.locked_ranks = []
        self.win_score = win_score

    def sortScores(self, scores):
        """

        :param scores:
        :return:
        """
        new_scores = [(v, k) for k, v in scores.items()]
        print(new_scores)
        new_scores.sort(reverse=True)
        print(new_scores)

    def sortScoresDict(self, old_scores):
        """
        sorts a dict of scores. high is the highest possible
        :param old_scores:
        :return:
        """
        high = self.win_score
        scores = [(v, k) for k, v in old_scores.items()]
        count = {}

        # calculate the histogram of scores:
        for x, y in scores:
            score, arr = count.get(x, (0, []))
            arr.append(y)
            count[x] = (score + 1, arr)

        # transcribe the histogram into the sorted scores
        sorts = []
        for i in range(high + 1):  # i = 0, 1, ... k-1
            if i in count:
                eyes = []
                for item in count[i][1]:
                    eyes.append((i, item))
                # eyes = [i] * count[i]
                sorts.extend(eyes)

        # print("scores %s sorted is %s" % (scores, sorts))
        return sorts

    def createScoreBoard(self, sorted_score_tuple_list):
        """

        :param sorted_score_tuple_list:
        :return:
        """

        print("{} - {} - {}".format("rank", "player", "score"))
        for winning_player in self.locked_ranks:
            rank, name, score = winning_player
            print("{} -- {} -- {}".format(rank, name, score))

        curr_rank = self.max_rank
        for i in reversed(sorted_score_tuple_list):

            if i[1] not in self.winners:
                # print("winner", i[1])
                if i[0] >= self.win_score:
                    self.winners.add(i[1])
                    self.locked_ranks.append((self.max_rank, i[1], i[0]))
                    print("{} -- {} -- {}".format(self.max_rank, i[1], i[0]))
                    self.max_rank += 1
                    curr_rank = self.max_rank
                else:
                    print("{} -- {} -- {}".format(curr_rank, i[1], i[0]))
                    curr_rank += 1

    def printScoreBoard(self, player_scores):
        """

        :param player_scores:
        :return:
        """
        self.createScoreBoard(self.sortScoresDict(player_scores))


class GamePlay:
    """

    GamePlay is the main class for the Game of Dice
    """

    def __init__(self, num_of_players, winning_score):
        """

        :param num_of_players: Number of participants
        :param winning_score: target score of game
        """
        if num_players is not None and winning_score is not None and type(num_players) is not int or type(num_players) is not int:
            raise CustomException("Must add integer values as number of player and target score")
        self.players = Players(num_of_players)
        self.dice = Dice()
        self.win_score = winning_score
        self.players.shufflePlayers()
        all_players = self.players.getPlayersList()
        self.skip = {key: False for key in all_players}
        self.penalty = {key: 0 for key in all_players}
        self.winner = {key: False for key in all_players}
        self.score_board = ScoreBoard(winning_score)
        self.winners_count = 0
        self.players_count = num_of_players

    def isWinner(self, player):
        """

        :param player:
        :return:
        """
        return self.winner[player]

    def playOneChance(self):
        """

        :return:
        """
        player = self.players.getNextPlayer()
        if not self.isWinner(player):
            if self.isPlayerRestricted(player):
                print(MESSAGE_FORMAT_NO_POINTS.format(player))
                print(MESSAGE_FORMAT_ONE_ROUND_SCORE.format(player, 0, self.players.getScoreOfPayer(player)))
                self.removePlayerRestriction(player)
            else:
                roll_point = self.dice.roll()
                self.printCurrentPoint(roll_point)
                point = roll_point
                if roll_point == 1:
                    print(MESSAGE_PENALTY)
                    self.penalty[player] = self.penalty[player] + 1
                    if self.penalty[player] > 1:
                        print(MESSAGE_SKIP)
                        self.skip[player] = True
                else:
                    if self.penalty[player] > 0:
                        print(MESSAGE_SAFE)
                        self.penalty[player] = 0
                while roll_point == 6:
                    print(MESSAGE_EXTRA_CHANCE)
                    roll_point = self.dice.roll()
                    self.printCurrentPoint(roll_point)
                    point += roll_point
                self.updatePlayerScore(player, point)
                print(MESSAGE_FORMAT_ONE_ROUND_SCORE.format(player, point,
                                                                           self.players.getScoreOfPayer(player)))
                if self.isWinner(player):
                    print(MESSAGE_FORMAT_CONGRATS_WIN.format(player))
            self.printScoreBoard()

    def play(self):
        """
        Main function to drive the whole game
        :return:
        """
        try:
            while not self.isGameFinished():
                self.playOneChance()

            print(MESSAGE_GAME_COMPLETE)
        except CustomException as error:
            print('A New Exception occurred: ', error.value)
        except Exception as err:
            print("Something Went Wrong: {}".format(str(err)))

    def playNChances(self, n):
        """

        :param n:
        :return:
        """
        for i in range(0, n):
            self.playOneChance()

    def isGameFinished(self):
        """

        :return:
        """
        return (self.players_count - self.winners_count) <= 1

    def updatePlayerScore(self, player, point):
        """

        :param player:
        :param point:
        :return:
        """

        new_score = self.players.updatePlayerScore(player, point, self.win_score)
        if new_score == self.win_score:
            self.winner.update({player: True})
            self.winners_count += 1

    def isPlayerRestricted(self, player):
        """

        :param player:
        :return:
        """
        return self.skip[player]

    def removePlayerRestriction(self, player):
        """

        :param player:
        :return:
        """
        self.skip[player] = False
        self.penalty[player] = 0

    def printCurrentPoint(self, point):
        """

        :param point:
        :return:
        """
        print("You got {}".format(point))

    def printScoreBoard(self):
        """

        :return:
        """
        self.score_board.printScoreBoard(self.players.getScores())
        # print("PLAYER -------- SCORE")
        # for key, value in self.players.getScores().items():
        #     print("{} -------- {}".format(key, value))


# And now the tests


class TestGamePlay(unittest.TestCase):

    def test_examples(self):
        """test some examples"""
        game = GamePlay(2, 25)
        game.play()
        players = game.players.getPlayersList()
        winner_score = 0
        loser_score = 0
        for player in players:
            if game.isWinner(player):
                winner_score = game.players.getScoreOfPayer(player)
            else:
                loser_score = game.players.getScoreOfPayer(player)
        self.assertEqual(winner_score > loser_score, True, "Winner Score %s should be more than Loser score %s" % (winner_score, loser_score))


def inputDetails():
    print("provide arguments in following manner on command line: ")
    print("python GameOfDice/Game/Game.py num_players target_score")
    print("Example: ")
    print("python GameOfDice/Game/Game.py 2 25")
    print("For Test")
    print("provide arguments in following manner: test")


if __name__ == "__main__":
    n = len(sys.argv)
    print(n)
    print(sys.argv)
    try:
        if n == 2 and sys.argv[1] == "test":
            suite = unittest.TestLoader().loadTestsFromTestCase(TestGamePlay)
            unittest.TextTestRunner(verbosity=2).run(suite)
        elif n == 3:
            try:
                num_players = int(sys.argv[1])
            except:
                raise CustomException(MESSAGE_ERROR_NUM_PLAYER_INTEGER)
            try:
                target_score = int(sys.argv[2])
            except:
                raise CustomException(MESSAGE_ERROR_TARGET_SCORE_INTEGER)

            game = GamePlay(num_players, target_score)
            game.play()
        else:
            inputDetails()
    except CustomException as e:
        print(MESSAGE_ERROR_SWW.format(str(e)))
        inputDetails()
    except Exception as e:
        print(MESSAGE_ERROR_SWW.format(str(e)))
        inputDetails()
