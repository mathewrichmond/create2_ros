from setuptools import find_packages, setup

package_name = "create2_ros"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools", "pycreate2"],
    zip_safe=True,
    maintainer="mathew richmond",
    maintainer_email="mathewrichmond@gmail.com",
    description="ROS2 Node for iRobot Create 2",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "service = create2_ros.node:main",
        ],
    },
)
