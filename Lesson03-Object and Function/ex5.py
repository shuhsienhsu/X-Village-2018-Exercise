def carbon_foot(vesicle):
    def action(distance):
        if(vesicle == 'car'):
            return 0.24 * distance
        elif(vesicle == 'bus'):
            return 0.03 * distance
        elif(vesicle == 'scooter'):
            return 0.06 * distance
    return action

way = carbon_foot('car')
print(way(100))