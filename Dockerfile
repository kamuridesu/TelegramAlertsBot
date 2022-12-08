FROM python:3-slim
RUN pip3 install python-telegram-bot==13.10
RUN pip3 install Flask==2.0.1
COPY api.py .
CMD ["python", "api.py"]
