# Download map.png too

import random
import io
from PIL import Image, ImageDraw

states = [{"name": "Alabama", "status": "Republican", "electors": 9, "location": (650, 398)},
          {"name": "Alaska", "status": "Republican", "electors": 3, "location": (92, 510)},
          {"name": "Arizona", "status": "Swing", "electors": 11, "location": (201, 367)},
          {"name": "Arkansas", "status": "Republican", "electors": 6, "location": (559, 357)},
          {"name": "California", "status": "Democratic", "electors": 54, "location": (85, 322)},
          {"name": "Colorado", "status": "Swing", "electors": 10, "location": (275, 256)},
          {"name": "Connecticut", "status": "Democratic", "electors": 7, "location": (852, 173)},
          {"name": "Delaware", "status": "Democratic", "electors": 3, "location": (828, 250)},
          {"name": "Florida", "status": "Swing", "electors": 30, "location": (752, 467)},
          {"name": "Georgia", "status": "Swing", "electors": 16, "location": (710, 393)},
          {"name": "Hawaii", "status": "Democratic", "electors": 4, "location": (331, 558)},
          {"name": "Idaho", "status": "Republican", "electors": 4, "location": (175, 121)},
          {"name": "Illinois", "status": "Democratic", "electors": 20, "location": (600, 258)},
          {"name": "Indiana", "status": "Republican", "electors": 11, "location": (651, 234)},
          {"name": "Iowa", "status": "Swing", "electors": 6, "location": (538, 219)},
          {"name": "Kansas", "status": "Republican", "electors": 6, "location": (465, 315)},
          {"name": "Kentucky", "status": "Republican", "electors": 8, "location": (660, 310)},
          {"name": "Louisiana", "status": "Republican", "electors": 8, "location": (539, 439)},
          {"name": "Maine-At-Large", "status": "Democratic", "electors": 2, "location": (887, 82)},
          {"name": "Maine-District 1", "status": "Democratic", "electors": 1, "location": (892, 113)},
          {"name": "Maine-District 2", "status": "Swing", "electors": 1, "location": (887, 58)},
          {"name": "Maryland", "status": "Democratic", "electors": 10, "location": (822, 257)},
          {"name": "Massachusetts", "status": "Democratic", "electors": 11, "location": (856, 157)},
          {"name": "Michigan", "status": "Swing", "electors": 15, "location": (673, 199)},
          {"name": "Minnesota", "status": "Swing", "electors": 10, "location": (495, 139)},
          {"name": "Mississippi", "status": "Republican", "electors": 6, "location": (603, 416)},
          {"name": "Missouri", "status": "Republican", "electors": 10, "location": (533, 295)},
          {"name": "Montana", "status": "Republican", "electors": 4, "location": (277, 78)},
          {"name": "Nebraska-At-Large", "status": "Republican", "electors": 2, "location": (414, 224)},
          {"name": "Nebraska-District 1", "status": "Republican", "electors": 1, "location": (462, 224)},
          {"name": "Nebraska-District 2", "status": "Swing", "electors": 1, "location": (476, 230)},
          {"name": "Nebraska-District 3", "status": "Republican", "electors": 1, "location": (442, 200)},
          {"name": "Nevada", "status": "Swing", "electors": 6, "location": (141, 213)},
          {"name": "New Hampshire", "status": "Swing", "electors": 4, "location": (864, 136)},
          {"name": "New Jersey", "status": "Democratic", "electors": 14, "location": (833, 226)},
          {"name": "New Mexico", "status": "Swing", "electors": 5, "location": (287, 397)},
          {"name": "New York", "status": "Democratic", "electors": 29, "location": (805, 138)},
          {"name": "North Carolina", "status": "Swing", "electors": 16, "location": (778, 329)},
          {"name": "North Dakota", "status": "Republican", "electors": 3, "location": (398, 107)},
          {"name": "Ohio", "status": "Swing", "electors": 17, "location": (684, 234)},
          {"name": "Oklahoma", "status": "Republican", "electors": 7, "location": (446, 375)},
          {"name": "Oregon", "status": "Democratic", "electors": 8, "location": (107, 114)},
          {"name": "Pennsylvania", "status": "Swing", "electors": 19, "location": (765, 205)},
          {"name": "Rhode Island", "status": "Democratic", "electors": 4, "location": (877, 172)},
          {"name": "South Carolina", "status": "Republican", "electors": 9, "location": (767, 377)},
          {"name": "South Dakota", "status": "Republican", "electors": 3, "location": (436, 152)},
          {"name": "Tennessee", "status": "Republican", "electors": 11, "location": (627, 347)},
          {"name": "Texas", "status": "Swing", "electors": 40, "location": (474, 474)},
          {"name": "Utah", "status": "Republican", "electors": 6, "location": (237, 237)},
          {"name": "Vermont", "status": "Democratic", "electors": 3, "location": (844, 116)},
          {"name": "Virginia", "status": "Swing", "electors": 13, "location": (802, 283)},
          {"name": "Washington", "status": "Democratic", "electors": 12, "location": (125, 56)},
          {"name": "Washington D.C.", "status": "Democratic", "electors": 3, "location": (803, 248)},
          {"name": "West Virginia", "status": "Republican", "electors": 5, "location": (784, 245)},
          {"name": "Wisconsin", "status": "Swing", "electors": 10, "location": (577, 169)},
          {"name": "Wyoming", "status": "Republican", "electors": 3, "location": (266, 166)}]
