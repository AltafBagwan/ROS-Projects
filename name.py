import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import SetPen
import time
import random

class DrawName(Node):
    def __init__(self):
        super().__init__("draw_name")
        self.publisher_ = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.time_period = 1
        self.create_timer(self.time_period,self.timer_callback)
        self.turtle_client = self.create_client(TeleportAbsolute,"/turtle1/teleport_absolute")
        self.pen_client = self.create_client(SetPen,"/turtle1/set_pen")

        while not self.turtle_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available wating for service")
        
        while not self.pen_client.wait_for_service(timeout_sec=1):
            self.get_logger().info("Service not available wating for service")

    def turtle_teleport(self,x,y,theta):
        request = TeleportAbsolute.Request()
        request.x = x
        request.y = y
        request.theta = theta
        self.turtle_client.call_async(request)

    def turtle_pen_(self,r,g,b,width,off):
        request = SetPen.Request()
        request.r =r
        request.g =g
        request.b =b
        request.width =width
        request.off =off

        self.pen_client.call_async(request)


    def draw_a(self):
        commands = []

        move = Twist()
        move.linear.x = 0.0
        commands.append(move)

        turn = Twist()
        turn.angular.z = 1.4
        commands.append(turn)

        move = Twist()
        move.linear.x = 3.0
        commands.append(move)
        
        turn = Twist()
        turn.angular.z = -2.6
        commands.append(turn)

        move = Twist()
        move.linear.x = 3.0
        commands.append(move)

        for cmd in commands:
            self.publisher_.publish(cmd)
            time.sleep(1)

    def draw_l(self):
        commands = []

        turn = Twist()
        turn.angular.z =1.57
        commands.append(turn)

        move = Twist()
        move.linear.x =3.0
        commands.append(move)
        
        move = Twist()
        move.linear.x =-3.0
        commands.append(move)
        
        move = Twist()
        move.linear.y =-2.0
        commands.append(move)


        for cmd in commands:
            self.publisher_.publish(cmd)
            time.sleep(1)


    def draw_t(self):
        commands = []

        move = Twist()
        move.linear.x =0.0
        commands.append(move)

        turn = Twist()
        turn.angular.z =1.57
        commands.append(turn)
        
        move = Twist()
        move.linear.x =3.0
        commands.append(move)
        
        move = Twist()
        move.linear.y =-1.0
        commands.append(move)
        
        move = Twist()
        move.linear.y =2.0
        commands.append(move)


        for cmd in commands:
            self.publisher_.publish(cmd)
            time.sleep(1)

    def draw_f(self):
        commands = []

        move = Twist()
        move.linear.x =0.0
        commands.append(move)

        turn = Twist()
        turn.angular.z =1.57
        commands.append(turn)
        
        move = Twist()
        move.linear.x =3.0
        commands.append(move)
        
        move = Twist()
        move.linear.y =-2.0
        commands.append(move)
        
        move = Twist()
        move.linear.y =2.0
        commands.append(move)
        
        move = Twist()
        move.linear.x =-1.0
        commands.append(move)
        
        move = Twist()
        move.linear.y =-2.0
        commands.append(move)


        for cmd in commands:
            self.publisher_.publish(cmd)
            time.sleep(1)



    def timer_callback(self):
        self.turtle_pen_(0,0,0,3,1)
        self.turtle_teleport(0.5,4.0,0.0)
        self.turtle_pen_(random.randint(0,255),random.randint(0,255),random.randint(0,255),3,0)
        self.draw_a()

        self.turtle_pen_(0,0,0,3,1)
        self.turtle_teleport(2.5,4.0,0.0)
        self.turtle_pen_(random.randint(0,255),random.randint(0,255),random.randint(0,255),3,0)

        self.draw_l()

        self.turtle_pen_(0,0,0,3,1)
        self.turtle_teleport(5.0,4.0,0.0)
        self.turtle_pen_(random.randint(0,255),random.randint(0,255),random.randint(0,255),3,0)
        self.draw_t()

        self.turtle_pen_(0,0,0,3,1)
        self.turtle_teleport(5.9,4.0,0.0)
        self.turtle_pen_(random.randint(0,255),random.randint(0,255),random.randint(0,255),3,0)
        self.draw_a()

        self.turtle_pen_(0,0,0,3,1)
        self.turtle_teleport(8.0,4.0,0.0)
        self.turtle_pen_(random.randint(0,255),random.randint(0,255),random.randint(0,255),3,0)
        self.draw_f()


def main(args=None):
    rclpy.init(args=args)
    node = DrawName()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()