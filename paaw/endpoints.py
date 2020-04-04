"""List of API endpoints."""

# flake8: noqa
# fmt: off

API_PATH = {
    "token":                                    "https://api.afl.com.au/cfs/afl/WMCTok",
    "broadcast_regions":                        "https://aflapi.afl.com.au/broadcasting/regions", # ?page=0&pageSize=100    
    "competitions":                             "https://aflapi.afl.com.au/afl/v2/competitions",
    "competition_seasons":                      "https://aflapi.afl.com.au/afl/v2/competitions/1/compseasons",
    "competition_season_rounds":                "https://aflapi.afl.com.au/afl/v2/compseasons", # /20/rounds?roundNumber=1&    
    "competition_season_teams":                 "https://aflapi.afl.com.au/afl/v2/teams", # ?compSeasonId=20&pageSize=100
    "competition_season_venues":                "https://aflapi.afl.com.au/afl/v2/venues", # ?compSeasonId=20&pageSize=100
    "competition_season_matches":               "https://aflapi.afl.com.au/afl/v2/matches", # ?competitionId=1&compSeasonId=20&pageSize=50&roundNumber=1
    "competition_season_ladder":                "https://aflapi.afl.com.au/afl/v2/compseasons", # /20/ladders
    "competition_season_player_statistics":     "https://api.afl.com.au/statspro/playersStats/seasons", # /CD_S2020014
    "statistics_reference":                     "https://api.afl.com.au/statspro/statsConfig",
    "clubs":                                    "https://api.afl.com.au/cfs/afl/clubs",
    "team_season_statistics":                   "https://api.afl.com.au/cfs/afl/statsCentre/teams", # ?competitionId=CD_S2020014
    "team_season_round_statistics":             "https://api.afl.com.au/cfs/afl/statsCentre/teams", # ?competitionId=CD_S2020014&roundId=CD_R202001401
    "player_profile":                           "https://api.afl.com.au/statspro/playerProfile", # /CD_I290528?CD_S2020014
    "player_statistics":                        "https://api.afl.com.au/statspro/playerCareerSeasonStats", # /CD_I290528
    "player_season_statistics":                 "https://api.afl.com.au/statspro/playerSeasonRoundStats", # /CD_I290528?seasonId=CD_S2017014
    "player_video_highlights":                  "https://api.afl.com.au/statspro/playerHighlights/player", # /CD_I290528
    "player_season_heatmaps":                   "https://api.afl.com.au/cfs/afl/coach/match", # /CD_M20200140109/playerSeasonHeatmaps
}