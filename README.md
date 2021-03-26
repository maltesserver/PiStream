# PiStream
Automatic Tool that Livestreams to Youtube

## What you need
* Raspberry Pi 
* Rasbperry Pi Camera Module


#### ⚠️ This tool only works with the Raspberry Pi Camera module


## Installation

#### Download Docker 

```
curl -sSL https://get.docker.com | sh

sudo usermod pi -aG docker

reboot
```

#### Copy the Files from this Github

```
git clone https://github.com/maltesserver/PiStream.git
```

To test your camera: 

```bash
sudo raspistill -o test.jpg
```

## Usage

#### Insert your YouTube Stream Key 

* run streamwithkey.sh

or 

* edit the file stream.sh and insert your key manually

#### To change your Stream Key

* run the file remove.sh
* run the file streamwithkey.sh

or 

* run the file remove.sh
* add the key manually into stream.sh

## Start the stream

* Run the file streamwithkey.sh and insert your Streamkey

or if you have already added the key manually
* start.sh

or 
```shell
sudo docker start cam
```

## Stop the stream 

* Press CTRL+c
or 
* Unplug the Pi
