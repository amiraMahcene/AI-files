import random

def kickoff():
    print("Welcome to Python Football!")
    team1 = input("Enter the name of Team 1: ")
    team2 = input("Enter the name of Team 2: ")
    
    score1 = 0
    score2 = 0
    
    for minute in range(1, 91, 5):  # Simulating 90 minutes, updating every 5 minutes
        print(f"Minute {minute}...")
        if random.random() < 0.2:  # 20% chance of a goal every 5 minutes
            scoring_team = random.choice([team1, team2])
            if scoring_team == team1:
                score1 += 1
            else:
                score2 += 1
            print(f"GOAL! {scoring_team} scores!")
    
    print("Full Time!")
    print(f"Final Score: {team1} {score1} - {score2} {team2}")
    if score1 > score2:
        print(f"{team1} wins!")
    elif score2 > score1:
        print(f"{team2} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    kickoff()