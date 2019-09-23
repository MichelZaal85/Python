import pyqrcode

qr_info = 'Lieve Jade, Ik houd van jou en ben voor eeuwig van jou. Kusjes jouw prins xxx'
qr = pyqrcode.create(qr_info)
qr.png('Liefde.png', scale=10)
