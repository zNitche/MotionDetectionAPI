# MotionDetectionAPI

Flask API for handling motion detections from [PicoMotionDetectors](https://github.com/TheZodiaCC/PicoMotionDetector)

---

### Setup

1. Configure Discord Bot / Webhook `DiscordConfig` in `config.py`.
2. Change `AUTH_TOKEN` in `config.py`.
3. Setup Docker container:
   1. Build image: 
   ```
   sudo docker build -t motion_detection_api .
   ```
   2. Run container:
   ```
   sudo docker run -d \
    -p 8080:8080 \
    -v <path_to_data_dir>:/MotionDetectionAPI/logs \
    -v /etc/timezone:/etc/timezone:ro \
    -v /etc/localtime:/etc/localtime:ro \
    --name motion_detection_api motion_detection_api
   ```
   3. Make container auto startup:
   ```
   sudo docker update --restart unless-stopped motion_detection_api
   ```
