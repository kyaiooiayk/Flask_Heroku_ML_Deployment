# MLOps (Machine Learning Operations)
How to create, deploy and manage your ML projects. But what do we mean when we talk about model deployment? Training a ML model using a method of your choice. Writing a service using FastAPI for exposing the model through a service endpoint. Packaging the service into a Docker container. Deploying the Docker container to (AWS) Kubernetes Cluster to scale up the service.

![image](https://user-images.githubusercontent.com/89139139/148684996-107b35e5-7136-4842-a132-119db6ee48ce.png)
***

## Data Engineering
- Apache Nifi
- [[Apache Spark](https://spark.apache.org/) | [Notes](https://github.com/kyaiooiayk/pySpark-Notes)]
- Argo workflow
- Azue databricks
- Hadoop 
***

## Data validation
- [[Pandera](https://pandera.readthedocs.io/en/stable/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Data_validation/Pandera)]
- [[Great Expectations](https://greatexpectations.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Data_validation/Great_expectations)]
***

## Pipelines
- [[Apache Airflow](https://airflow.apache.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Airflow)]
- **Kubeflow Pipelines** is an orchestration subsystem built on Kubernetes.
- [MLeap](https://github.com/combust/mleap) allows data scientists and engineers to deploy machine learning pipelines from Spark and Scikit-learn to a portable format and execution engine. MLeap is a common serialisation format and execution engine for machine learning pipelines. 
- [How to Build MLOps Pipelines with GitHub Actions [Step by Step Guide]](https://neptune.ai/blog/build-mlops-pipelines-with-github-actions-guide)
- [[Prefect](https://www.prefect.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Prefect)]
***

## Model serialisation
- [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Model_Serialisation)
***

## Model lifecycle
- MLFlow
- Kubeflow
- [[Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/TensorFlowServing.md)]
- AWS SageMaker
***

## Dashboard
- Bokeh
- Plotly
***

## Deployment options
You essentially have two options:
 - If our application requires **low latency**, then we should deploy the model as a real- time API to provide super-fast predictions on single prediction requests over HTTPS, for example. We can deploy, scale, and compare our model prediction servers with SageMaker Endpoints using the REST API protocol with HTTPS and JSON.
 - For **less-latency-sensitive** applications that require high throughput, we should deploy our model as a batch job to perform batch predictions on large amounts of data in S3, for example. We will use SageMaker Batch Transform to perform the batch predic‐ tions along with a data store like Amazon RDS or DynamoDB to productionize the predictions,
***

## DevOps
DevOps is a role that integrates the job scope of software developers and operations teams to automate workflows.
- [ Git | [Notes](https://github.com/kyaiooiayk/Git-Cheatsheet)]
- [[Jenkins](https://www.jenkins.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Jenkins)]
- Maven : it is used to create deployment package.
- [[Docker](https://www.docker.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Docker)]
- [Kubernets | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Kubernetes)]
***

## Application Framework/Model Deployment
- Django
- [[Flask](https://flask.palletsprojects.com/en/2.1.x/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Flask)]
- [[Node.js]() | [Notes]()]
- [[Express.js]() | [Notes]()]
- [[React](https://reactjs.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/React)]
- Nginx
- Redis
- [[FastAPI](https://fastapi.tiangolo.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/FastAPI)]
- [[Heroku](https://www.heroku.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Heroku)]
- [[Streamlit](https://streamlit.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Streamlit)]
***

## Cloud computing
Cloud computing is a name which refers to cluster machines on the cloud.
- [[AWS (Amazon Web Services)](https://aws.amazon.com/?nc2=h_lg) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS)]
- [[Microsoft Azure](https://azure.microsoft.com/en-gb/) | Notes]
- [[GCP (Google Cloud Platform)](https://cloud.google.com/) | Notes]
***

## Edge computing
- Edge computing referes to computation done on edge devices, meaning consumer devices. Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data.
- [TensorFlow Lite | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/TensorFLowLite.md)]
***

## Relational Database
- RDB (relational database) is a database that stores data into tables with rows and columns.
- How to turn SQL-like into a map-reduce job that can run on a distributed file system. This is essentially what we mean by relational database at scale.
- [Hive | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Hive.md)] (twice as popular as Pig and developed by Facebook). Hive provides SQL type querying language for the ETL purpose on top of Hadoop file system. 
- Pig (less popular than Hive)
***

## Data warehouse tools
A **data warehouse*** stores data in files or folders in a hierarchical manner whereas a **data lake** uses a flat architecture. Every bit of data in the lake has a unique ID and is tagged with sets of extended metadata tags. When you need information, the data lake can be queried for relevant data, and that smaller set of data can be accessed to get the data you need. The ability to append your own metadata enables you to make it very easy to search your data.
- MongoDB
- CosmosDB
- Looker
- Stitch
- DBT
- Snowflake
- Amazon redshift
- Azure synapse
- Google big query
***

##  Management 
Unified analytics platform.
- Databricks 
***

## Streaming
- Apache Kafka
- Google Dataflow
***

## Schedulers
- [5 ways to schedule Jupyter Notebook](https://mljar.com/blog/schedule-jupyter-notebook/)
***

## RESTful APIs & Microservices
- **Microservices** function as the “building‐blocks” of the application by performing various services.
- **RESTful APIs** function as the “glue” that integrates the microservices into an application.
***

## Version control system (VCS)
- Version control system (VCS) also known as revision control or source control, records and manages changes to files and folders. [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/VCS.md)
- [[Hydra](https://hydra.cc/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/VCS/Hydra)]
- [[DVC](https://dvc.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/VCS/DVC)]
***

## References
- [A Full End-to-End Deployment of a Machine Learning Algorithm into a Live Production Environment](https://www.kdnuggets.com/2021/12/deployment-machine-learning-algorithm-live-production-environment.html)
- [An full E2E description of a deployed ML for stock market allocation](https://principiamundi.com/posts/didact-anatomy/?utm_source=substack&utm_medium=email)
- [Guide to evaluating MLOps platforms *by thoughtworks*](https://www.thoughtworks.com/content/dam/thoughtworks/documents/whitepaper/tw_whitepaper_guide_to_evaluating_mlops_platforms_2021.pdf)
- [MLOps Is a Mess But That's to be Expected](https://www.mihaileric.com/posts/mlops-is-a-mess/)
- [VCS](https://deploybot.com/blog/version-control-systems-and-continuous-deployment-tools-a-perfect-fit)
- [ML Experiment Tracking: What It Is, Why It Matters, and How to Implement It](https://neptune.ai/blog/ml-experiment-tracking)
- [HTTP vs. REST APIs](https://hevodata.com/learn/http-api-vs-rest-api/)
- [Awesome production machine learning](https://github.com/EthicalML/awesome-production-machine-learning#model-and-data-versioning)
- [MLOps Is a Mess But That’s to be Expected](https://www.kdnuggets.com/2022/03/mlops-mess-expected.html)
- [MLOps Principles](https://ml-ops.org/content/mlops-principles)
- [What is an MLOps Engineer?](https://www.kdnuggets.com/2022/03/mlops-engineer.html)
- [Google Rules of Machine Learning: Best Practices for ML Engineering](https://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf)
