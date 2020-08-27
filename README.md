# Python_HelloWorld_DockerApp

Commands to build docker image and run docker container:
Docker Image Build Command: Docker build -t <ImageName> . (Command should be executed from the path where Dockerfile exists)
Docker Container Run Command: Docker run -d -p 8080:8080 --name <containername> <ImageName>
  
1) Application url should return a greeting such as Hello! as json or plain text (ex: when you open a browser and navigate to http://localhost:8080, it should return Hello! plain text.)

After running docker container on local machine, when user open a browser and navigate to http://localhost:8080, it will show Hello! plain text greeting.
 2) Application should provide a health endpoint (http://localhost:8080/healthz) that returns HTTP status (200 OK) which indicates health of the application and returns a valid json with the following information:
 
    Healthcheck endpoint: http://localhost:8080/healthz will return below format status.
 {
  "status": "200 OK",
  "version": "0.0.1",
  "uptime": "up since 2020-08-04 08:00:05"
}

3) What other information would you add to health endpoint json object in step 2? Explain what would be the use case for that extra information?

      Server Metrics: Server metrics will help a DevOps or Non-DevOps person to understand the health of the server/application.
                   If healthCheck pass print "<$ApplicationName> is up and running and application metadata is an extra additional information which helps"
                   else
                   print "application healthcheck failure message with Error Code, Server Metrics( Disk Space, CPU, Memory, etc..)" 
                   Print "Escalation process details" 
                   Fi
                   
4) Create a docker file to build, package, deploy, and run this application locally with Docker.
     
     Done in above steps.

5) How would you automate the build/test/deploy process for this application? (a verbal answer is enough. installation of CICD is bonus, not required)

     5a) What branching strategy would you use for development? 
          Feature branch workflow is preferred, Devs work on individual feature branch based on the stories assigned from story board to test code vigorously before it reaches mainline branch. To merge feature branch code to mainline branch it must go through the PR process and all necessary approvals. This process will give other senior Devs or team leads the opportunity sign off on a feature before it gets integrated into the official project. Or, if you get stuck in the middle of a feature, you can open a pull request asking for suggestions from your colleagues. Process might change based on Dev and DevOps team requirements.
     5b) What CICD tool/service would you use?
          CICD is a methodology to achieve fast and smooth release process and it involve various automation tools and scripting languages. Since the web app is containerized, I would use GitHub/BitBucket for source control management, Bamboo/Jenkins as an orchestrator tool for build and deploy process. Docker to containerize application. Apps will be deployed to Kubernetes and automate deployments and operations on k8s cluster using kubectl cli.
     5c) What stages would you have in the CICD pipeline?
          Stages might differ based on tools and technologies adopted by the organization, starting from PR approval process few orgs doesn’t follow it.
          Ideal stages in a CICD process:
             •	PR approval process to merge code into mainline branch.
             •	Unit testing and Build stage.
             •	Code analysis.
             •	Deploy built artifact to Dev.
             •	Automated functional testing against Dev environment.
             •	Automated Deploy to Test after successful testing in Dev.
             •	Automated functional testing against Test environment.
             •	Change process is different in different organizations.
             •	Deploy to Prod.
     5d) What would be the purpose of each stage in CICD pipeline?
          PR approval process: This will help to avoid broken code merged to mainlain branch.
          Unit Testing and Build Stage: This will help testing code during build process.
          Code Analysis: To find vulnerabilities in application.
          Testing: This can be done in multiple stages (Integration testing, Load testing etc.)
          Change Process: This requires test results, approvals from product owners to deploy application to Prod. Change board will take a decision based on test results,      change window and analyze if it requires downtime.
          Deploy: Deploying application to Environment. 


  
