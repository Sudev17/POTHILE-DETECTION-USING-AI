from flask import Flask, render_template, request, send_file
from ultralytics import YOLO
import cv2
import os
import time
import uuid
import webbrowser

app = Flask(__name__)  # Fix here: __name__, not _name_
model = YOLO('best.pt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['video']
        os.makedirs('uploads', exist_ok=True)
        os.makedirs('static', exist_ok=True)

        input_path = os.path.join('uploads', file.filename)
        unique_id = uuid.uuid4().hex
        mp4_output = os.path.join('static', f"output_{unique_id}.mp4")

        file.save(input_path)

        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            return "❌ Failed to open video file."

        fps = cap.get(cv2.CAP_PROP_FPS) or 20
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if width == 0 or height == 0:
            return "❌ Invalid video file."

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        mp4_writer = cv2.VideoWriter(mp4_output, fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            for result in results:
                for box in result.boxes:
                    cls = int(box.cls)
                    label = model.names[cls]
                    conf = box.conf.item()
                    if label.lower() == "pothole" and conf > 0.5:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            mp4_writer.write(frame)

        cap.release()
        mp4_writer.release()

        ts = int(time.time())
        return render_template('index.html', video_output=f"output_{unique_id}.mp4", timestamp=ts)

    return render_template('index.html', video_output=None)

@app.route('/static/<filename>')
def serve_static(filename):
    return send_file(f'static/{filename}', mimetype='video/mp4')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Use Render's port or default
    app.run(host='0.0.0.0', port=5000, debug=true)
