# elf-project


## 1. Introduction


## 2. Trajectory Control: Theoretical Approach


### 2.1 Control Law
A line follower is basically a differential drive with the following kinematics:

$$\dot{\text{x}} = f(\theta)\text{u} \quad \Longrightarrow \quad \begin{bmatrix} \dot{x} \\ \dot{y} \\ \dot{\theta} \end{bmatrix} = \begin{bmatrix} \frac{1}{2}\cos(\theta) & \frac{1}{2}\cos(\theta) \\ \frac{1}{2}\sin(\theta) & \frac{1}{2}\sin(\theta) \\ \frac{1}{2r} & \frac{-1}{2r} \end{bmatrix} \begin{bmatrix} u_r \\ u_l \end{bmatrix}$$

To track a desired trajectory $\text{x}_{d}$, define:

$$\dot{\text{x}}(t) = \dot{\text{x}}_d(t) + K_{p}\text{x}_{e}(t) + K_{i}\int_{0}^{t}\text{x}_{e}(\tau)d\tau$$

$$\text{x}_e(t) = \text{x}_d(t) - \text{x}(t)$$

Therefore,

$$\text{u} = f^{+}(\theta)\dot{\text{x}}$$

where $f^{+}$ is the  left inverse of $f$, s.t. $f^{+}f=I$ (Luckily, the column of $f$ is linearly independent). The value of $f^{+}$ is

$$f^{+}(\theta) = \begin{bmatrix} \cos(\theta) & \sin(\theta) & r \\ \cos(\theta) & \sin(\theta) & -r \end{bmatrix}$$


### 2.2 Controller on the Input $\text{u}$
Since we have encoders on both motors, we can guarantee an accurate speed controller for the motor $u_i$. Suppose we have a function that maps a reference speed to the corresponding PWM value $f_{\text{PWM}}(r_u)$. The speed controller is:

$$u_{\text{PWM}}(t) = f_{\text{PWM}}(r_u) + K_pu_e(t) + K_i\int_{0}^{t}u_e(\tau)d\tau$$

$$u_e = r_u - u_i, \quad i=l,r$$



### 2.3 Output (Sensor) Values
ELF robot is equipped with 16 line-detecting photodiodes, a 9-axis IMU, and two motor encoders, which produce full-state information.


#### (a) The value of $\theta$ and $\dot{\theta}$
The value of $\theta$ can be determined from:
1. $\dot{\theta}$ computation, 
2. IMU filtering,
3. photodiodes

Whereas, the value of $\dot{\theta}$ can be determined from:
1. input-state computation,
2. IMU gyroscope

Let us design a complementary filter that produces $\dot{\hat{\theta}}$ with:

$$\dot{\hat{\theta}}[n] = \alpha_1\dot{\hat{\theta}}[n - 1] + (1 - \alpha_1)\left(\alpha_2\dot{\theta}(\hat{\theta}[n], \text{u}[n]) + (1 - \alpha_2)g_z[n] \right)$$

where $g_z$ is the z-axis gyroscope value. The value of $\alpha_1, \alpha_2 \in [0, 1]$ can be made close to zero if we are confident with the sensor.

Furthermore, the $\hat{\theta}$:

$$\hat{\theta}_c[n] = \alpha_3\hat{\theta}[n - 1] + (1 - \alpha_3)\left( \alpha_4\left(\hat{\theta}[n-1] + \dot{\hat{\theta}}[n]\Delta T\right) + (1 - \alpha_4)q[n] \right)$$

$$\hat{\theta}[n] = \alpha_5\hat{\theta}_c[n] + (1-\alpha_5)p[n]$$

where $q$ is the heading value from the IMU filter, i.e., Madgwick or Mahony, and $p$ is the heading value from photodiode sensors reading relative to the line. Same as before, the value of $\alpha_3, \alpha_4 \in [0, 1]$ can be made close to zero if we are confident with the sensor. We can choose whether to include or exclude the photodiode sensors reading by changing the value of $\alpha_5$.


#### (b) The value of $x$, $y$, $\dot{x}$, and $\dot{y}$ 

To be continued.