# 入退室管理システム

## 環境構築
### on Raspberrypi OS
nfcpyをインストール

```shell
$ pip install nfcpy
```

プログラム実行時に以下のエラーが出た場合

```shell
$ python main.py
Traceback (most recent call last):

...

OSError: [Errno 19] No such device
```

以下のコマンドを実行し、そこに書かれている手順に従う

```shell
$ python -m nfc

...

-- better assign the device to the 'plugdev' group
   sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
   sudo udevadm control -R # then re-attach device

...

Sorry, but I couldn't find any contactless device
```

と出ていたら

```shell
$ sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
$ sudo udevadm control -R
```

を実行して再起動

