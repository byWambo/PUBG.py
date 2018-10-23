import pubg

class URL:

    def __init__(self, url, shard=None, player_id=None, player_name=None,season_name=None, match_id=None, tournament_id=None):

        self.url = url
        self._url = None

        if shard:
            self.shard = shard
        if player_id:
            self.player_id = player_id
        if season_name:
            self.season_name = season_name
        if match_id:
            self.match_id = match_id
        if tournament_id:
            self.tournament_id = tournament_id
        if player_name:
            self.player_name = player_name

    def link(self):
        if self.url == pubg.urls.URLS.get_tournament:
            self._url = self.url.format(tournament_id=self.tournament_id)
            return self._url
        if self.url == pubg.urls.URLS.player_stats:
            self._url = self.url.format(shard=self.shard, player_name=self.player_name)
            print(self._url)
            return self._url
        else:
            return
