
import random
import time
import logging
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RoboticScarecrow:
    def __init__(self, email_recipient, pesticide_rate=1, speed=1.0, irrigation_rate=1.0):
        self.position = 0
        self.is_moving = True
        self.field_length = 100  # Example field length
        self.pesticide_rate = pesticide_rate
        self.speed = speed  # Speed in m/s
        self.irrigation_rate = irrigation_rate  # Irrigation rate in liters per sq meter
        self.maintenance_needed = False
        self.email_recipient = email_recipient

    def move(self):
        if self.is_moving:
            step = self.speed
            self.position += step
            
            if self.position >= self.field_length:
                self.position = 0  # Reset position when reaching the end of the field
            
            logging.info(f"Robotic Scarecrow moved to position {self.position:.2f} meters.")

    def detect_birds(self):
        detected = random.random() < 0.5
        if detected:
            logging.info("Birds detected!")
        return detected

    def scare_birds(self):
        logging.info("Buzz! Scaring birds away!")

    def spray_pesticide(self):
        logging.info(f"Spraying {self.pesticide_rate} unit(s) of pesticide on the plants.")

    def irrigate(self):
        logging.info(f"Irrigating at a rate of {self.irrigation_rate} liters per square meter.")

    def monitor_field(self):
        if random.random() < 0.1:  # 10% chance of detecting irregular activity
            logging.warning("Irregular activity detected! Taking action.")
            self.scare_birds()
            self.spray_pesticide()
            self.send_notification("Irregular activity detected in the field!")

    def check_maintenance(self):
        if random.random() < 0.05:  # 5% chance of needing maintenance
            self.maintenance_needed = True
            logging.warning("Maintenance needed!")
            self.send_notification("Maintenance is required for the Robotic Scarecrow.")

    def send_notification(self, message):
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'Robotic Scarecrow Alert'
            msg['From'] = 'your_email@example.com'
            msg['To'] = self.email_recipient

            with smtplib.SMTP('smtp.example.com', 587) as server:  # Configure SMTP server
                server.starttls()
                server.login('your_email@example.com', 'your_password')
                server.send_message(msg)
                logging.info("Notification sent to the user.")
        except Exception as e:
            logging.error(f"Failed to send notification: {e}")

def main():
    email_recipient = 'recipient@example.com'  # Replace with the user's email address
    pesticide_rate = float(input("Enter the pesticide application rate (default is 1): ") or 1)
    speed = float(input("Enter the robot speed in meters per second (default is 1): ") or 1)
    irrigation_rate = float(input("Enter the irrigation rate in liters per square meter (default is 1): ") or 1)

    scarecrow = RoboticScarecrow(email_recipient, pesticide_rate, speed, irrigation_rate)

    try:
        while True:
            scarecrow.move()
            if scarecrow.detect_birds():
                scarecrow.scare_birds()
                scarecrow.spray_pesticide()
            scarecrow.irrigate()  # Call the irrigation method
            scarecrow.monitor_field()
            scarecrow.check_maintenance()
            time.sleep(2)  # Simulate time delay between movements
            
            # Check for user input to stop the robot
            if input("Type 'stop' to end the operation: ").strip().lower() == 'stop':
                logging.info("Stopping the Robotic Scarecrow.")
                break

    except KeyboardInterrupt:
        logging.info("Shutting down the Robotic Scarecrow.")

if __name__ == "__main__":
    main()

##Code for Scaring away crow, Maintenance Alerts, User Customization(speed of robot and rates of spraying), User Alerts, Multi-Functionality (Seed Planting and Irrigation System) and Spraying pesticide
import random
import time
import logging
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RoboticScarecrow:
    def __init__(self, email_recipient, pesticide_rate=1, speed=1.0, irrigation_rate=1.0):
        self.position = 0
        self.is_moving = True
        self.field_length = 100  # Example field length
        self.pesticide_rate = pesticide_rate
        self.speed = speed  # Speed in m/s
        self.irrigation_rate = irrigation_rate  # Irrigation rate in liters per sq meter
        self.maintenance_needed = False
        self.email_recipient = email_recipient

    def move(self):
        if self.is_moving:
            step = self.speed  # Move based on speed
            self.position += step
            
            if self.position >= self.field_length:
                self.position = 0  # Reset position when reaching the end of the field
            
            logging.info(f"Robotic Scarecrow moved to position {self.position} meters.")

    def detect_birds(self):
        detected = random.random() < 0.5
        if detected:
            logging.info("Birds detected!")
        return detected

    def scare_birds(self):
        logging.info("Buzz! Scaring birds away!")

    def spray_pesticide(self):
        logging.info(f"Spraying {self.pesticide_rate} unit(s) of pesticide on the plants.")

    def irrigate(self):
        logging.info(f"Irrigating at a rate of {self.irrigation_rate} liters per square meter.")

    def monitor_field(self):
        if random.random() < 0.1:  # 10% chance of detecting irregular activity
            logging.warning("Irregular activity detected! Taking action.")
            self.scare_birds()
            self.spray_pesticide()
            self.send_notification("Irregular activity detected in the field!")

    def check_maintenance(self):
        # Randomly determine if maintenance is needed
        if random.random() < 0.05:  # 5% chance of needing maintenance
            self.maintenance_needed = True
            logging.warning("Maintenance needed!")
            self.send_notification("Maintenance is required for the Robotic Scarecrow.")

    def send_notification(self, message):
        # Simple email notification system (configure SMTP settings accordingly)
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'Robotic Scarecrow Alert'
            msg['From'] = 'your_email@example.com'
            msg['To'] = self.email_recipient

            with smtplib.SMTP('smtp.example.com', 587) as server:  # Configure SMTP server
                server.starttls()
                server.login('your_email@example.com', 'your_password')
                server.send_message(msg)
                logging.info("Notification sent to the user.")
        except Exception as e:
            logging.error(f"Failed to send notification: {e}")

