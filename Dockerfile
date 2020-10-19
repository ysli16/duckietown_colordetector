FROM duckietown/dt-duckiebot-interface:daffy-arm32v7

#WORKDIR /color_detector_dir

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY color_detector.py .

CMD python3 ./color_detector.py
