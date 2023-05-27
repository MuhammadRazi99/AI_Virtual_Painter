# AI_Virtual_Painter
This project is called AI Virtual Painter. It is a computer vision-based application that allows users to draw and paint virtually using hand gestures detected by a webcam. The project utilizes the following technologies and concepts:

1. OpenCV: The OpenCV library is used for image and video processing. It provides functions for webcam access, image manipulation, and drawing on images.

2. Mediapipe: Mediapipe is a framework for building multimodal (audio, video, etc.) applied ML pipelines. In this project, it is used for hand tracking and detecting hand landmarks.

3. Hand Tracking: The project includes a custom module called "ch1_HandTracking," which uses the mediapipe library to detect and track the user's hand in real-time.

4. User Interface: The application presents a graphical user interface where the user can interact with different virtual drawing tools and colors. The UI includes a header section with various options, which can be selected by hovering the hand over specific regions on the screen.

5. Drawing and Painting: The user can draw on a virtual canvas by moving their index finger. Different colors and brush thicknesses are available, and an eraser tool can be used to remove parts of the drawing. The canvas is displayed in real-time on the screen.

Overall, this project combines computer vision techniques, hand tracking, and image processing to create an interactive virtual painting experience. Users can express their creativity without the need for physical drawing tools or materials.
