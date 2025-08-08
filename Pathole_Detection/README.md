 🚧 Pothole Detection Web App using YOLOv8 and Flask

A simple and interactive web application that detects potholes in uploaded videos using the YOLOv8 object detection model. Designed for public infrastructure monitoring, smart cities, and real-time road damage assessment.

✅ Live Demo

> ⚠️ This is a local deployment project. To deploy online, use services like **Render**, **Railway**, or **Firebase Hosting** (for frontend).

---

📌 Features

* 🧠 **YOLOv8 Integration** – Detect potholes with high accuracy using a pre-trained `best.pt` model.
* 🎥 **Video Upload** – Upload `.mp4` road surveillance videos for pothole detection.
* 📦 **Output Preview** – Returns a downloadable processed video with potholes highlighted.
* 💡 **Auto Folder Management** – Automatically creates folders for uploads and outputs.
* 🌐 **Browser-based Interface** – No local UI needed; runs in your browser.

---

 🗂 Folder Structure

Make sure your project directory has the following structure:

```
.
├── app.py
├── templates/
│   └── index.html
├── static/               ← (Output videos will be saved here)
├── uploads/              ← (Uploaded input videos are stored here)
├── best.pt               ← (YOLOv8 trained weights for pothole detection)
├── requirements.txt
└── README.md
```

> 📝 **Note:** Create empty folders `uploads/` and `static/` before running the app.

---

⚙️ Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```txt
Flask
ultralytics
opencv-python
```

---
🚀 How to Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/pothole-detection-webapp.git
   cd pothole-detection-webapp
   ```

2. **Ensure folders exist**:

   ```bash
   mkdir uploads static
   ```

3. **Add your YOLO model**
   Place your trained YOLOv8 `.pt` file in the root directory as `best.pt`.

4. **Run the Flask App**:

   ```bash
   python app.py
   ```

5. **Open in browser**:
   Navigate to `http://localhost:5000` in your browser.

---
🧠 Model Details

* **Model Used:** YOLOv8 (`best.pt`)
* **Trained On:** Pothole dataset (custom or Kaggle dataset)
* **Framework:** [Ultralytics](https://docs.ultralytics.com/) YOLOv8

---

📽️ Output Sample

Once processed, the app returns a video where each detected pothole is:

* Highlighted with a red bounding box
* Annotated with confidence scores

---

🌐 Deployment Tips

To deploy online:

* Use **Render** or **Railway** for backend Flask hosting.
* Use **Firebase Hosting** if your frontend is separated.
* Ensure to modify the port in `app.py` to match the hosting environment.



Would you like me to generate a `templates/index.html` file too? Let me know if you're deploying this to GitHub right now—I’ll help with the `.gitignore` and commit structure too.
