from Bunker_cards import professions, phobias, hobbies, character_traits, \
    health_conditions, additional_info, \
    action_cards, baggage_items, sexes, Useful_bunker, Useless_bunker, Funny_bunker, \
    Catastrophe
    
import random, os



class Player():
    def __init__(self, name):
        self.name = name
        self.sex = random.choice(sexes)
        self.age = random.randint(18, 80)
        self.hobby_exp = random.randint(0, self.age//3)
        self.job_exp = random.randint(0, self.age//2)

        self.selected_baggage = random.choice(baggage_items)
        baggage_items.remove(self.selected_baggage)

        self.selected_profession = random.choice(professions)
        professions.remove(self.selected_profession)

        self.selected_phobia = random.choice(phobias)
        phobias.remove(self.selected_phobia)

        self.selected_hobby = random.choice(hobbies)
        hobbies.remove(self.selected_hobby)

        self.selected_trait = random.choice(character_traits)
        character_traits.remove(self.selected_trait)

        self.selected_health = random.choice(health_conditions)
        health_conditions.remove(self.selected_health)

        self.selected_info = random.choice(additional_info)
        additional_info.remove(self.selected_info)

        self.selected_card1 = random.choice(action_cards)
        action_cards.remove(self.selected_card1)

        self.selected_card2 = random.choice(action_cards)
        action_cards.remove(self.selected_card2)

    def stats(self):
        print(f"{player_number}. Hello {self.name}!")
        print(f"You are a {self.age} year old {self.sex}!")
        print()
        print(f"Your Profession: {self.selected_profession} with {self.job_exp} years of experience")
        print("Your Baggage: ", self.selected_baggage)
        print("Your Phobia: ", self.selected_phobia)
        print(f"Your Hobby: {self.selected_hobby} with {self.hobby_exp} years of experience")
        print("Your Trait: ", self.selected_trait)
        print("Your Health Condition: ", self.selected_health)
        print("Your Additional Info: ", self.selected_info)
        print("Your Action Card 1: ", self.selected_card1)
        print("Your Action Card 2: ", self.selected_card2)

class Game():
    def __init__(self, difficulty):
        self.difficulty = difficulty

        self.catastrophe = random.choice(Catastrophe)
        Catastrophe.remove(self.catastrophe)

        if difficulty == "easy":
            self.useful1 = random.choice(Useful_bunker)
            Useful_bunker.remove(self.useful1)
            self.useful2 = random.choice(Useful_bunker)
            Useful_bunker.remove(self.useful2)
            self.useful3 = random.choice(Useful_bunker)
            Useful_bunker.remove(self.useful3)

            self.useless1 = random.choice(Useless_bunker)
            Useless_bunker.remove(self.useless1)
            self.useless2 = random.choice(Useless_bunker)
            Useless_bunker.remove(self.useless2)

            self.funny1 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny1)
            self.funny2 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny2)
            self.funny3 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny3)
        elif difficulty == "normal":
            self.useful1 = random.choice(Useful_bunker)
            Useful_bunker.remove(self.useful1)
            self.useful2 = random.choice(Useful_bunker)
            Useful_bunker.remove(self.useful2)

            self.useless1 = random.choice(Useless_bunker)
            Useless_bunker.remove(self.useless1)

            self.funny1 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny1)
            self.funny2 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny2)
            self.funny3 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny3)
        elif difficulty == "hard":
            self.useful1 = random.choice(Useful_bunker)
            Useful_bunker.remove(self.useful1)

            self.useless1 = random.choice(Useless_bunker)
            Useless_bunker.remove(self.useless1)

            self.funny1 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny1)
            self.funny2 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny2)
            self.funny3 = random.choice(Funny_bunker)
            Funny_bunker.remove(self.funny3)
    




New_players = ['Artem', 'Marina', 'Rita', 'Maria', 'Nick']
player_number = 1

Players = []

for guest in New_players:
    profile = Player(guest)
    profile.stats()
    profile.number = player_number
    player_number += 1
    print()
    print()
    Players.append(profile)
    
for player_used in Players:
    if os.path.exists(player_used.name):
        os.remove(player_used.name)
running = True

for player_used in Players:
    f = open(player_used.name, "x")

    f.write(f"Hello {player_used.name}!\n")
    f.write(f"You are a {player_used.age} year old {player_used.sex}!\n")
    f.write(f"Your Profession: {player_used.selected_profession} with {player_used.job_exp} years of experience\n")
    f.write(f"Your Baggage: {player_used.selected_baggage}\n")
    f.write(f"Your Phobia: {player_used.selected_phobia}\n")
    f.write(f"Your Hobby: {player_used.selected_hobby} with {-player_used.hobby_exp} years of experience\n")
    f.write(f"Your Trait: {player_used.selected_trait}\n")
    f.write(f"Your Health Condition: {player_used.selected_health}\n")
    f.write(f"Your Additional Info: {player_used.selected_info}\n")
    f.write(f"Your Action Card 1: {player_used.selected_card1}\n")
    f.write(f"Your Action Card 2: {player_used.selected_card2}\n")
    
    f.close()


