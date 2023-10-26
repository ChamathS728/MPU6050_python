# Import relevant libraries

import smbus # Low level library for communications
import time # used to sleep the RPi

# MPU6050 Datasheet: https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf
# MPU6050 Register sheet: https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf


# Linear acceleration registers
ACCEL_XOUT_H = 0x3B
ACCEL_XOUT_L = 0x3C
ACCEL_YOUT_H = 0x3D
ACCEL_YOUT_L = 0x3E
ACCEL_ZOUT_H = 0x3F
ACCEL_ZOUT_L = 0x40

# Angular acceleration registers
GYRO_XOUT_H = 0x43
GYRO_XOUT_L = 0x44
GYRO_YOUT_H = 0x45
GYRO_YOUT_L = 0x46
GYRO_ZOUT_H = 0x47
GYRO_ZOUT_L = 0x48

# Additional registers
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19 # Sample rate divider. Sample rate = GyroscopeOutputRate/(1 + SMPLRT_DIV)
                    # GyroscopeOutputRate = 8kHz if DLPF_CFG = 0 or 7 | 1kHz if DLPF_CFG is 1 to 6
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
ACCEL_CONFIG = 0x1C
INT_ENABLE   = 0x38

# Setting up constants or
bus = smbus.SMBus(1)
Device_Address = 0x68

# Setup functions for the MPU6050
def MPU_init():
    # Set up sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    # Set up power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    # Set up configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
    # Set up gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
        # This sets the gyroscope to measure to +- 1000deg/s
        # and sets ZG_ST bit = 1 which causes the Z axis gyro to self test
    # Set up interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)
    # Set up accelerometer config register
    bus.write_byte_data(Device_Address, ACCEL_CONFIG, 8)
        # Sets AFS_SEL = 1 so it can measure +- 2g for linear acceleration

def read_raw_data(addr):
    # Accelerometer and Gyroscope values are 16-bit, so
    # there's 2 registers that store all the info

    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)

    # High should be 8 place values higher than low
    value = ((high << 8) | low)

    # Get signed value from the MPU6050
    if (value > 32768):
        value -= 65536

    return value


# Set up the MPU
MPU_init()

print("Reading data from Gyro and Accelerometer")

while True:
    # Read linear accelerations
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)

    # Read angular accelerations
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)

    # Divide by sensitivity scale factors based on FS_SEL and AFS_SEL
        # FS_SEL = 2 in this case and AFS_SEL = 1
    Ax = acc_x / 8192.0
    Ay = acc_y / 8192.0
    Az = acc_z / 8192.0

    Gx = gyro_x / 32.8
    Gy = gyro_y / 32.8
    Gz = gyro_z / 32.8

    # Print everything
    #print("Gx = %.2f" %Gx, u'\u00v0'+"/s", "\tGy=%.2f" %Gy, u'\u00v0'+"/s", "\tGz=%.2f" %Gz, u'\u00v0'+"/s", "\tAx=%.2f g" %Ax, u'\u00v0'+"/s""\tAy=%.2f g" %Ay, u'\u00v0'+"/s", "\tAz=%.2f g" Az)

    print(f"{Ax=}")




