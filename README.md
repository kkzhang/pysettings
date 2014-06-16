pysettings
==========

Simple Settings component which can be configured under multiple environment for any python project

Installation
====

    pip install -e git+https://github.com/kkzhang/pysettings.git

Creating setting files
====

Create settings file for your project:

    pysettings init

This command will settings folder under current path. Or you can specify your own folder name by --dir:

    pysettings init --dir=mysettings

By default, pysettings create development and production settings files for you. you can specify your own environments:

    pysettings init myenv1 myenv1

The first environment name is set to be default. You can set it by --default

    pysettings init myenv1 myenv2 --default=myenv2

`pysettings` file structure:

    Your project
      settings
        myenv1.py
        myenv2.py
      settings.py

--myapp.py

`SettingBase` in settings.py is your default setting for all environments. It is overridden by  <current_env>.py

Usage
====

Edit setting file myenv1.py:

    class Settings:
        mykey1 = "Helloworld"

In your py file, eg myapp.py:

    from settings.settings import settings

    print setting.mykey1

If everything go fine, will print `Helloworld`
