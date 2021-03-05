# By Kami Bigdely-Shamloo
# Consolidate duplicate conditional fragments
# This program changes car's gear according to the car speed. Then it 
# displays the updated gear on the car's front panel.

def change_gear(str_gear):
    print("Gear changed to", str_gear)

def display_gear(str_gear): 
    print("displayed gear:", str_gear)

gearList = {
    '1': [0,30],
    '2': [30,50],
    '3': [50,90],
    '4': [90],
    'R': [0],
}
def process_speed(speed):
    for g in gearList:
        if len(gearList[g]) == 2:
            if gearList[g][0]<= speed < g[1]:
                display_gear(g)
        else:
            if 90 <= speed:
                display_gear(g)
            elif speed <= 0:
                display_gear(g)
            

if __name__ == "__main__":
    process_speed(40)