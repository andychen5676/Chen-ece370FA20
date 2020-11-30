rosservice call gazebo/delete_model cc_robot
rosrun gazebo_ros spawn_model -file models/model.sdf -sdf -model cc_robot -y $2 -x $1 -z 1.0