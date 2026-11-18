import json
try:
    with open("settings.json", "r") as file:
        saved_settings = json.load(file)
except FileNotFoundError:
    saved_settings = {"artists": [], "seen_ids": []}

artists = saved_settings["artists"]
seen_ids = saved_settings.get("seen_ids", [])

city = input("What city should I track for these artists? ")
new_artist = input("Add another artist:")
if new_artist and new_artist not in artists:
    artists.append(new_artist)
settings = {"city": city, "artists": artists, "seen_ids": seen_ids}

with open("sample_events.json", "r") as file:
    events = json.load(file)

new_matches = 0
for event in events:
    if event["artist"] in artists and event["city"] == city and event["id"] not in seen_ids:
       print(f"New match: {event['artist']} in {event['city']} on {event['date']} at {event['venue']}")
       seen_ids.append(event["id"])
       new_matches += 1


if new_matches == 0:
    print("No new matching events.")


print("Artists I'm Tracking:")
for artist in artists:
    print(f"Tracking {artist} in {city}")

with open("settings.json", "w") as file:
    json.dump(settings, file, indent=2)