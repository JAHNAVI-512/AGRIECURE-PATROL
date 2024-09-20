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
