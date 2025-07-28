# Warehouse Inspection Robot

A ROS 2-based autonomous warehouse inspection robot developed as part of a global hackathon project. This system combines robotics, environmental sensing, and 3D CAD modeling to optimize warehouse monitoring and safety.

---

## Project Summary

This robot is designed to autonomously inspect warehouse environments using various onboard sensors like LIDAR, ultrasonic, light, temperature, and humidity sensors. It includes a custom chassis modeled in Fusion 360 and integrated into ROS 2 using URDF/Xacro. The system is visualized in RViz and can be simulated for path planning and environment scanning.

---

## Features

- 🛠️ **Fully modeled robot using Fusion 360 (.f3d + STL files)**
- 📦 **ROS 2 Foxy** integration with URDF/Xacro description
- 🧭 **LIDAR-based SLAM** for navigation and environment mapping
- 🌡️ **Sensor integration** for temperature, humidity, and lighting conditions
- 🧹 **Smart waste-sorting assistant module** (via attachable sub-bot)
- 📸 Optional **CCTV camera mounting** for visual inspection
- 🧾 Compatible with **Gazebo** and **RViz** for visualization

