微信自定义菜单管理模块
=================

基于django-wechat-base的简单微信自定义管理模块

快速开始:
---------

安装django-wechat-menu:

.. code-block::

    pip install django-wechat-menu

修改settings.py文件:

.. code-block::

    INSTALLED_APPS = (
        ...
        'wechat',
        'wechat_menu',
        ...
    )

在settings.py文件底部添加:

.. code-block::

    # wechat config
    WECHAT = [
        {
            'appid': 'demo',
            'appsecret': 'demo',
            'token': 'demo',
        },
    ]


版本更改:
---------
