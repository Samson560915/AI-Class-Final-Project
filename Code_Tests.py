from Determine_Path import add_path, del_path, check_paths
from Utils import get_points
from Searches import weighted_local
from Draw import get_paths

def test_one(start_lim = 0):
    limit = start_lim
    min_utility = float('inf')
    best_limit = 0
    for i in range(30):
        avr_utility = 0
        for i in range(20):
            points = get_points(20)
            nodes = weighted_local(points)
            paths = get_paths(nodes)
            should_add = True
            should_del = True
            count = 0
            while (should_add or should_del) and count < len(nodes)*4:
                if should_add:
                    upper = add_path(nodes)
                if should_del:
                    lower = del_path(nodes)
                if upper <= limit:
                    should_add = False
                else:
                    should_add = True
                if lower >= limit:
                    should_del = False
                else:
                    should_del = True
                count+=1
            avr_priority = 0
            test = check_paths(nodes)
            for p in test:
                avr_priority += -p[0]
            paths = get_paths(nodes)
            distance = 0
            for path in paths:
                distance += ((path[0][0] - path[1][0]) ** 2 + (path[0][1]-path[1][1])**2) ** 0.5
            avr_priority /= len(test)
            utility = distance * avr_priority
            avr_utility += utility
            print(f"{utility}, {avr_priority}, {distance}")
        avr_utility /= 20
        if avr_utility < min_utility:
            min_utility = avr_utility
            best_limit = limit
        limit += 0.1
    print(min_utility, best_limit)

def test_two(start_lim = 0):
    limit = start_lim
    min_utility = float('inf')
    min_distance = float('inf')
    min_priority = float('inf')
    best_limit_utility = 0
    best_limit_distance = 0
    best_limit_priority = 0
    for i in range(30):
        avr_utility = 0
        total_distance = 0
        total_priority = 0
        for i in range(20):
            points = get_points(20)
            nodes = weighted_local(points)
            paths = get_paths(nodes)
            should_add = True
            should_del = True
            count = 0
            while (should_add or should_del) and count < len(nodes)*4:
                if should_add:
                    upper = add_path(nodes)
                if should_del:
                    lower = del_path(nodes)
                if upper <= limit:
                    should_add = False
                else:
                    should_add = True
                if lower >= limit:
                    should_del = False
                else:
                    should_del = True
                count+=1
            avr_priority = 0
            test = check_paths(nodes)
            for p in test:
                avr_priority += -p[0]
            paths = get_paths(nodes)
            distance = 0
            for path in paths:
                distance += ((path[0][0] - path[1][0]) ** 2 + (path[0][1]-path[1][1])**2) ** 0.5
            avr_priority /= len(test)
            utility = distance * (avr_priority-1)*10
            avr_utility += utility
            total_distance += distance
            total_priority += avr_priority
            print(f"{utility}, {avr_priority}, {distance}")
        avr_utility /= 20
        if avr_utility < min_utility:
            min_utility = avr_utility
            best_limit_utility = limit
        if total_distance < min_distance:
            min_distance = total_distance
            best_limit_distance = limit
        if total_priority < min_priority:
            min_priority = total_priority
            best_limit_priority = limit
        limit += 0.1
    print(min_utility, best_limit_utility)
    print(min_distance, best_limit_distance)
    print(min_priority, best_limit_priority)

