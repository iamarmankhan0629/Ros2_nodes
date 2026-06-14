#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    
    def __init__(self):
        super().__init__('py_test')
        self.counter_=0
        self.get_logger().info("Hello world!")
        self.create_timer(1.0,self.time_callback)
    
    def time_callback(self):
        self.get_logger().info('hello'+str(self.counter_))
        self.counter_+=1

def main(args=None):
    rclpy.init(args=args)
    
    #creating a node
    node=MyNode()
    
    
    
    # to run the program as long as we want and close it with ctrl+c
    rclpy.spin(node)
    
    
    # to close the program after execution
    rclpy.shutdown()
    
if __name__=="__main__":
    main()    