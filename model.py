import random, time

def add_gun():
    if len(guns)<8:
        make_gun()

def make_gun():
    gun = {
        "level": 1,
        "level_price": 10,
        "shots_per_second": 1,
        "shots_per_second_price": 10,
        "shot_power": 1,
        "shot_power_price": 10,
        "shot_speed": 1,
        "shot_speed_price": 10,
        "time_shot": time.time()
    }

    guns.append(gun)
    bullet_lines.append([])
    brick_lines.append([])


def make_bullet(gun: dict, gun_line_number):
    time_interval = 1 / gun["shots_per_second"]
    time_pass = time.time() - gun["time_shot"]
    if time_pass >= time_interval:
        bullet = {
            "power": gun["shot_power"],
            "x": 150,
            "speed": gun["shot_speed"]
        }

        bullet_lines[gun_line_number].append(bullet)
        gun["time_shot"] = time.time()


def make_all_bullets():
    num = 0
    for gun in guns:
        make_bullet(gun, num)
        num += 1


def remove_bullets():
    for bul_line in bullet_lines:
        for bul in bul_line.copy():
            bul["x"] += bul["speed"]
            if bul["x"] > 850:
                bul_line.remove(bul)


def kill_bricks():
    global coins
    num = 0
    for bul_line in bullet_lines:
        for bul in bul_line.copy():

            if len(brick_lines[num]) == 0:
                break

            first_brick = brick_lines[num][0]
            if bul["x"] > first_brick["x"]:
                first_brick["hp"] -= bul["power"]

                bul_line.remove(bul)
                if first_brick["hp"] <= 0:
                    brick_lines[num].remove(first_brick)
                    coins += first_brick["coins"]
        num += 1


def move_bricks():
    global game_over
    for brick_line in brick_lines:
        for brick in brick_line:
            brick["x"] -= 1
            if brick['x'] < 155:
                game_over = True


def step():
    global game_over
    if game_over:
        return

    make_all_bullets()

    remove_bullets()

    kill_bricks()

    move_bricks()


def make_bricks():
    """
    Алгоритм создания кирпичей:
         каждую секунду должны создаваться кирпичи общей мощностью brick_points_per_second. Это число будет постепенно увеличиваться.
         Кирпичи должны создаться на одной трети из всех линий. То есть, если в игре 6 линий, то кирпичи должны
           создаться на двух линиях. Линии выбираются случайно.

         На каждой выбранной линии должен создаться кирпич мощностью brick_points_per_second/3.

    """
    line_count = int(len(guns) / 3)

    point_per_line = int(brick_points_per_second / line_count)

    lines = []
    while len(lines) < line_count:
        line = random.randint(0, len(guns) - 1)
        if line not in lines:
            lines.append(line)

    for line in lines:
        add_brick(point_per_line, line)


def add_brick(hp, line_number):
    if hp < 5:
        level = 1
    elif hp < 25:
        level = 2
    elif hp < 125:
        level = 3
    else:
        level = 4

    brick = {
        "level": level,
        "hp": hp,
        "x": 900,
        "coins": hp
    }

    brick_lines[line_number].append(brick)


def buy_shot_power(gun_num):
    global coins

    if coins >= guns[gun_num]["shot_power_price"]:
        guns[gun_num]["shot_power"] += 1
        coins -= guns[gun_num]["shot_power_price"]
        guns[gun_num]["shot_power_price"] = int(1.1 * guns[gun_num]["shot_power_price"])


def buy_shot_speed(gun_num):
    global coins
    if coins >= guns[gun_num]["shot_speed_price"]:
        guns[gun_num]["shot_speed"] += 1
        coins -= guns[gun_num]["shot_speed_price"]
        guns[gun_num]["shot_speed_price"] = int(1.1*guns[gun_num]["shot_speed_price"])



def buy_shot_count(gun_num):
    global coins
    if coins >= guns[gun_num]["shots_per_second_price"]:
        guns[gun_num]["shots_per_second"] += 1
        coins -= guns[gun_num]["shots_per_second_price"]
        guns[gun_num]["shots_per_second_price"] = int(1.1 * guns[gun_num]["shots_per_second_price"])


def buy_gun_level(gun_num):
    guns[gun_num]["level"] += 1


game_over = False

coins = 100

guns = []
bullet_lines = []
brick_lines = []

brick_points_per_second = 3

make_gun()
make_gun()
make_gun()
# make_gun()
# make_gun()
# make_gun()
# make_gun()
# make_gun()
