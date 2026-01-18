# :cat: Silly Catmera

A real-time facial expression and hand gesture recognition program displaying silly cat images to match your mood, using OpenCV and Google MediaPipe.

### :triangular_ruler: Project Structure

The project is split into 4 principal Python scripts :
- `main.py` : Handles the animation loop and ties other scripts together.
- `silly_cater.py` : Contains the Google MediaPipe logic for faces and hands detection.
- `capture.py` : Manages the video capture and frame conversion.
- `display.py` : Initializes the Matplotlib window layout.  

The cat images are all located in the `silly_cats` folder.
Models used for facial and gesture recognition are in the `models` folder.

### :rocket: Installation

**1. Clone the GitHub repository:**
```bash
git clone https://github.com/tom-perrin/silly_catmera.git
```

**2. Install dependencies:** 
```bash
pip install -r requirements.txt
```

**3. Run the app:** 
```bash
python main.py`
```

### :brain: Logic Hierarchy

The app has the following priority system during recognition :
- **Gestures:** If a hand is detected (ThumbsUp, Victory, ...), the corresponding cat will be shown directly.
- **Expressions:** If no gesture is present, the app analyses facial blenshapes (smile, sad, ...).
- **Default:** If no particular movement is detected, the app default to `larry` (neutral).

### :hammer_and_wrench: Troubleshooting

In case some images are not appearing, you can uncomment the Debugging section of the `detect_expression` function in `silly_cater.py` in order to see the top scores for face blenshapes in real-time.  
You can also customize the threshold values in the same function.  
Feel free to add more cat images and include them in the `CAT_MAP` dictionary (currently, all image files are in .jpg format).

### :star: Credits

This project is inspired by a very creative Instagram reel of Shana Nursoo (@reinesana) !  
This project is licensed under the MIT License - see the LICENSE file for details.
