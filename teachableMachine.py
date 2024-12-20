import os
import cv2
import numpy as np
import tensorflow as tf
import serial
import time

# Load TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path="model_new.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Setup Serial Communication
arduino = serial.Serial('COM9', 9600)  # Update with Port (Windows/Mac different formats)
time.sleep(2)  # Allow time for Arduino to initialize

# Setup Webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Update with Format (Windows/Mac different formats)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame to fit model input
    input_image = cv2.resize(frame, (224, 224))  # Adjust size as per your model
    input_image = np.expand_dims(input_image, axis=0)
    input_image = input_image.astype(np.float32) / 255.0

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], input_image)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])

    # Determine which class has the highest confidence
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)

    if confidence > 0.7:  # Ensure confidence is high enough
        if predicted_class == 0:
            print("Hydrangea")
            arduino.write(b"Hydrangea\n")
            os.startfile("3D-models\\Hydrangea_sp_Hortensia_OBJ\\FL48_1.obj")
            time.sleep(10)
        elif predicted_class == 1:
            print("Strelizia Reginae")
            arduino.write(b"Strelizia Reginae\n")
            os.startfile("3D-models\\Strelitzia_OBJ\\strelitzia_1.obj")
            time.sleep(10)
        elif predicted_class == 2:
            print("Sunflower")
            arduino.write(b"Sunflower\n")
            os.startfile("3D-models\\Sunflower.glb")
            time.sleep(10)
        elif predicted_class == 3:
            print("Fern")
            arduino.write(b"Fern\n")
            os.startfile("3D-models\\Matteuccia_Struthiopteris_OBJ\\matteucia_struthiopteris_1.obj")
            time.sleep(10)
        elif predicted_class == 4:
            print("Orchid")
            arduino.write(b"Orchid\n")
            os.startfile("3D-models\\Orchid_Phalaenopsis_OBJ\\orchid.obj")
            time.sleep(10)

    # Display the frame
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()
