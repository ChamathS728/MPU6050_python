import RPi.GPIO
import smbus
import numpy as np

class MPU6050:
    """
    Raw datasheet here: https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf
    Register map here: https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf 
    
    Reference repository here: https://github.com/m-rtijn/mpu6050/blob/master/mpu6050/mpu6050.py

    """

    # Linear acceleration registers
    ACCEL_XOUT_H    = 0x3B
    ACCEL_XOUT_L    = 0x3C
    ACCEL_YOUT_H    = 0x3D
    ACCEL_YOUT_L    = 0x3E
    ACCEL_ZOUT_H    = 0x3F
    ACCEL_ZOUT_L    = 0x40    

    # Angular acceleration registers
    GYRO_XOUT_H     = 0x43
    GYRO_XOUT_L     = 0x44
    GYRO_YOUT_H     = 0x45
    GYRO_YOUT_L     = 0x46
    GYRO_ZOUT_H     = 0x47
    GYRO_ZOUT_L     = 0x48

    # Additional registers
    PWR_MGMT_1      = 0x6B
    SMPLRT_DIV      = 0x19 # Sample rate divider. Sample rate = GyroscopeOutputRate/(1 + SMPLRT_DIV)
                        # GyroscopeOutputRate = 8kHz if DLPF_CFG = 0 or 7 | 1kHz if DLPF_CFG is 1 to 6
    CONFIG          = 0x1A
    GYRO_CONFIG     = 0x1B
    ACCEL_CONFIG    = 0x1C
    INT_ENABLE      = 0x38
    FIFO_ENABLE     = 0x23 
    INT_STATUS      = 0x3A

    # FS_SEL[1:0] gyro -> inputs into Bits 4 and 3 of GYRO_CONFIG register
    FS_SEL_250  = 0x00 #bin(0)  
    FS_SEL_500  = 0x01 #bin(1) 
    FS_SEL_1000 = 0x02 #bin(2)
    FS_SEL_2000 = 0x03 #bin(3)

    # AFS_SEL[1:0] accelerometer -> inputs into Bits 4 and 3 of ACCEL_CONFIG register
    AFS_SEL_2g  = 0x00
    AFS_SEL_4g  = 0x01
    AFS_SEL_8g  = 0x02
    AFS_SEL_16g = 0x03


    # Setting up constants or
    # Device_Address = 0x68        


    def __init__(self, addr=0x68, bus=1):
        
        # Preamble stuff for I2C communication
        self.addr = addr
        self.bus = smbus.SMBus(bus)


    def configure_accel(self, full_scale: int):
        pass

    def configure_gyro(self, full_scale: int):
        pass

    def calibrate(self):
        pass    

    def get_accel(self) -> np.array:
        """
        Returns results from all acceleration registers in an np array as decimals
        -> Requires conversion from 2's complement 
        """
        pass

    def get_gyro(self) -> np.array:
        pass

    def get_temp(self):
        pass

    def set_sample_rate(self, smplrt_div: np.uint8):
        pass

    def set_interrupt(self, status: bool):
        pass