biden_states = ["California", "Oregon", "Washington", "Arizona", "New Mexico", "California", "Minnesota",
                "Wisconsin", "Illinois", "Michigan", "Georgia", "Pennsylvania", "Virginia", "Maryland",
                "Washington D.C.", "Delaware", "New Jersey", "New York", "Connecticut", "Rhode Island",
                "Massachusetts", "New Hampshire", "Vermont", "Maine-At-Large", "Hawaii", "Nevada", "Maine-District 1",
                "Nebraska-District 2", "Colorado"]

# Modes: Normal, Unrealistic, Landslide

print("Which election mode? Normal, Unrealistic, or Landslide are the only options.")
input = input()
if input in ["normal", "Normal"]:
    mode = "Normal"
    valid = True
elif input in ["unrealistic", "Unrealistic"]:
    mode = "Unrealistic"
    valid = True
elif input in ["landslide", "Landslide"]:
    mode = "Landslide"
    valid = True
    

def electiongenerator(mode):
    republican_states = []
    democrat_states = []
    landslide_victor = random.randint(1, 2)
    map = Image.open("scripts/Map.png").convert('RGB')
    democrat_color = (16, 48, 114)
    democrat_flip_color = (37, 93, 130)
    republican_color = (132, 17, 20)
    republican_flip_color = (191, 29, 41)
    if mode == "Normal":
        unrealistic = False
        landslide = False
    if mode == "Unrealistic":
        unrealistic = True
        landslide = False
    if mode == "Landslide":
        unrealistic = False
        landslide = True
    for state in states:
        name = state["name"]
        if name != "Nebraska-At-Large" or "Maine-At-Large":
            status = state["status"]
            if landslide is True:
                if landslide_victor == 1:
                    if status == "Swing":
                        status = "Republican"
                    elif status == "Democratic":
                        status = "Swing"
                elif landslide_victor == 2:
                    if status == "Swing":
                        status = "Democratic"
                    elif status == "Republican":
                        status = "Swing"
            elif unrealistic is True:
                unrealistic_victor = random.randint(1, 2)
                if unrealistic_victor == 1:
                    if status == "Swing":
                        status = "Republican"
                    elif status == "Democratic":
                        status = "Swing"
                elif unrealistic_victor == 2:
                    if status == "Swing":
                        status = "Democratic"
                    elif status == "Republican":
                        status = "Swing"
            if status == "Swing":
                coin_toss = random.randint(1, 2)
                if coin_toss == 1:
                    republican_states.append(name)
                elif coin_toss == 2:
                    democrat_states.append(name)
            elif status == "Republican":
                republican_states.append(name)
            elif status == "Democratic":
                democrat_states.append(name)
        state["color"] = (republican_color if state["name"] in republican_states else democrat_color)
    for state in states:
        ImageDraw.floodfill(map, xy=state["location"],
                            value=state["color"])
        if state["name"] in democrat_states:
            if state["name"] not in biden_states:
                ImageDraw.floodfill(map, xy=state["location"],
                                    value=democrat_flip_color)
            else:
                ImageDraw.floodfill(map, xy=state["location"],
                                    value=state["color"])
        elif state["name"] in republican_states:
            ImageDraw.floodfill(map, xy=state["location"],
                                value=state["color"])
            if state["name"] in biden_states:
                republican_states.remove(state["name"])
                republican_states.append("**"+state["name"]+"**")
                ImageDraw.floodfill(map, xy=state["location"],
                                    value=republican_flip_color)
    map.show()

if valid == True:
    electiongenerator(mode)
elif valid == False:
    print("Mode invalid. Your only options are Normal, Unrealistic, or Landslide. Did you spell one wrong?")