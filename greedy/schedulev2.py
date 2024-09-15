schedule = {}
stack = []

#        CLASSES    
schedule["arts"] = {}
schedule["arts"]["start"] = 9
schedule["arts"]["end"] = 10

schedule["english"] = {}
schedule["english"]["start"] = 9.30
schedule["english"]["end"] = 10.30

schedule["math"] = {}
schedule["math"]["start"] = 10
schedule["math"]["end"] = 11

schedule["cs"] = {}
schedule["cs"]["start"] = 10.30
schedule["cs"]["end"] = 11.30

schedule["music"] = {}
schedule["music"]["start"] = 11
schedule["music"]["end"] = 12
  

def find_smaller_end(schedule, processed):
    min = float("inf")
    min_elm = None
    min_name = None
    last_end = processed[-1][list(processed[-1].keys())[0]]["end"] if processed else float("-inf")
    
    for aula in schedule:
        if aula not in [list(p.keys())[0] for p in processed]:
            if schedule[aula]["end"] < min and schedule[aula]["start"] >= last_end:
                min = schedule[aula]["end"]
                min_elm = schedule[aula]
                min_name = aula
    return {min_name: min_elm} if min_elm else None

def find_smallest_end(schedule):
    min = float("inf")
    min_elm = None
    min_name = None
    
    for aula in schedule:
        if schedule[aula]["end"] < min:
            min = schedule[aula]["end"]
            min_elm = schedule[aula]
            min_name = aula
    return {min_name: min_elm}

def greedy(schedule):   
    processed = []
    min = 0

    processed.append(find_smallest_end(schedule))

    while min is not None:
        min = find_smaller_end(schedule, processed)
        if min is not None:
            processed.append(min)

    return processed
    
print(greedy(schedule))