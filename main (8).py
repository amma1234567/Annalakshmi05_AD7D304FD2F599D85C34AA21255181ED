#define the base class player
class Player:
  def play(self):
    print("the player is playing cricket.")
    #define the derived class batsman
class Batsman(Player):
  def play(self):
              print("the batsman is batting.")
               #define the derived class bowler
class Bowler(Player):
  def play(self):
    print("the bowler is bowling.")

batsman=Batsman()
bowler=Bowler()
player=Player()

batsman.play()
bowler.play()
player.play()