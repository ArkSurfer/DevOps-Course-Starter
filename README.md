# DevOps Apprenticeship: Project Exercise

To create create either a development or production image use below commands: 
```
docker build --target development --tag todo-app:dev . 
docker build --target production --tag todo-app:prod .  
```

Docker run commands:
```
docker run --env-file ./.env -p8000:8000 --mount type=bind,source="$(pwd)"todo_app,target=/app/todo_app todo-app:prod
docker run --env-file ./.env -p5000:5000 --mount type=bind,source="$(pwd)"todo_app,target=/app/todo_app todo-app:dev
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.
