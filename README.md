# PyImgur

_Python IMGUR API wrapper_

Requirements:

*pycurl
*anonomous key from imgur
 
### Usage example:

```
In [1]: from pyimgur import UploadImage as U

In [2]: a = U('roosevelt.jpg')

In [3]: a.imageURL.keys()
Out[4]: ['url', 'bigthumb', 'deletehash', 'hash', 'smallthumb']

In [4]: a.imageURL['url']
Out[4]: u'http://i.imgur.com/cUWzn.jpg'

In [5]: a.error
Out[5]: []

In [6]: b = U(dhash="1IRyqQVh9BokqEs", delete=True)

In [7]: b.message
Out[7]: ['Success!']

In [8]: b.error
Out[8]: []
```

__Make sure to set anonymous imgur key.__

* Get your anon key here: http://imgur.com/register/api_anon
* Copy local_settings.py.dist to local_settings.py
* Edit local_settings.py and set ANNON_KEY
* 

### Using the handler `handler.py` as a simple interface
```bash
alias grabs="scrot -s -e 'python handler.py \$f'"
```
Now just run `grabs` in your terminal, select your region, and watch the magic (browser opens uploaded image and you have the link in your clipboard).

### Using the handler
The `handler.py` file is a quick example of integrating PyImgur with your system.
To be able to right click on images and shoot them to Imgur with PyImgur, you can add a custom action 
by clicking `Edit->Configure custom actions...` and then follow the images below for a walk-through.
After upload, the script will open the newly uploaded file on Imgur in your system web browser for you to view and share.
_You can also choose to show only on image files in the context portion of the second tab `Appearance Conditions` when configuring._




![PyImgur Thunar Setup](http://mutaku.com/pyimgur_thunar1.png)
![PyImgur Thunar Upload](http://mutaku.com/pyimgur_thunar2.png)
![PyImgur Thunar Browser Success](http://mutaku.com/pyimgur_thunar3.png)
