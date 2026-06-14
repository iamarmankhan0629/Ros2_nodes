#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
 
 
class number_counter_node(Node): 
    def __init__(self):
        super().__init__("number_counter") 
        self.subscriber_=self.create_subscription(Int64,'number',self.callback_number_counter,10)
        self.get_logger().info('number_counter is started')
    
    def callback_number_counter(self,msg:Int64):
        self.get_logger().info(str(msg.data))
        
            
 
 
def main(args=None):
    rclpy.init(args=args)
    node = number_counter_node() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main() 