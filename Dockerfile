FROM public.ecr.aws/docker/library/python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
CMD ["python", "main.py"]
EXPOSE 5000
