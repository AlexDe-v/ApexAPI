import apex

apex.token = "TOKEN"

map_rotation = apex.get_maps() # Does not require a token, returns JSON object

current_map = map_rotation['battle_royale']['current']['map']
current_map_end = map_rotation['battle_royale']['current']['remainingTimer']

next_map = map_rotation['rotation']['battle_royale']['next']['map']


print(f'Current map {current_map} will end in {current_map_end} and next is {next_map}!')


# Example JSON response:
"""
{
    "bannerPath": "https:\/\/lil2-gateway.apexlegendsstatus.com\/maps\/a04c6b41a3a67c14d9099d843fa776cc.png",
    "rotation": {
        "battle_royale": {
            "current": {
                "start": 1681567200,
                "end": 1681572600,
                "readableDate_start": "2023-04-15 14:00:00",
                "readableDate_end": "2023-04-15 15:30:00",
                "map": "Storm Point",
                "code": "storm_point_rotation",
                "DurationInSecs": 5400,
                "DurationInMinutes": 90,
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Storm_Point.png",
                "remainingSecs": 5033,
                "remainingMins": 84,
                "remainingTimer": "01:23:53"
            },
            "next": {
                "start": 1681572600,
                "end": 1681578000,
                "readableDate_start": "2023-04-15 15:30:00",
                "readableDate_end": "2023-04-15 17:00:00",
                "map": "Broken Moon",
                "code": "broken_moon_rotation",
                "DurationInSecs": 5400,
                "DurationInMinutes": 90,
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Broken_Moon.png"
            }
        },
        "arenas": {
            "current": {
                "start": 1681567200,
                "end": 1681568100,
                "readableDate_start": "2023-04-15 14:00:00",
                "readableDate_end": "2023-04-15 14:15:00",
                "map": "Habitat",
                "code": "arenas_habitat",
                "DurationInSecs": 900,
                "DurationInMinutes": 15,
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Arena_Habitat.png",
                "remainingSecs": 533,
                "remainingMins": 9,
                "remainingTimer": "00:08:53"
            },
            "next": {
                "start": 1681568100,
                "end": 1681569000,
                "readableDate_start": "2023-04-15 14:15:00",
                "readableDate_end": "2023-04-15 14:30:00",
                "map": "Drop Off",
                "code": "arenas_composite",
                "DurationInSecs": 900,
                "DurationInMinutes": 15,
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Arenas_Dropoff.png"
            }
        },
        "ranked": {
            "current": {
                "start": 1681491600,
                "end": 1681578000,
                "readableDate_start": "2023-04-14 17:00:00",
                "readableDate_end": "2023-04-15 17:00:00",
                "map": "Broken Moon",
                "code": "broken_moon_rotation",
                "DurationInSecs": 86400,
                "DurationInMinutes": 1440,
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Broken_Moon.png",
                "remainingSecs": 10433,
                "remainingMins": 174,
                "remainingTimer": "02:53:53"
            },
            "next": {
                "start": 1681578000,
                "end": 1681664400,
                "readableDate_start": "2023-04-15 17:00:00",
                "readableDate_end": "2023-04-16 17:00:00",
                "map": "Olympus",
                "code": "olympus_rotation",
                "DurationInSecs": 86400,
                "DurationInMinutes": 1440,
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Olympus.png"
            }
        },
        "arenasRanked": {
            "current": {
                "start": 1681567200,
                "end": 1681568100,
                "readableDate_start": "2023-04-15 14:00:00",
                "readableDate_end": "2023-04-15 14:15:00",
                "map": "Habitat",
                "code": "arenas_habitat",
                "DurationInSecs": 900,
                "DurationInMinutes": 15,
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Arena_Habitat.png",
                "remainingSecs": 533,
                "remainingMins": 9,
                "remainingTimer": "00:08:53"
            },
            "next": {
                "start": 1681568100,
                "end": 1681569000,
                "readableDate_start": "2023-04-15 14:15:00",
                "readableDate_end": "2023-04-15 14:30:00",
                "map": "Drop Off",
                "code": "arenas_composite",
                "DurationInSecs": 900,
                "DurationInMinutes": 15,
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/Arenas_Dropoff.png"
            }
        },
        "ltm": {
            "current": {
                "start": 1681567200,
                "end": 1681568100,
                "readableDate_start": "2023-04-15 14:00:00",
                "readableDate_end": "2023-04-15 14:15:00",
                "map": "Barometer",
                "code": "control_tropics_barometer",
                "DurationInSecs": 900,
                "DurationInMinutes": 15,
                "isActive": true,
                "eventName": "Control",
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/",
                "remainingSecs": 533,
                "remainingMins": 9,
                "remainingTimer": "00:08:53"
            },
            "next": {
                "start": 1681568100,
                "end": 1681569000,
                "readableDate_start": "2023-04-15 14:15:00",
                "readableDate_end": "2023-04-15 14:30:00",
                "map": "Skulltown",
                "code": "freedm_tdm_skulltown",
                "DurationInSecs": 900,
                "DurationInMinutes": 15,
                "isActive": true,
                "eventName": "TDM",
                "asset": "https:\/\/apexlegendsstatus.com\/assets\/maps\/"
            }
        }
    }
}"""