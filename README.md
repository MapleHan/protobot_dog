# Protobot_dog仿真程序
**Rviz**
![RobotModel](Screenshot%20from%202019-12-11%2008-33-03-01.png "RobotModel")

**Gazebo**
![RobotModel](Screenshot%20from%202019-12-11%2008-33-03-02.png "RobotModel")

**protobot_dog_description**: 模型文件package  
**protobot_dog_leg_ik**: 狗腿姿态逆解package,订阅落脚点topic，发布关节位置命令topic  
**protobot_dog_controll**: 狗行走四条腿轨迹控制package，发布每一条腿的落脚点轨迹topic  
**protobot_dog_simulation**: 启动Gazebo并加载关节控制器package，订阅每一关节位置命令topic  

## Step1:安装
1. 网页下载
2. git下载
```bash
git clone https://github.com/MapleHan/protobot_dog.git
```
## Step2:运行
1. 启动Gazebo，默认暂停仿真
```bash
roslaunch protobot_dog_simulation protobot_dog_simulation.launch
```   
2. 启动真实狗    
```bash
roslaunch protobot_dog_bringup bring_up.launch
```
3. 启动运动学逆解程序
```bash
roslaunch protobot_dog_leg_ik protobot_dog_leg_ik.launch
```
4. 发布运动轨迹
   1. 上下蹲起
   ```bash
   rosrun protobot_dog_controll simple_demo.py
   ```
   2. walk
   ```bash
   rosrun protobot_dog_controll walk_demo.py
   ```
   3. trot
   ```bash
   rosrun protobot_dog_controll trot_demo.py
   ```
