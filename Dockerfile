# Build:  docker build -t emx-docs .
# Run:    docker run -d -p 8080:80 emx-docs      ->  http://localhost:8080/
#
# Stage 1 needs internet access (pip). For a closed network build the image on a
# connected machine and move it with `docker save` / `docker load` (see README).

FROM python:3.12-slim AS build
WORKDIR /src
COPY requirements.in ./
RUN pip install --no-cache-dir -r requirements.in
COPY . .
RUN python build.py --no-install

FROM nginx:1.27-alpine
COPY --from=build /src/site /usr/share/nginx/html
EXPOSE 80
