FROM python:3.12
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app/
CMD ["sh", "-c", "python manage.py migrate && \
                    python manage.py load_ingredients ./data/ingredients.json && \
                    python manage.py collectstatic --noinput && \
                    gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000"]