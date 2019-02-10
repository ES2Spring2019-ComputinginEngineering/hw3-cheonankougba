import microbit
import math

def xangle(accel_z, accel_x, accel_y):
    angle_x = math.atan2(accel_x, math.sqrt(accel_z**2+accel_y**2))
    return (math.degrees(angle_x))

def yangle(accel_z, accel_y, accel_x):
    angle_y = math.atan2(accel_y, math.sqrt(accel_z**2+accel_x**2))
    return (math.degrees(angle_y))

while True:
    microbit.sleep(200)
    accel_x = microbit.accelerometer.get_x()
    accel_y = microbit.accelerometer.get_y()
    accel_z = microbit.accelerometer.get_z()

    Xangle = xangle(accel_z, accel_x, accel_y)
    Yangle = yangle(accel_z, accel_y, accel_x)

    print((Xangle,Yangle))

    if Xangle < -10 and Yangle > 10:
        microbit.display.show(microbit.Image.ARROW_NE)
    elif Xangle < -10 and 10 > Yangle > -10:
        microbit.display.show(microbit.Image.ARROW_E)
    elif Xangle < -10 and -10 > Yangle:
        microbit.display.show(microbit.Image.ARROW_SE)
    elif 10 > Xangle > -10 and 10 > Yangle > -10:
        microbit.display.show(microbit.Image('00000:00900:09990:00900:00000:'))
    elif 10 < Xangle and 10 > Yangle > -10:
        microbit.display.show(microbit.Image.ARROW_W)
    elif 10 < Xangle and 10 < Yangle:
        microbit.display.show(microbit.Image.ARROW_NW)
    elif 10 > Xangle > -10 and -10 > Yangle:
        microbit.display.show(microbit.Image.ARROW_S)
    elif 10 > Xangle > -10 and 10 < Yangle:
        microbit.display.show(microbit.Image.ARROW_N)
    elif 10 < Xangle and -10 > Yangle:
        microbit.display.show(microbit.Image.ARROW_SW)
    #if 185 > Xangle > 175 and 185 > Yangle > 175:
        #microbit.display.scroll(":)")
    #else:
        #microbit.display.scroll(":(")