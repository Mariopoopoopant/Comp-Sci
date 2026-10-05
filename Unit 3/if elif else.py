team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A Win!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B Win!")
    team_b_wins += 1
else: 
    print("Tie!")


if team_a_wins > team_b_wins:
    print("Team A has more wins then Team B")
elif team_b_wins > team_a_wins:
    print("Team B has more wins then Team A")
else:
    print("Both Teams A and B have the same number of wins.")