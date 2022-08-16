FROM python:3 
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "DigitalCV_CourseRecommendation_AssociationRule.py"]
CMD ["python", "app.py"]