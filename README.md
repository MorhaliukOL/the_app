# the_app
Django web application where users can register, edit/delete their profiles and see profiles of other users using API,
build with Django-Rest-Framework (DRF).

The project is deployed on Heroku server. To explore admin web interface you can log in using\
*username*: `Admin`\
*password*: `admin`\
[https://prof1le-app.herokuapp.com/admin/](https://prof1le-app.herokuapp.com/admin/)

# Available endpoints
#### Register a new user:
`https://prof1le-app.herokuapp.com/auth/users/ -d "username=<username>&password=<user_password>"`
#### Get JSON Web Token (JWT). It is needed to access protected endpoints.
`https://prof1le-app.herokuapp.com/auth/jwt/create/`\
`-d "username=<username>&password=<user_password>"`
#### Retrieve profiles of all users:
`https://prof1le-app.herokuapp.com/profile/list/`
#### Retrieve one specific profile:
`https://prof1le-app.herokuapp.com/profile/<profile_id>/`
#### Delete profile:
`https://prof1le-app.herokuapp.com/profile/2/ -X DELETE -H "Authorization: Bearer <JWT>"`
#### Create profile:
`https://prof1le-app.herokuapp.com/profile/list/`\
`-X POST`\
`-d "description=<user_description>&country=<user_country>&city=<user_city>"`\
`-H "Authorization: Bearer <JWT>`
#### Update profile:
`https://prof1le-app.herokuapp.com/profile/11/`\
`-X PUT`\
`-d "description=<new_description>&country=<new_country>&city=<new_city>"`\
`-H "Authorization: Bearer <JWT>`
