import math
class Drones:

    def __init__(self, *latitude, *longitude, *altitude):
        self.lat = latitude
        self.long = longitude
        self.alt = altitude

    @classmethod
    def distance_between_drones(cls,first_drone, second_drone):
        R = 6371 # in km
        x = math.sin((first_drone.lat - second_drone.lat)/2)**2 
        y = math.cos(first_drone.lat) * math.cos(second_drone.lat) * (math.sin((first_drone.long - second_drone.long)/2)**2)
        
        return 2*R*math.asin((x + y) ** 0.5)

    def angle_between_drones(self):

        pass


if __name__ == "__main__":
    d1 = Drones( 48.8566, 2.3522, 1)
    d2 = Drones(27.9881, 86.9250, 1)
    d3 = Drones(50.0647, 19.9450, 1)
    d4 = Drones(40.7484, 19.9450, 1)

    print(Drones.distance_between_drones(d1,d3))
    print(Drones.distance_between_drones(d2,d4))
