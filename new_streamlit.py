import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np
import time

import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.preprocessing import image


# Judul Aplikasi
st.title("Corn Leaf Classification")
st.markdown("Upload an image to predict if the corn leaf is healthy or diseased.")

def main():
    file_uploaded = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    classify_button = st.button("Classify")

    if file_uploaded is not None:
        img = Image.open(file_uploaded)
        st.image(img, caption="Uploaded Image", use_column_width=True)

    if classify_button:
        if file_uploaded is None:
            st.error("Please upload an image before classifying!")
        else:
            with st.spinner("Classifying..."):
                prediction = predict(img)
                st.success("Classification Complete")
                st.write(prediction)
def predict(img):
    classifier_model_path = "corn_leaf_classifier.h5"

    try:
        model = load_model(classifier_model_path)
    except Exception as e:
        return f"Error loading model: {e}"

    # Preprocess image
    try:
        img = img.resize((256, 256))
        img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
    except Exception as e:
        return f"Error processing image: {e}"

    # Prediction
    try:
        predictions = model.predict(img_array)
        print("Raw Predictions:", predictions)

        if predictions is None or len(predictions) == 0:
            return "Model returned no predictions."

        if len(predictions.shape) != 2 or predictions.shape[1] != 4:  # Ubah ke 4
            return f"Unexpected prediction shape: {predictions.shape}"

        confidence = tf.nn.softmax(predictions[0]).numpy()
        print("Confidence Scores:", confidence)

        class_names = {
            0: "Blight",       # Sesuaikan nama kelas sesuai data Anda
            1: "Common_Rust",
            2: "Gray_Leaf_Spot",
            3: "Healthy"
        }

        predicted_class = class_names[np.argmax(confidence)]
        confidence_score = 100 * np.max(confidence)
    except Exception as e:
        return f"Error during prediction: {e}"

    return f"{predicted_class} with {confidence_score:.2f}% confidence."

if __name__ == "__main__":
    main()