def main():
    email_recipient = 'recipient@example.com'  # Replace with the user's email address
    pesticide_rate = float(input("Enter the pesticide application rate (default is 1): ") or 1)
    speed = float(input("Enter the robot speed in meters per second (default is 1): ") or 1)
    irrigation_rate = float(input("Enter the irrigation rate in liters per square meter (default is 1): ") or 1)

    scarecrow = RoboticScarecrow(email_recipient, pesticide_rate, speed, irrigation_rate)

    try:
        while True:
            scarecrow.move()
            if scarecrow.detect_birds():
                scarecrow.scare_birds()
                scarecrow.spray_pesticide()
            scarecrow.irrigate()  # Call the irrigation method
            scarecrow.monitor_field()
            scarecrow.check_maintenance()
            time.sleep(2)  # Simulate time delay between movements
    except KeyboardInterrupt:
        logging.info("Shutting down the Robotic Scarecrow.")

if __name__ == "__main__":
    main()

import random
import time
import sys
import pyttsx3 ## INSTALL pyttsx3 before running the code to get sound output

class RoboticScarecrow:
    def _init_(self, name):
        self.name = name
        self.modes = ['Chill Mode', 'Warrior Mode', 'Alert Mode']
        self.current_mode = 'Chill Mode'
        self.achievements = []
        self.pests_sprayed = 0
        self.birds_scared = 0
        self.engine = pyttsx3.init()

    def speak(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

    def switch_mode(self, mode):
        if mode in self.modes:
            self.current_mode = mode
            self.speak(f"{self.name} is now in {self.current_mode}!")
        else:
            self.speak(f"Mode {mode} not available.")

    def scare_bird(self):
        self.birds_scared += 1
        print(f"{self.name} scared away a bird!")
        self.speak("Bird scared away!")
        if self.birds_scared % 10 == 0:
            self.unlock_achievement(f"Bird Master: Scared {self.birds_scared} birds")

    def spray_pesticide(self):
        self.pests_sprayed += 1
        print(f"{self.name} sprayed pesticide!")
        self.speak("Pesticide sprayed!")
        if self.pests_sprayed % 5 == 0:
            self.unlock_achievement(f"Pest Buster: Sprayed {self.pests_sprayed} pests")

    def unlock_achievement(self, achievement):
        self.achievements.append(achievement)
        print(f"Achievement Unlocked: {achievement}")
        self.speak(f"Achievement Unlocked: {achievement}")

    def patrol(self):
        print(f"{self.name} is patrolling in {self.current_mode}...")
        self.speak(f"{self.name} is patrolling in {self.current_mode}.")
        for _ in range(5):
            action = random.choice(['scare_bird', 'spray_pesticide'])
            if action == 'scare_bird':
                self.scare_bird()
            else:
                self.spray_pesticide()
            self.display_dashboard()
            time.sleep(1)

    def display_achievements(self):
        print("\nAchievements:")
        for ach in self.achievements:
            print(f"- {ach}")

    def report_status(self):
        print(f"\nReport for {self.name}:")
        print(f"Mode: {self.current_mode}")
        print(f"Birds Scared: {self.birds_scared}")
        print(f"Pests Sprayed: {self.pests_sprayed}")
        self.display_achievements()

    def display_dashboard(self):
        sys.stdout.write("\r")  # Return the cursor to the start of the line
        sys.stdout.write(f"{self.name} | Mode: {self.current_mode} | Birds Scared: {self.birds_scared} | Pests Sprayed: {self.pests_sprayed}")
        sys.stdout.flush()

# Example of usage
robot = RoboticScarecrow("AgriBot")

# Switch personality mode
robot.switch_mode("Warrior Mode")

# Simulate patrolling with random actions
robot.patrol()

# Display final report
robot.report_status()


