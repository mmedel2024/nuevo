docker stop webservice || true

docker run -itd --rm --name webservice -p 3000:3000 proyecto_img:1.0

