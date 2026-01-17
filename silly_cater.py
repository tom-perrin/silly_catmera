### Imports

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# --------------------------------------------------

### Script

# Cat images dictionary
CAT_MAP = {
    # Expressions
    'neutral': 'larry',
    'happy': 'happi',
    'shocked': 'chokbar',
    'sleepy': 'mimimi',
    'tongue': 'bleh',
    'wink': 'wink',
    'sad': 'sorrow',
    'pucker': 'duckyduck',

    # Gestures
    'Thumb_Up': 'oetrobien',
    'Victory': 'peace',
    'Pointing_Up': 'actually'
}

# Expression recognizer
base_options_expression = python.BaseOptions(model_asset_path='./models/face_landmarker.task')
options_expression = vision.FaceLandmarkerOptions(
    base_options = base_options_expression,
    output_face_blendshapes = True,
    output_facial_transformation_matrixes = True,
    num_faces = 1
    )
detector_expression = vision.FaceLandmarker.create_from_options(options_expression)

# Gesture recognizer
base_options_gesture = python.BaseOptions(model_asset_path='./models/gesture_recognizer.task')
options_gesture = vision.GestureRecognizerOptions(base_options=base_options_gesture)
detector_gesture = vision.GestureRecognizer.create_from_options(options_gesture)


def detect_expression(rgb_frame):
    '''
    Detects potential facial expression from a given rgb frame.
    Thresholds on the scores were set arbitrarily after testing.
    
    :param rgb_frame: RGB image
    '''
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    detection_result = detector_expression.detect(image)

    if not detection_result.face_blendshapes:
        return 'neutral'
    
    score = {b.category_name: b.score for b in detection_result.face_blendshapes[0]}

    # Debugging
    # sorted_scores = sorted(score.items(), key=lambda item: item[1], reverse=True)
    # print(f"Top Moves: {sorted_scores[:3]}", end='\r')

    # Known expressions
    if score['mouthLowerDownLeft'] > 0.5 and score['mouthLowerDownRight'] > 0.5:
        return 'tongue'
    if score['mouthPucker'] > 0.85:
        return 'pucker'
    if score['jawOpen'] > 0.4:
        return 'shocked'
    if score['eyeBlinkLeft'] > 0.5 and score['eyeBlinkRight'] > 0.5:
        return 'sleepy'
    if score['mouthSmileLeft'] > 0.65 and score['mouthSmileRight'] > 0.65:
        return 'happy'
    if score['mouthShrugLower'] > 0.8 and score['mouthShrugUpper'] > 0.4:
        return 'sad'
    if score['eyeBlinkLeft'] > 0.3 or score['eyeBlinkRight'] > 0.3:
        return 'wink'
    
    return 'neutral'


def detect_gesture(rgb_frame):
    '''
    Detects potential hand gestures from a given rgb frame.
    
    :param rgb_frame: RGB image
    '''
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    detection_result = detector_gesture.recognize(image)

    # Known gestures
    if detection_result.gestures:
        top_gesture = detection_result.gestures[0][0]
        if top_gesture.score > 0.5:
            return top_gesture.category_name
    
    return None


def cat_picker(rgb_frame):
    '''
    Decision engine to select silly cat.
    
    :param rgb_frame: Description
    :param detector: Description
    '''
    # Check gesture
    gesture_label = detect_gesture(rgb_frame)
    if gesture_label != None and gesture_label in CAT_MAP:
        return CAT_MAP[gesture_label]
    
    # Check expression
    expression_label = detect_expression(rgb_frame)
    if expression_label != None and expression_label in CAT_MAP:
        return CAT_MAP[expression_label]
    
    # Fallback
    return CAT_MAP['neutral']
    
# --------------------------------------------------

### Test