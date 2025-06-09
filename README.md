# FocusLens 🔍  
**Interactive Image Masking & Blurring Tool using OpenCV**

![Demo](demo.gif)

---

## ✨ Features  
- 🎛 Adjustable **mask position** (`X`, `Y`) and **size** via sliders  
- 🌫 Control **blur intensity** interactively with a **blur kernel slider**  
- 🧠 Uses OpenCV’s `cv2.blur()` with a dynamic **kernel size**  
- ⚡ Real-time visual updates  
- 🖼 Plug-and-play: just replace the image file (`street.jpg`)  

---

## 🚀 How It Works  
1. Loads and resizes your image  
2. Draws a white rectangular mask on a black background  
3. Applies a **uniform blur** using OpenCV’s `cv2.blur()`  
   - The **kernel size (k × k)** is adjusted with the `Blur` slider  
   - Must be an **odd number**, automatically handled in code  
4. Combines the **sharp masked area** with the **blurred background**  
5. Shows the final result in a single OpenCV window  

---

## 🛠 Requirements  
- Python 3.x  
- `opencv-python`  
- `numpy`  
