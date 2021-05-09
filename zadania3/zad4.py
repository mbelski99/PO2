def gen_time(start, stop, hop):
    czStart = list(start)
    czStop = list(stop)
    czHop = list(hop)

    start = (czStart[0], czStart[1], czStart[2])
    yield start

    while True:
        t_h = czStart[0] + czHop[0]
        t_min = czStart[1] + czHop[1]
        t_sec = czStart[2] + czHop[2]

        if t_h >= 24:
            czStart[0] = 0
        else:
            czStart[0] += czHop[0]

        if t_min >= 60:
            czStart[0] += 1
            czStart[1] = t_min - 60
        else:
            czStart[1] += czHop[1]

        if t_sec >= 60:
            czStart[1] += 1
            czStart[2] = t_sec - 60
        else:
            czStart[2] += czHop[2]


        start1 = (czStart[0], czStart[1], czStart[2])
        yield start1

        if czStart >= czStop:

                break


if __name__ == '__main__':

    for time in gen_time((8, 10, 0), (10, 50, 00), (0, 15, 12)):
        print(time)