## Python FastAPI Examples  

```
|-python_fastapi - A simple project to create Rest API with FastAPI   
	|  
	|- src    
	    |- main.py - Programe entry  
            |- routers/ - Routes for endpoints   
            |- services/ - Business Logic and DAO layer calls   
            |- model -  pydentic models   
            |- dependencies - Dependencies for routes    
            |- middleware - Custom middleware   
            |- tests - Test files    
            

```

### To run this program run below command from the project root directory   

uvicorn src.main:app --reload