while running:

    set_difficulty = input("What difficulty do you want to play? easy/normal/hard ")
    Bunker = Game(set_difficulty)
    print(f"Hello, players. Today's catastrophe is {Bunker.catastrophe}")

    card_type = input("What type of a card is being used? one/all ")
    
    if card_type == "one":
        used_card = int(input("What player has used the card? "))
        player_used = Players[used_card - 1]
        f = open(player_used.name, "a")
        stat = input("What characteristic is being rerolled? prof/baggage/phobia/hobby/health/info/(sex/age) ")
        if stat == "prof":
            player_used.selected_profession = random.choice(professions)
            print(f"{player_used.name}: {player_used.selected_profession}\n")
            f.write(f"Your NEW Profession: {player_used.selected_profession}\n")
             
        elif stat == "baggage":
            player_used.selected_baggage = random.choice(baggage_items)
            print(f"{player_used.name}: {player_used.selected_baggage}\n")
            f.write(f"Your NEW Baggage: {player_used.selected_baggage}\n")
        elif stat == "phobia":
            player_used.selected_phobia = random.choice(phobias)
            print(f"{player_used.name}: {player_used.selected_phobia}\n")
            f.write(f"Your NEW Phobia: {player_used.selected_phobia}\n")
        elif stat == "hobby":
            player_used.selected_hobby = random.choice(hobbies)
            print(f"{player_used.name}: {player_used.selected_hobby}\n")
            f.write(f"Your NEW Hobby: {player_used.selected_hobby}\n")
        elif stat == "health":
            player_used.selected_health = random.choice(health_conditions)
            print(f"{player_used.name}: {player_used.selected_health}\n")
            f.write(f"Your NEW Health Condition: {player_used.selected_health}\n")
        elif stat == "info":
            player_used.selected_info = random.choice(additional_info)
            print(f"{player_used.name}: {player_used.selected_info}\n")
            f.write(f"Your NEW Additional Info: {player_used.selected_info}\n")
        elif stat == "sex/age":
            player_used.sex = random.choice(sexes)
            print(f"{player_used.name}: {player_used.sex}\n")
            f.write(f"Your NEW Sex: {player_used.sex}\n")
            player_used.age = random.randint(18, 80)
            print(f"{player_used.name}: {player_used.age} years old\n")
            f.write(f"Your NEW Age: {player_used.age}\n")
        f.close()
    
    elif card_type == "all":
        stat = input("What characteristic is being rerolled? prof/baggage/phobia/hobby/health/info ")
        for player_used in Players:
            f = open(player_used.name, "a")
            if stat == "prof":
                player_used.selected_profession = random.choice(professions)
                print(f"{player_used.name}: {player_used.selected_profession}\n")
                f.write(f"Your NEW Profession: {player_used.selected_profession}\n")
            elif stat == "baggage":
                player_used.selected_baggage = random.choice(baggage_items)
                print(f"{player_used.name}: {player_used.selected_baggage}\n")
                f.write(f"Your NEW Baggage: {player_used.selected_baggage}\n")
            elif stat == "phobia":
                player_used.selected_phobia = random.choice(phobias)
                print(f"{player_used.name}: {player_used.selected_phobia}\n")
                f.write(f"Your NEW Phobia: {player_used.selected_phobia}\n")
            elif stat == "hobby":
                player_used.selected_hobby = random.choice(hobbies)
                print(f"{player_used.name}: {player_used.selected_hobby}\n")
                f.write(f"Your NEW Hobby: {player_used.selected_hobby}\n")
            elif stat == "health":
                player_used.selected_health = random.choice(health_conditions)
                print(f"{player_used.name}: {player_used.selected_health}")
                f.write(f"Your NEW Health Condition: {player_used.selected_health}\n")
            elif stat == "info":
                player_used.selected_info = random.choice(additional_info)
                print(f"{player_used.name}: {player_used.selected_info}\n")
                f.write(f"Your NEW Additional Info: {player_used.selected_info}\n")
            elif stat == "sex/age":
                player_used.sex = random.choice(sexes)
                print(f"{player_used.name}: {player_used.sex}\n")
                f.write(f"Your NEW Sex: {player_used.sex}\n")
                player_used.age = random.randint(18, 80)
                print(f"{player_used.name}: {player_used.age} years old\n")
                f.write(f"Your NEW Age: {player_used.age}\n")
            f.close()

