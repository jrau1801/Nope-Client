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

    def get_tournament_url(self, tunier_id):
        """Get the URL for a tournament's information."""
        return self._tournament_url.format(tunier_id=tunier_id)

    def get_tournament_stats_url(self, tunier_id):
        """Get the URL for tournament statistics."""
        return self._tournament_stats_url.format(tunier_id=tunier_id)

    def get_match_url(self, match_id):
        """Get the URL for a match's information."""
        return self._match_url.format(match_id=match_id)

    def get_game_url(self, game_id):
        """Get the URL for a game's information."""
        return self._game_url.format(game_id=game_id)


# Usage example:
api = PlayerAPI()

player_url = api.get_player_stats_url('Jan2')
print(player_url)
player_url = api.get_player_stats_url('Jan')
print(player_url)
