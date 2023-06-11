class PlayerAPI:
    """
    Class representing the API endpoints for player-related information.
    """

    def __init__(self):
        """
        Initialize Rest-API Endpoints
        """
        self._player_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}'
        self._player_stats_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/stats'
        self._player_tournament_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/tournaments'
        self._player_tournaments_won_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/tournaments/won'
        self._player_tournaments_hosted_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/tournaments/hosted'
        self._player_tournaments_stats_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/tournaments/statistics'
        self._player_matches_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/matches'
        self._player_matches_won_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/matches/won'
        self._player_games_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/games'
        self._player_games_won_url = 'https://nope-server.azurewebsites.net/api/player/{spielername}/games/won'

        self._tournament_url = 'https://nope-server.azurewebsites.net/api/tournament/{tunier_id}'
        self._tournament_stats_url = 'https://nope-server.azurewebsites.net/api/tournament/{tunier_id}/statistic'

        self._match_url = 'https://nope-server.azurewebsites.net/api/match/{match_id}'

        self._game_url = 'https://nope-server.azurewebsites.net/api/game/{game_id}'

        self._docs_url = "https://nope-server.azurewebsites.net/docs/"

    def get_player_url(self, spielername):
        """Get the URL for a player's information."""
        return self._player_url.format(spielername=spielername)

    def get_player_stats_url(self, spielername):
        """Get the URL for a player's statistics."""
        return self._player_stats_url.format(spielername=spielername)

    def get_player_tournament_url(self, spielername):
        """Get the URL for a player's tournaments."""
        return self._player_tournament_url.format(spielername=spielername)

    def get_player_tournaments_won_url(self, spielername):
        """Get the URL for tournaments won by a player."""
        return self._player_tournaments_won_url.format(spielername=spielername)

    def get_player_tournaments_hosted_url(self, spielername):
        """Get the URL for tournaments hosted by a player."""
        return self._player_tournaments_hosted_url.format(spielername=spielername)

    def get_player_tournaments_stats_url(self, spielername):
        """Get the URL for tournament statistics of a player."""
        return self._player_tournaments_stats_url.format(spielername=spielername)

    def get_player_matches_url(self, spielername):
        """Get the URL for matches played by a player."""
        return self._player_matches_url.format(spielername=spielername)

    def get_player_matches_won_url(self, spielername):
        """Get the URL for matches won by a player."""
        return self._player_matches_won_url.format(spielername=spielername)

    def get_player_games_url(self, spielername):
        """Get the URL for games played by a player."""
        return self._player_games_url.format(spielername=spielername)

    def get_player_games_won_url(self, spielername):
        """Get the URL for games won by a player."""
        return self._player_games_won_url.format(spielername=spielername)

    def get_tournament_url(self, turnier_id):
        """Get the URL for a tournament's information."""
        return self._tournament_url.format(tunier_id=turnier_id)

    def get_tournament_stats_url(self, turnier_id):
        """Get the URL for tournament statistics."""
        return self._tournament_stats_url.format(tunier_id=turnier_id)

    def get_match_url(self, match_id):
        """Get the URL for a match's information."""
        return self._match_url.format(match_id=match_id)

    def get_game_url(self, game_id):
        """Get the URL for a game's information."""
        return self._game_url.format(game_id=game_id)

    def get_docs_url(self):
        """Get the URL for the Rest-API Documentation"""
        return self._docs_url


api = PlayerAPI()

# Prompt the user for input
while True:

    api = PlayerAPI()

    # Prompt the user for input
    generated_url = ""
    spielername = input("Enter the player's name: ")
    url_choice = input("\nEnter the number corresponding to the URL you want to generate:\n"
                       "1. Player Information\n"
                       "2. Player Statistics\n"
                       "3. Player Tournaments\n"
                       "4. Tournaments Won by Player\n"
                       "5. Tournaments Hosted by Player\n"
                       "6. Player Tournament Statistics\n"
                       "7. Matches Played by Player\n"
                       "8. Matches Won by Player\n"
                       "9. Games Played by Player\n"
                       "10. Games Won by Player\n"
                       "11. Tournament Information\n"
                       "12. Tournament Statistics\n"
                       "13. Match Information\n"
                       "14. Game Information\n"
                       "15. API Documentation\n"
                       "Enter your choice: ")

    # Generate the desired URL based on the user's choice
    if url_choice == "1":
        generated_url = api.get_player_url(spielername)
    elif url_choice == "2":
        generated_url = api.get_player_stats_url(spielername)
    elif url_choice == "3":
        generated_url = api.get_player_tournament_url(spielername)
    elif url_choice == "4":
        generated_url = api.get_player_tournaments_won_url(spielername)
    elif url_choice == "5":
        generated_url = api.get_player_tournaments_hosted_url(spielername)
    elif url_choice == "6":
        generated_url = api.get_player_tournaments_stats_url(spielername)
    elif url_choice == "7":
        generated_url = api.get_player_matches_url(spielername)
    elif url_choice == "8":
        generated_url = api.get_player_matches_won_url(spielername)
    elif url_choice == "9":
        generated_url = api.get_player_games_url(spielername)
    elif url_choice == "10":
        generated_url = api.get_player_games_won_url(spielername)
    elif url_choice == "11":
        turnier_id = input("Enter the tournament ID: ")
        generated_url = api.get_tournament_url(turnier_id)
    elif url_choice == "12":
        turnier_id = input("Enter the tournament ID: ")
        generated_url = api.get_tournament_stats_url(turnier_id)
    elif url_choice == "13":
        match_id = input("Enter the match ID: ")
        generated_url = api.get_match_url(match_id)
    elif url_choice == "14":
        game_id = input("Enter the game ID: ")
        generated_url = api.get_game_url(game_id)
    elif url_choice == "15":
        generated_url = api.get_docs_url()
    else:
        print("Invalid choice!")

    # Print the generated URL
    print(f"\nGenerated URL: {generated_url}\n")
