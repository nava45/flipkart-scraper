nohup python2.7 redis_worker.py >> worker.out &
sleep 1
nohup python2.7 app.py >> recv.out &
echo "Visit the url: http://127.0.0.1:8802/"
echo "http://127.0.0.1:8802/"
