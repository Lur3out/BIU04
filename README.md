# BIU04
## Application Programming Interface
>В разработке...

## API Unix Service
>Edit and copy service file by next command
```
cp api.service /lib/systemd/system/api.service
```
>Enable service
```
sudo systemctl enable api.service
```
>Start service
```
sudo systemctl start api.service
```

## Подключение Arduino
В данном коде используется /dev/ttyS0, поскольку устройство подключено через COM порт VirtualBox.
