key="xxxx-xxxx-xxxx-xxxx"
read -p "$key" -p "Please enter your YouTube Streamkey: " input
key="${input:-$key}"
sudo docker run --privileged --name cam -ti alexellis2/streaming:latest $key
