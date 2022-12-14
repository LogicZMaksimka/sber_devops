minikube start

kubectl delete -f web.yml
kubectl delete -f postgres.yml
kubectl create -f postgres.yml
kubectl create -f web.yml

minikube service web-service --url