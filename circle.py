import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircle(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.publisher = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.time_period =1
        self.create_timer(self.time_period,self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.0
        # msg.linear.y = 0.0
        # msg.linear.z = 0.0

        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 1.0

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=='__main__':
    main()