#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge

import cv2
import numpy as np


class FeatureTrackerNode(Node):

    def __init__(self):
        super().__init__('feature_tracker_node')

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(
            CompressedImage,
            '/camera/image/compressed',
            self.image_callback,
            10
        )

        self.orb = cv2.ORB_create(1000)

        self.get_logger().info("Feature tracker started")

    def image_callback(self, msg):

        np_arr = np.frombuffer(msg.data, np.uint8)

        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        keypoints, descriptors = self.orb.detectAndCompute(gray, None)

        frame_with_features = cv2.drawKeypoints(
            frame,
            keypoints,
            None,
            color=(0, 255, 0)
        )

        cv2.imshow("ORB Features", frame_with_features)
        cv2.waitKey(1)


def main(args=None):

    rclpy.init(args=args)

    node = FeatureTrackerNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()