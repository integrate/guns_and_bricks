import random, time

def make_gun():
    gun = {
        "level": 1,
        "shots_per_second":1,
        "shot_power": 1,
        "shot_speed": 1,
        "time_shot": time.time()
    }
    guns.append(gun)
    bullet_lines.append([])

def make_bullet(gun: dict, gun_line_number):
    time_interval = 1/gun["shots_per_second"]
    time_pass = time.time()-gun["time_shot"]
    if time_pass>=time_interval:
        bullet={
            "power": gun["shot_power"],
            "x":0,
            "speed": gun["shot_speed"]
        }

        bullet_lines[gun_line_number].append(bullet)
        gun["time_shot"]=time.time()

def step():
    num = 0
    for gun in guns:
        make_bullet(gun, num)
        num+=1

    for bul_line in bullet_lines:
        for bul in bul_line:
            bul["x"]+=bul["speed"]

coins = 0

guns = []
bullet_lines = []

make_gun()
make_gun()
make_gun()
make_gun()
make_gun()
make_gun()
make_gun()
make_gun()
