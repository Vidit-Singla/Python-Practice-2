def race(v1, v2, g):
    d1 = g
    d2 = 0
    t = 0
    
    while d1 > d2:
        t += 1
        d1 += v1/3600
        d2 += v2/3600
    
    hours = t // 3600
    minutes = (t % 3600) // 60
    seconds = t % 60
    
    print(f"{hours} hour(s), {minutes} minute(s), and {seconds} second(s)")

race(720, 850, 70)
