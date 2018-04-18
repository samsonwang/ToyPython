
'''
RockPaperScissors
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock
'''

# ?? how to hide the input content


def get_player_hand (str_player_name) :
	while True :
		list_hand = ["rock", "scissors", "paper"]
		str_player_hand = input("%s enter hand: " % str_player_name)
		if str_player_hand in list_hand :
			return str_player_hand
		else :
			print("please input a valid hand")


def get_hand_bigger(str_hand1, str_hand2) :
	if str_hand1 == str_hand2 :
		return 0
	if str_hand1=="rock" :
		if str_hand2=="paper" :
			return 2
	elif str_hand1=="paper" :
		if str_hand2 == "scissors" :
			return 2
	elif str_hand1 == "scissors" :
		if str_hand2 == "rock" :
			return 2
	return 1
			
def main () :
	str_p1_name = input("enter player1 name: ")
	str_p2_name = input("enter player2 name: ")
	while True :
		str_p1_hand = get_player_hand(str_p1_name)
		str_p2_hand = get_player_hand(str_p2_name)
		num_ret = get_hand_bigger(str_p1_hand, str_p2_hand)
		if num_ret==0 :
			print("tie game")
		elif num_ret==1 :
			print("%s win" % str_p1_name)
		elif num_ret==2 :
			print("%s win" % str_p2_name)
		else :
			print("error result")
		str_continue = input("enter \"y\" to start next round: ")
		if str_continue != "y" :
			break
			
if __name__ == '__main__' :
	main()
