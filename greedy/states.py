states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

def find_better_station(stations: dict, states: set) -> list: 
    covered: set = set()
    appended_stations: set = set()

    while covered != states:
        biggest: int = 0
        for station in stations.keys():
            counter: int = 0
            for state in stations[station]:
                if state not in covered:
                    counter += 1
            if counter > biggest:
                better = station
                biggest = counter
        covered.update(stations[better])
        appended_stations.add(better)


    return appended_stations
    
print(find_better_station(stations, states))