import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class DrawSquare(Node):
    def __init__(self):
        super().__init__("draw_square")
        self.publisher = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer_period =1
        self.create_timer(self.timer_period,self.timer_callback)

    def timer_callback(self):
        command =[]
        msg = Twist()
        msg.angular.z = 1.5707963267948966192313216916398
        command.append(msg)

        turn = Twist()
        turn.linear.x =2.0
        command.append(turn)

        command = command*4

        for m in command:
            self.publisher.publish(m)
            time.sleep(3)
            


def main(args=None):
    rclpy.init(args=args)
    node = DrawSquare()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =='__main__':
    main()
