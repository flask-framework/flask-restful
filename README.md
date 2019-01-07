# flask-restful
基于flask的restful api项目结构

### 项目依赖
- flask>=1.0.2
- flask_restful>=0.3.6
- flask_sqlalchemy>=2.3.2
- flask_uploads>=0.2.1
- Flask_Babel>=0.11.2
- celery>=4.2.1
- redis>=2.10.6
- flask-session>=0.3.1
- Geoalchemy2>=0.5.0
- psycopg2-binary>=2.7.6.1
- PyJWT>=1.7.1
- flask-cors>=3.0.7

### 配置文件说明(core.settings)
    
- INSTALL_APPS 

    安装的应用app，类似于django
    
- BASE_DIR 

    项目根目录
    
- DEBUG 

    调试模式
    
- SECRET_KEY

    加密字符串
    
- SQLALCHEMY_DATABASE_URI

    flask-sqlalchemy URI数据库配置
    
- SQLALCHEMY_ECHO

    flask-sqlalchemy 是否打印
    
- SQLALCHEMY_POOL_SIZE

     flask-sqlalchemy 数据库连接池配置
     
- SQLALCHEMY_TRACK_MODIFICATIONS

    如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。

- SESSION_COOKIE_NAME

    客户端cookie中session id的名称

- SESSION_TYPE

    session类型redis、mongodb和sqlalchemy

- SESSION_REDIS

    session配置redis的路径redis://

- PERMANENT_SESSION_LIFETIME

    session持续时间

- UPLOADED_FILES_DEST

    上传文件路径

- UPLOADED_FILES_URL

    上传文件URL

- UPLOADED_FILES_ALLOW

    允许上传文件类型

- UPLOADED_FILES_DENY

    屏蔽上传文件类型

- BABEL_DEFAULT_LOCALE

    国际化语言

- BABEL_DEFAULT_TIMEZONE

    国际化时区

- PAGE_SIZE

    分页大小

- JWT_EXPIRED

    JWT过期时间

- JWT_MODEL

    JWT认证用户模型

### 使用

#### app包
  
  - 文件目录

      - urls.py
            
        路由模块，例如：urlpatterns = []
           
      - views.py
      
        视图模块
        
      - validators.py
      
        参数校验模块
        
      - exceptions.py
      
        自定义异常类模块
        
      - serializers.py
      
        序列化模块
        
  - 安装使用
    
      在core.settings配置中的INSTALL_APP列表中添加该包名称，系统会自动查找该包下的urls.py，并且加载该模块里面的urlpatterns列表中所有路由和视图关系
      
### wsgi应用

  需要安装uwsgi或者其他的辅助工具进行wsgi应用启动，配合nginx代理，以达到高并发的相应，这里只展示uwsgi配置。
  
  - uwsgi配置示例
  
    ```ini
    [uwsgi]
    uid = root                                          # 执行用户，root用户危险，请谨慎使用
    gid = root                                          # 执行组，请谨慎使用
    
    master = true                                       # 
    processes = 2                                       # 启动进程个数，视情况而定
    listen = 120                                        # 监听等待队列大小，视情况而定
    socket = 127.0.0.1:9000                             # 代理IP地址
    pidfile = /usr/local/software/uwsgi/uwsgi.pid       # uwsgi进程编号文件
    vacuum = true                                       # 是否在前台启动，设置true
    daemonize = /usr/local/software/uwsgi/uwsgi.log     # uwsgi日志路径
    chdir = /usr/local/software/project                 # 项目文件目录
    home=/usr/local/software/env                        # virtualenv目录
    buffer-size = 32768                                 # 交换buffer大小，视情况而定
    module = manage                                     # 启动模块名称
    callable = app                                      # wsgi调用应用名称
    # http-websockets = true                            # websocket配置，需要请打开注释
    # gevent = 1000                                     # gevent配置，需要请打开注释
    ```
    
    其他配置请参考模块[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
    
  - nginx配置示例
  
  ```shell
    server {
        listen       90;
        server_name  test.com;
        charset UTF-8;
        
        # socketio配置，需要开打注释
        # location ^~ /socket.io/ {
        #        include uwsgi_params;
        #        proxy_redirect off;
        #        proxy_buffering off;

        #        proxy_set_header Host $host;
        #        proxy_set_header X-Real-IP $remote_addr;
        #        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        #        proxy_http_version 1.1;
        #        proxy_set_header Upgrade $http_upgrade;
        #        proxy_set_header Connection "Upgrade";

        #        uwsgi_pass 127.0.0.1:9000;
        #}
        location ^~ /api/ {
                include uwsgi_params;
                uwsgi_pass 127.0.0.1:9000;
                client_max_body_size 100m;
        }
        location ^~ /static/ {
                alias /usr/local/src/software/project/static/;
        }
}
  ```
  
### 示例

- [flask-restful完整示例](https://github.com/flask-framework/flask-restful-example)