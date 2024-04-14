FROM python:3.9
WORKDIR /app2
COPY prediction.py /app2/
COPY model33.pkl /app2/
COPY price.csv /app2/
RUN pip install numpy scikit-learn pandas pickle
CMD ["python", "prediction.py","model33.py","price.csv"]
