This is a repository containing code for execution of a simple Airflow pipeline in Docker.

**Prerequisites:**
1. Docker Desktop installed
2. Docker Compose installed

**Running instructions:**

1. Clone the repository to your local machine.
2. Start Docker Desktop.
3. Open Terminal. Navigate to the folder containing cloned repository:
   ``` 
   cd path/to/cloned repository
   ```
**3.1** If you are on Linux machine **only**, run 
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
to align Airflow user ID with your user ID. This is to make sure that Airflow does not create stuff as a root user.

4. Start Airflow in Docker by running 
   ```
   docker-compose -f docker-compose.yaml up
   ```
5. After docker-compose finishes, go to localhost:8080 in your browser to see Airflow UI. Enter login and password (airflow/airflow by defaukt) to log in.
![alt text](https://miro.medium.com/max/1400/1*Nc17yaLOx87o7i_-N62jIA.png)

**Triggering a DAG**
1. Move DAG slider from 'off' to 'on'.
2. Click 'Run' button on the right.
3. Click on green circle under 'Runs' to view execution progress.

**Adding a new DAG**
1. Navigate to dags folder in your local repository copy. 
2. Create a new DAG file, e.g. my_new_dag.py
3. Add execution steps.
4. Navigate to Airflow UI to see your new DAG.
