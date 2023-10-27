import mpu6050

class KalmanFilter:
    def __init__(self, Q, R):
        # Set up any needed matrices
        self.state = None
        self.covariance = None
        self.kalman_gain = None

        self.Q = Q
        self.R = R

    def predict_state(self):
        pass

    def predict_covariance(self):
        pass

    def calc_kalman_gain(self):
        pass
    
    def update_state(self):
        pass

    def update_covariance(self):
        pass