## PyImgur

 Python IMGUR API wrapper


 Usage example:

```
In [1]: from pyimgur import UploadImage as U

In [2]: a = U('roosevelt.jpg')

In [3]: a.imageURL.keys()
Out[4]: ['url', 'bigthumb', 'deletehash', 'hash', 'smallthumb']

In [4]: a.imageURL['url']
Out[4]: u'http://i.imgur.com/cUWzn.jpg'

In [5]: a.error
Out[5]: []
```

__Make sure to set anonymous imgur key.__

* Get your anon key here:
* Copy local_settings.py.dist to local_settings.py
* Edit local_settings.py and set ANNON_KEY