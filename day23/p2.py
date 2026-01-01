import sys
from collections import defaultdict
from heapq import heappop, heappush


DOOR = [2, 4, 6, 8]
HALL_STOPS = [0, 1, 3, 5, 7, 9, 10]
ROOM_IDX = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
TARGET = (('A', 'A', 'A', 'A'), ('B', 'B', 'B', 'B'), ('C', 'C', 'C', 'C'), ('D', 'D', 'D', 'D'))

def main():
    data = open(sys.argv[1]).read().splitlines()

    hall_start = ('.',) * 11
    rooms_start = (
        (data[2][3], 'D', 'D', data[3][3]),
        (data[2][5], 'C', 'B', data[3][5]),
        (data[2][7], 'B', 'A', data[3][7]),
        (data[2][9], 'A', 'C', data[3][9]),
    )
    start = (hall_start, rooms_start)

    cost = defaultdict(lambda: float('inf'))
    cost[start] = 0
    pq = [(0, start)]

    while pq:
        cur_cost, cur_state = heappop(pq)
        cur_hall, cur_rooms = cur_state

        if cur_rooms == TARGET:
            print(cur_cost)
            break

        if cur_cost > cost[cur_state]:
            continue

        moves = []

        # 1) Move from hall to room
        for hpos in HALL_STOPS:
            amphipod = cur_hall[hpos]
            if amphipod == '.':
                continue

            ridx = ROOM_IDX[amphipod]
            room = cur_rooms[ridx]

            if '.' not in room:
                continue
            if any(x not in ('.', amphipod) for x in room):
                continue

            door_pos = DOOR[ridx]
            step = 1 if hpos < door_pos else -1

            if any(cur_hall[pos] != '.' for pos in range(hpos + step, door_pos + step, step)):
                continue

            depth = 3 if room[3] == '.' else 2 if room[2] == '.' else 1 if room[1] == '.' else 0
            steps = abs(hpos - door_pos) + depth + 1
            new_cost = cur_cost + steps * COST[amphipod]

            new_hall = list(cur_hall)
            new_hall[hpos] = '.'
            new_rooms = [list(r) for r in cur_rooms]
            new_rooms[ridx][depth] = amphipod
            new_state = (tuple(new_hall), tuple(tuple(r) for r in new_rooms))
            moves.append((new_cost, new_state))

        if moves:
            for new_cost, new_state in moves:
                if new_cost < cost[new_state]:
                    cost[new_state] = new_cost
                    heappush(pq, (new_cost, new_state))
            continue

        # 2) Move from room to hall
        for ridx, room in enumerate(cur_rooms):
            if all(x == '.' for x in room):
                continue

            depth = 0 if room[0] != '.' else 1 if room[1] != '.' else 2 if room[2] != '.' else 3
            amphipod = room[depth]

            if ROOM_IDX[amphipod] == ridx and all(x == amphipod for x in room[depth:]):
                continue

            door_pos = DOOR[ridx]
            for hpos in HALL_STOPS:
                step = 1 if door_pos < hpos else -1
                if any(cur_hall[pos] != '.' for pos in range(door_pos + step, hpos + step, step)):
                    continue

                steps = abs(hpos - door_pos) + depth + 1
                new_cost = cur_cost + steps * COST[amphipod]

                new_hall = list(cur_hall)
                new_hall[hpos] = amphipod
                new_rooms = [list(r) for r in cur_rooms]
                new_rooms[ridx][depth] = '.'
                new_state = (tuple(new_hall), tuple(tuple(r) for r in new_rooms))

                if new_cost < cost[new_state]:
                    cost[new_state] = new_cost
                    heappush(pq, (new_cost, new_state))


if __name__ == '__main__':
    main()
