FROM nikolaik/python-nodejs:python3.10-nodejs16
WORKDIR /usr/project
COPY . .
# RUN sed -i 's/\r$//' ./scripts/**/*.sh
RUN ls -la
RUN npm run setup:ci && npm ci
RUN npm test
EXPOSE 8000
ENTRYPOINT ["python", "webapp/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
