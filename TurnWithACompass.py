def direction(facing, turn):
    '''Solution for "Turn with a Compass" task with error processing.
    https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/train/python'''

    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    if turn < 0:
        turn = abs(turn)
        directions.reverse()

    turn = turn % 360
    directions = directions[directions.index(facing)::] + directions[:directions.index(facing)+1:]

    return f'\n{directions[int(turn / 45)]}\n'


def main():

    while True:
        facing = input("\nEnter the direction (N, NE, E, SE, S, SW, W, NW): ").upper()
        try:
            turn = int(input("Enter certain degree to turn (A multiple of 45, between -1080 and 1080): "))
        except BaseException:
            print("\nEnter a valid degree!")
            continue
        if facing not in ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']:
            print("Enter a valid direction!")
            continue
        if int(turn / 45) != turn / 45:
            print("\nEnter a valid degree!")
            continue

        print(direction(facing, turn))
        break

if __name__ == "__main__":
    main()