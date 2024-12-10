
---

# 🌽 Corn Leaf Disease Classification  

This repository contains a project that uses a pre-trained machine learning model to classify diseases on corn leaves. The project includes a **Streamlit-based web application** for easy interaction and deployment.  

---

## 📜 Table of Contents  
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Setup](#setup)  
5. [Usage](#usage)  
6. [Deployment](#deployment)  
7. [License](#license)  

---

## 🌟 Introduction  
Corn is a vital crop worldwide, and early detection of leaf diseases is critical for maximizing yield. This project focuses on:  
1. Providing an interactive web application using **Streamlit**.  
2. Enabling predictions using a trained classification model (`corn_leaf_classifier.h5`).  

The app predicts the condition of a corn leaf (e.g., Blight, Common Rust, Gray Leaf Spot, or Healthy) with confidence scores.  

---

## ✨ Features  
- **Streamlit Web App**: User-friendly interface for uploading and classifying leaf images.  
- **Pre-trained Model**: Efficient classification with `corn_leaf_classifier.h5`.  
- **Error Handling**: Robust validation for image uploads and model predictions.  

---

## 📁 Project Structure  
```  
.  
├── .devcontainer/                # Development container configuration (optional)  
├── corn_leaf_classifier.h5       # Pre-trained model for classification  
├── new_streamlit.py              # Streamlit app script  
├── requirements.txt              # Dependencies for the project  
```  

---

## 🛠️ Setup  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/nnatureall/Corn_Leaf_Diseases_Classifier_With_CNN.git  
   cd corn-leaf-disease-classification  
   ```  

2. **Install Dependencies**:  
   Ensure Python is installed on your system (Python 3.8+ recommended). Install dependencies using:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the App**:  
   Launch the Streamlit app locally:  
   ```bash  
   streamlit run new_streamlit.py  
   ```  

---

## 🚀 Usage  

1. Open the Streamlit app in your browser (usually at `http://localhost:8501`).  
2. Upload an image of a corn leaf (supported formats: `.png`, `.jpg`, `.jpeg`).  
3. Click on the **Classify** button to predict the condition of the leaf.  

---

## 🌐 Deployment  

### Deploy on Streamlit Community Cloud  
1. Push the repository to GitHub.  
2. Visit [Streamlit Community Cloud](https://share.streamlit.io).  
3. Select your repository and set the entry point as `new_streamlit.py`.  
4. Deploy and share the app link!  

### Example URL:  
```  
https://cornleafdiseasesclassifierwithcnn-iqbkasqkm53kgctun5m2vj.streamlit.app/```  
---

## 📝 License  
This project is licensed under the [MIT License](LICENSE).  

Feel free to use, modify, and deploy this project for educational or research purposes.  

---  
