# Dockerized Flask App R2D

Dockerized flask app template ready for deployment on Heroku

## How to make it work

### Changes and local testing

1. Create the virtual environment you will be using locally
2. Install the required packages by activating the venv and running 
`pip install -r requirements.txt`
3. Make the changes you want and need to the endpoints in `app.py`

For testing build and run the docker container locally

### Deployment to Heroku

For the next steps you need Heroku CLI installed

Log in to heroku
1. `heroku login`

Create the Heroku app

2. `heroku create <app-name>`

Add the remote branches

3. `git remode add <branch-name> <heroku-git-url>` 

4. `heroku stack:set container`
5. `git push <heroku-git-url> master`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
