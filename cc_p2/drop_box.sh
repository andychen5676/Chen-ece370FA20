#rosservice call gazebo/delete_model cc_robot
rosrun gazebo_ros spawn_model -file models/box.sdf -sdf -model $1 -y $3 -x $2 -z 5.0