FROM python:3.8-slim
RUN pip install opencv-python-headless tqdm
COPY obj_detect_video.py /app/
WORKDIR /app/
ENTRYPOINT ["python", "obj_detect_video.py"]
