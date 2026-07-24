def digitalClock(seconds):
    totla_min = seconds // 60
    minutes = totla_min % 60
    hours = (totla_min // 60) % 24
    sec = seconds % 60
    return f'{hours:02}:{minutes:02}:{sec:02}'
print(digitalClock(61201))