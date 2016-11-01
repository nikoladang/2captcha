# 2captcha
* This project is a folk from Mirio/captcha2upload
* Fix so that it can work with Python3

# 2Captcha
2Captcha team solves your CAPTCHA with high accuracy

## How to install?

### pip
```
pip install 2captcha
```

### Source
```
git clone https://github.com/nikoladang/2captcha.git
cd 2captcha
python setup.py install
```

## How to start?
[Register Here](http://2captcha.com/?from=2529829)
And get the api key:
* Login in your account
* Go to "2Captcha API"
* Get "CAPTCHA Key"

# Example

## Solve Captcha
```
from 2captcha import CaptchaUpload

captcha = CaptchaUpload(<YOURKEY>)
print captcha.solve(<PATHFILE>)
```

## Get balance
```
from 2captcha import CaptchaUpload

captcha = CaptchaUpload(<YOURKEY>)
print captcha.getbalance()
```

## Attach the logs
```
from 2captcha import CaptchaUpload

captcha = CaptchaUpload(<YOURKEY>, log=<YOURLOGVAR>)
print captcha.getbalance()
```

## Change Wait Time
```
from 2captcha import CaptchaUpload

captcha = CaptchaUpload(<YOURKEY>, waittime=<YOURLOGVAR>)
print captcha.solve(<PATHFILE>)
```
