# MotionDetectionAPI

Flask API for handling motion detections from PicoMotionDetectors

---

### Setup

1. Configure Discord Bot / Webhook `DiscordConfig` in `config.py`.
3. Setup Docker container:
   1. Build image: 
   ```
   sudo docker build -t motiondetectionapi .
   ```
   2. Run container:
   ```
   sudo docker run -d \
    -p 8080:8080 \
    -v <path_to_data_dir>:/MotionDetectionAPI/logs \
    -v /etc/timezone:/etc/timezone:ro \
    -v /etc/localtime:/etc/localtime:ro \
    --name motiondetectionapi motiondetectionapi
   ```
   3. Make container auto startup:
   ```
   sudo docker update --restart unless-stopped motiondetectionapi
   ```
