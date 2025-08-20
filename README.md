# 🎮 Subway Surfers Hand Control

A Python application that allows you to control Subway Surfers using hand gestures captured through your webcam. Control your character with simple swipe gestures - no keyboard or mouse needed!

## ✨ Features

- **Hand Gesture Recognition**: Uses MediaPipe for accurate hand tracking
- **Fast Response**: Optimized swipe detection with low latency
- **Intuitive Controls**: Natural hand movements for game control
- **Real-time Processing**: Live webcam feed with gesture overlay
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🎯 How It Works

The application tracks your index finger through your webcam and translates hand movements into keyboard inputs:

- **👈 Swipe Left** → Move character left
- **👉 Swipe Right** → Move character right  
- **👆 Swipe Up** → Jump
- **👇 Swipe Down** → Duck

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Webcam
- Subway Surfers game (or any game that uses arrow keys)

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Manoj20705/subway_surfers_hand_control.git
   cd subway_surfers_hand_control
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Position your hand** in front of the webcam
3. **Make swipe gestures** to control the game:
   - Move your index finger left/right to move the character
   - Swipe up to jump
   - Swipe down to duck
4. **Press 'q'** to quit the application

## ⚙️ Configuration

You can adjust the sensitivity and response time by modifying these values in `main.py`:

```python
SWIPE_THRESHOLD = 30   # Lower = more sensitive
COOLDOWN = 0.15        # Lower = faster response
```

## 📋 Requirements

- `opencv-python` - Computer vision library
- `mediapipe` - Hand tracking and gesture recognition
- `pyautogui` - Keyboard input simulation
- `keyboard` - Additional keyboard control

## 🔧 Troubleshooting

### Common Issues

1. **Webcam not detected**
   - Ensure your webcam is connected and not in use by other applications
   - Check webcam permissions

2. **Gesture detection not working**
   - Ensure good lighting conditions
   - Keep your hand clearly visible in the camera frame
   - Try adjusting the `SWIPE_THRESHOLD` value

3. **Game not responding**
   - Make sure the game window is active/focused
   - Verify that the game uses arrow keys for movement

### Performance Tips

- Use a well-lit environment for better hand detection
- Keep your hand steady and clearly visible
- Close unnecessary applications to free up system resources

## 🎯 Game Compatibility

This application works with any game that uses arrow keys for movement:
- Subway Surfers
- Temple Run
- Other endless runner games
- Any game with arrow key controls

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking capabilities
- [OpenCV](https://opencv.org/) for computer vision functions
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for automation features

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Ensure all dependencies are properly installed

---

**Happy gaming! 🎮✨**

*Made with ❤️ by [Manoj20705](https://github.com/Manoj20705)*
