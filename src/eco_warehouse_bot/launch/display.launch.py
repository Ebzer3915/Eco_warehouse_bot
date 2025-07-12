from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_name = 'eco_warehouse_bot'  # <-- replace with your actual package name
    xacro_file = os.path.join(get_package_share_directory(pkg_name), 'urdf', 'eco_bot.xacro')

    return LaunchDescription([
        DeclareLaunchArgument(
            name='use_sim_time', default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'robot_description': Command(['xacro ', xacro_file])
            }]
        ),
        
        Node(
           package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/Users/ebinezerjustin/ros_eco/src/eco_warehouse_bot/rviz/rviz.rviz']
        )
    
    ])
