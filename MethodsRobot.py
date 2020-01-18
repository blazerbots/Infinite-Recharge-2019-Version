import ctre
import wpilib as wpi
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID
import ports

class Drive():
    def __init__(self):
        
        self.leftMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(ports.talonPorts.get("leftChassisMotor")))
        self.rightMotor = wpi.SpeedControllerGroup(ctre.WPI_TalonSRX(ports.talonPorts.get("rightChassisMotor")))
        self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

    def basicDrive(self, x, y):
        if self.drive is None:
            self.drive = wpi.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

        self.controllerXValue = x
        self.controllerYValue = y
        self.drive.arcadeDrive(self.controllerYValue, self.controllerXValue)
    
'''
class Shooter():
    def shooterInit(self, robot, controller):
    
        Intake Components and Variables
        self.intakeMotor = ctre.WPI_TalonSRX(ports.talonPorts.get("intkeMotor"))
        self.bToggle = False
        self.aToggle = False

        if(not( type(controller) is None) and isinstance(controller, wpi.XboxController)):
            self.driverController = controller
        else:
            print("No controller detected")

    def intake(self):
        if(self.driverController.getBButtonPressed()):
            self.bToggle = not self.bToggle
            self.aToggle = False

        if(self.driverController.getAButtonPressed()):
            self.aToggle = not self.aToggle
            self.bToggle = False

        if(self.aToggle):
            self.intakeMotor.set(.1)
        else:
            self.intakeMotor.stopMotor()

        if(self.bToggle):
            self.intakeMotor.set(-.1)
        else:
            self.intakeMotor.stopMotor()
'''

