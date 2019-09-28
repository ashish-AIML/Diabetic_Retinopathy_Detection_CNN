import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

img_width, img_height = 150, 150
model_path = r'C:\Users\Kiran\Desktop\Major Project\CNN-Image-Classifier\src\models\model.h5'
model_weights_path = r'C:\Users\Kiran\Desktop\Major Project\CNN-Image-Classifier\src\models\weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("Label: No_DR")
  elif answer == 1:
    print("Labels: Mild_DR")
  elif answer == 2:
    print("Label: Moderate_DR")
  elif answer == 3:
    print("Label: Severe_DR")
  elif answer == 4:
    print("Label: PDR")


  return answer

No_DR_t = 0
Mild_DR_t = 0
Moderate_DR_t = 0
Severe_DR_t = 0
PDR_t = 0
No_DR_f = 0
Mild_DR_f = 0
Moderate_DR_f = 0
Severe_DR_f = 0
PDR_f = 0

for i, ret in enumerate(os.walk(r'C:\Users\Kiran\Desktop\Computer Vision\IEEE DR dataset\B. Disease Grading\data\validation\0')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Label: No_DR")
    result = predict(ret[0] + '/' + filename)
    if result == 0:
      No_DR_t += 1
    else:
      No_DR_f += 1

for i, ret in enumerate(os.walk(r'C:\Users\Kiran\Desktop\Computer Vision\IEEE DR dataset\B. Disease Grading\data\validation\1')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Label: Mild_DR")
    result = predict(ret[0] + '/' + filename)
    if result == 1:
      Mild_DR_t += 1
    else:
      Mild_DR_f += 1

for i, ret in enumerate(os.walk(r'C:\Users\Kiran\Desktop\Computer Vision\IEEE DR dataset\B. Disease Grading\data\validation\2')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Label: Moderate_DR")
    result = predict(ret[0] + '/' + filename)
    if result == 3:
      Moderate_DR_t += 1
    else:
      Moderate_DR_f += 1

for i, ret in enumerate(os.walk(r'C:\Users\Kiran\Desktop\Computer Vision\IEEE DR dataset\B. Disease Grading\data\validation\3')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Label: Severe_DR")
    result = predict(ret[0] + '/' + filename)
    if result == 4:
      Severe_DR_t += 1
    else:
      Severe_DR_f += 1

for i, ret in enumerate(os.walk(r'C:\Users\Kiran\Desktop\Computer Vision\IEEE DR dataset\B. Disease Grading\data\validation\4')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    print("Label: PDR")
    result = predict(ret[0] + '/' + filename)
    if result == 2:
      PDR_t += 1
    else:
      PDR_f += 1
"""
Check metrics
"""
print("True No_DR: ", No_DR_t)
print("False No_DR: ", No_DR_f)
print("True Mild_DR: ", Mild_DR_t)
print("False Mild_DR: ", Mild_DR_f)
print("True Moderate_DR: ", Moderate_DR_t)
print("False Moderate_DR: ", Moderate_DR_f)
print("True Severe_DR: ", Severe_DR_t)
print("False Severe_DR: ", Severe_DR_f)
print("True PDR: ", PDR_t)
print("False PDR: ", PDR_f)
