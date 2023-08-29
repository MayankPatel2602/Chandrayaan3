class SpacecraftNavigator:
    def __init__(self):
        pass

    def navigate(self, commands, initial_position, initial_direction):
        x, y, z = initial_position
        direction = initial_direction
        pre_direction = []
        count = 0

        for cmd in commands:
            if cmd == "f":
                if direction == "N":
                    y += 1
                elif direction == "S":
                    y -= 1
                elif direction == "E":
                    x += 1
                elif direction == "W":
                    x -= 1
                elif direction == "U":
                    z += 1
                elif direction == "D":
                    z -= 1
            elif cmd == "b":
                if direction == "N":
                    y -= 1
                elif direction == "S":
                    y += 1
                elif direction == "E":
                    x -= 1
                elif direction == "W":
                    x += 1
                elif direction == "U":
                    z -= 1
                elif direction == "D":
                    z += 1
            elif cmd == "r":
                pre_direction.append(direction)
                count += 1
                if direction == "U":
                    if pre_direction[-2] == "N":
                        direction = "E"
                    elif pre_direction[-2] == "S":
                        direction = "W"
                    elif pre_direction[-2] == "W":
                        direction = "E"
                    elif pre_direction[-2] == "E":
                        direction = "S"
                elif direction == "D":
                    if pre_direction[-2] == "N":
                        direction = "E"
                    elif pre_direction[-2] == "S":
                        direction = "W"
                    elif pre_direction[-2] == "W":
                        direction = "E"
                    elif pre_direction[-2] == "E":
                        direction = "S"
                elif direction == "N":
                    direction = "E"
                elif direction == "S":
                    direction = "W"
                elif direction == "E":
                    direction = "S"
                elif direction == "W":
                    direction = "N"

            elif cmd == "l":
                pre_direction.append(direction)
                count += 1
                if direction == "N":
                    direction = "W"
                elif direction == "S":
                    direction = "E"
                elif direction == "E":
                    direction = "N"
                elif direction == "W":
                    direction = "S"
                elif direction == "U":
                    if pre_direction[-2] == "N":
                        direction = "W"
                    elif pre_direction[-2] == "S":
                        direction = "E"
                    elif pre_direction[-2] == "W":
                        direction = "S"
                    elif pre_direction[-2] == "E":
                        direction = "N"
                elif direction == "D":
                    if pre_direction[-2] == "N":
                        direction = "W"
                    elif pre_direction[-2] == "S":
                        direction = "E"
                    elif pre_direction[-2] == "W":
                        direction = "S"
                    elif pre_direction[-2] == "E":
                        direction = "N"
            elif cmd == "u":
                pre_direction.append(direction)
                count += 1
                if direction == "N" or direction == "S" or direction == "E" or direction == "W":
                    direction = "U"
                elif direction == "U":
                    if pre_direction[-2] == "N":
                        direction = "S"
                    elif pre_direction[-2] == "S":
                        direction = "N"
                    elif pre_direction[-2] == "E":
                        direction = "W"
                    elif pre_direction[-2] == "W":
                        direction = "E"
                elif direction == "D":
                    direction = pre_direction[-2]
            elif cmd == "d":
                pre_direction.append(direction)
                count += 1
                if direction == "N" or direction == "S" or direction == "E" or direction == "W":
                    direction = "D"
                elif direction == "D":
                    if pre_direction[-2] == "N":
                        direction = "S"
                    elif pre_direction[-2] == "S":
                        direction = "N"
                    elif pre_direction[-2] == "E":
                        direction = "W"
                    elif pre_direction[-2] == "W":
                        direction = "E"
                elif direction == "U":
                    direction = pre_direction[-2]
        return (x, y, z), direction

    def main(self):
        commands = input("Enter commands : ")
        initial_position = tuple(map(int, input("Enter initial position (x y z): ").split()))
        initial_direction = input("Enter initial direction (N, S, E, W, U, D): ")

        final_position, final_direction = self.navigate(commands, initial_position, initial_direction)

        print("Final Position:", final_position)
        print("Final Direction:", final_direction)


if __name__ == "__main__":
    navigator = SpacecraftNavigator()
    navigator.main()
