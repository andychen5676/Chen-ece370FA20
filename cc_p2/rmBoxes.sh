for i in {0..255}
do
    rosservice call gazebo/delete_model box$i &
    echo $i
done
