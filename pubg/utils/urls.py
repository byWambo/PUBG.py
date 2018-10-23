class URLS:

    player_season = "https://api.pubg.com/shards/{shard}/seasons"
    player_stats = "https://api.pubg.com/shards/{shard}/players?filter[playerNames]={player_name}"
    season_stats = "https://api.pubg.com/shards/{shard}/players/{player_id}/seasons/{season_name}"
    get_match = "https://api.pubg.com/shards/{shard}/matches/{match_id}"
    get_tournament = "https://api.pubg.com/tournaments/{tournament_id}"
