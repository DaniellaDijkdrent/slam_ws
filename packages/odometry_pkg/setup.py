from setuptools import setup

package_name = 'odometry_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dani',
    maintainer_email='dani@example.com',
    description='Duckietown odometry package',
    license='MIT',
    entry_points={
        'console_scripts': [
            'odometry_node = odometry_pkg.odometry_node:main',
            'encoder_sim_node = odometry_pkg.encoder_sim_node:main',
            'feature_tracker_node = odometry_pkg.feature_tracker_node:main',
            'monocular_slam_node = odometry_pkg.monocular_slam_node:main',
        ],
    },
)