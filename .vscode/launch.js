{
  "version": "0.2.0",
  "configurations": [
      {
          "name": "Python: Django",
          "type": "python",
          "request": "launch",
          "program": "${workspaceFolder}/manage.py",
          "args": ["runserver"],
          "django": true,
          "autoReload":{
              "enable": true
          }
      }
  ]
}
