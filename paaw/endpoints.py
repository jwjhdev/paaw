"""List of API endpoints."""

# flake8: noqa
# fmt: off

API_PATH = {
    "token":                                    "/cfs/afl/WMCTok",
    "broadcast_regions":                        "/broadcasting/regions",
    "competitions":                             "/afl/v2/competitions",
    "competition_seasons":                      "/afl/v2/competitions/1/compseasons",
    "competition_season_rounds":                "/afl/v2/compseasons",
    "competition_season_teams":                 "/afl/v2/teams",
    "competition_season_venues":                "/afl/v2/venues",
    "competition_season_matches":               "/afl/v2/matches",
    "competition_season_ladder":                "/afl/v2/compseasons",
    "competition_season_player_statistics":     "/statspro/playersStats/seasons",
    "statistics_reference":                     "/statspro/statsConfig",
    "clubs":                                    "/cfs/afl/clubs",
    "team_season_statistics":                   "/cfs/afl/statsCentre/teams",
    "team_season_round_statistics":             "/cfs/afl/statsCentre/teams",
    "player_profile":                           "/statspro/playerProfile",
    "player_statistics":                        "/statspro/playerCareerSeasonStats",
    "player_season_statistics":                 "/statspro/playerSeasonRoundStats",
    "player_video_highlights":                  "/statspro/playerHighlights/player",
    "player_season_heatmaps":                   "/cfs/afl/coach/match",
}
