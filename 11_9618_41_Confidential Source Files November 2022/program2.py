class Card:
    def __init__(self,Num,Color):
        self.__Number = Num
        self.__Color = Color
    def GetNumber(self):
        return(self.__Number)
    def GetColor(self):
        return(self.__Color)

class Hand:
    def __init__(self,  Card1, Card2, Card3, Card4, Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0
        self.__NumberCards = 5
    
    def GetCards(self, Index):
        return self.__Cards[Index]
    
def CalculateValue(Player):
    Score = 0
    for Count in range(0, 4):
        CardGot = Player.GetCards(Count)
        Score = Score + CardGot.GetNumber()
        Colour = CardGot.GetColor()
        if Colour == "red":
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        else:
            Score = Score + 15
    return Score
    
OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")
OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")
OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed,OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow,FiveYellow, OneBlue)

Player1score = CalculateValue(Player1)
Player2score = CalculateValue(Player2)
if Player1score > Player2score:
 print("Player 1 wins")
elif Player1score < Player2score:
 print("Player 2 wins")
else:
 print("It's a draw")