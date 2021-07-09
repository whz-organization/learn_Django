## Take Home Tests

### Exercise 1 (Django)

Use `api.serializers.CourseSerializer` to code a view 
at `api.views.CourseListView`. The view will serve a publicly available course 
listing API that will show `name` and `description` for each `Course`. Get the 
model attributes from the serializer to code the model (`courses.models.Course`)
as well.

The default sorting order for the listing will be by course name. 
*Both `name` and `description` attributes will be searchable* via another 
public endpoint that will be built later by your colleague.

The public API will be throttled. The throttle value is not important, but it 
should be changeable by editing the django settings file.

### Exercise 2 (VueJS)

Start the Vue development server. The site at `http://localhost:8080` should not
work. Figure out why it is not working and fix the bug, so the site shows 
the course listing API you created in Exercise 1.

## Setup

### Setup Django

Create a virtualenv:
```
cd take-home
virtualenv -p python3 venv
source venv/bin/activate
```

Install python dependencies and initialize the Django site:
```
# in directory take-home
cd django
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
```

Create a super user:
```
# in directory take-home
source venv/bin/activate
cd django
./manage createsuperuser
```

Start the server:
```
# in directory take-home
source venv/bin/activate
cd django
./manage.py runserver 8000
```

The admin site will be accessible at: `http://127.0.0.1:8000/admin/`

The API site will be accessible at: `http://127.0.0.1:8000/api/courses/`

### Setup Vue
Change directory into `vuejs`.
```
# in directory take-home
cd vuejs
```

Install `nvm` if you don't already have it
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
```

Install `npm` dependencies
```
# in directory take-home/vuejs
nvm use
npm install
```

Start the Vue development server
```
# in directory take-home/vuejs
npm run serve
```

The frontend site will be accessible at: `http://localhost:8080`

