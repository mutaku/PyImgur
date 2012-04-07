## PyImgur

## Python IMGUR API wrapper


# Usage example:

```
In [1]: from pyimgur import UploadImage as U

In [2]: a = U('roosevelt.jpg')

In [3]: a.imageURL.url
Out[3]: u'http://i.imgur.com/cUWzn.jpg'

In [4]: a.error
Out[4]: []
```

__Make sure to set anonymous imgur key.__
