
roslaunch rosbridge_server rosbridge_websocket.launch &
rosrun uvc_camera uvc_camera_node _device:=/dev/video0 &
rosrun rosserial_python serial_node.py /dev/ttyACM0 _baud:=115200 &
rosrun jetson_servo_arm main.py 
