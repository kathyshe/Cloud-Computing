## :shipit: CITY-ZIP-WEATHER MICROSERVICES: :shipit:

**1.	Build image from city-to-zip python file, then run a container from this image.**
<img width="503" alt="build image 1" src="https://user-images.githubusercontent.com/113223572/217951707-f808ee0f-9332-49ff-98c9-204cbe28d377.png">

<img width="1382" alt="image 1" src="https://user-images.githubusercontent.com/113223572/217951924-48eec8a1-f036-48bb-b719-fcd508c8985e.png">

<img width="503" alt="image 1 to container" src="https://user-images.githubusercontent.com/113223572/217951943-79ae4a08-6ff4-448d-a597-ce217b3d38c1.png">

<img width="1382" alt="Container1" src="https://user-images.githubusercontent.com/113223572/217951848-dca63677-9032-453a-86e5-ca605611beb9.png">

**2.	Build image from zip-to-weather python file, then run a container from this image.**
<img width="498" alt="build image 2" src="https://user-images.githubusercontent.com/113223572/217952026-08165725-1906-42c6-b7bf-07c5ffdd3462.png">

<img width="498" alt="image 2 to container" src="https://user-images.githubusercontent.com/113223572/217952042-b798e8a7-fe45-4fb7-93dd-2fa1aa095952.png">

<img width="1382" alt="截屏2023-02-09 13 12 05" src="https://user-images.githubusercontent.com/113223572/217952062-32d059cc-40ad-4960-bed6-29a4ebd8b213.png">

**3.  Create network and add containers to network.**
<img width="498" alt="截屏2023-02-09 13 13 57" src="https://user-images.githubusercontent.com/113223572/217952163-502fea00-a908-466e-a756-6eecdd805e31.png">

<img width="835" alt="截屏2023-02-09 13 15 36" src="https://user-images.githubusercontent.com/113223572/217952179-9bae95bc-687d-49fc-a222-8b2b140103d3.png">

**4.  Check with browser and curl.**
<img width="1524" alt="截屏2023-02-09 13 38 11" src="https://user-images.githubusercontent.com/113223572/217952283-6a9f0df5-7e2f-4a07-9a7f-f6b10a444106.png">

<img width="1524" alt="截屏2023-02-09 13 38 42" src="https://user-images.githubusercontent.com/113223572/217952294-04b7a09c-0b87-4cd6-84db-b1f6a4c813b2.png">

<img width="673" alt="截屏2023-02-09 13 41 52" src="https://user-images.githubusercontent.com/113223572/217952311-93c3bf62-d80b-4dbe-90df-7446340e20cc.png">



*3.1 Hadoop: setting up a single node cluster*
	
	
_3.2 Install Java JDK 8 on Linux_

	•	$ java -version
	•	$ sudo apt-get update
	•	$ sudo apt-get install openjdk-8-jdk
	•	$ java -version //check if java is installed successfully
	
_3.3 Install ssh, sshd, pdsh_

	•	$ sudo apt-get install ssh
	•	$ sudo apt-get install sshd
	•	$ sudo apt-get install pdsh
	
_3.4 Download Hadoop from Apache Download Mirrors_

	•	$ wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz

_3.5 Unpack and save to Hadoop directory_

	•	$ tar xzf Hadoop-3.3.4.tar.gz
	
_3.6 Modify bashrc file and set java and Hadoop environment_

	•	$ update-alternatives --list java //find root of java
	•	$ vi ~/.bashrc //modify bashrc file and set environment
		//“i” to edit file, “ESC - :wq” to close and save file
			#Set JAVA_HOME 
			export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 
			#SET HADOOP_HOME 
			export HADOOP_HOME=$HOME/hadoop-3.3.4 
			#Add bin/ directory of Haddop to PATH 
			export PATH=$PATH:$HADOOP_HOME/bin
	•	$ . ~/.bashrc //source the environment
	•	$ cd etc/hadoop/ 
	•	$ vi hadoop-env.sh //configuration related to HDFS
			#Set JAVA_HOME 
			export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
	•	$ cd .. 
	•	$ cd ..
	•	$ bin/hadoop //display documentation

_3.7 Pseudo-distributed Operation_

	•	$vi ./etc/hadoop/core-site.xml
			<configuration>
			    <property>
			        <name>fs.defaultFS</name>
			        <value>hdfs://localhost:9000</value>
			    </property>
			</configuration>
	•	$ vi ./etc/hadoop/hdfs-site.xml
			<configuration>
			    <property>
			        <name>dfs.replication</name>
			        <value>1</value>
			    </property>
			</configuration>

**4. Prepare input data from GenerateRandomNumbers.java**

	•	$ mkdir PiCalculation
	•	$ cd PiCalculation
	•	$ vi GenerateRandomNumbers.java
	•	$ javac GenerateRandomNumbers.java
	•	$ java -cp . GenerateRandomNumbers
		o	//use 1000000 for number of random pairs
		o	//use 200 for radius
	•	//Input data will be stored in PiCalculationInput and used for calculation

**5. Setup passphraseless ssh**

	•	$ ssh localhost
	•	$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
	•	$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
	•	$ chmod 0600 ~/.ssh/authorized_keys 
	•	$ ssh localhost
	
**6. Make the HDFS directories, format the file system**

	•	$ cd hadoop-3.3.4
	•	$ bin/hdfs namenode -format
	•	$ sbin/start-dfs.sh
	•	$ sudo apt-get remove pdsh //if error occurs, trying remove pdsh; if password required, just restart SSH from GCP
	•	$ sbin/start-dfs.sh
	•	$ wget http://localhost:9870/ //if cannot connect, try to reset passphraseless again

**7. Make HDFS directories required to execute PiCalculation jobs**

	•	  $ cd hadoop-3.3.4/
	•	  $ bin/hdfs namenode -format
	•	  $ sbin/start-dfs.sh
	•	  $ wget http://localhost:9870/
	•	  $ bin/hdfs dfs -mkdir /user
	•	  $ bin/hdfs dfs -mkdir /user/kshe
	•	  $ bin/hdfs dfs -mkdir /user/kshe/picalculate
	•	  $ bin/hdfs dfs -mkdir /user/kshe/picalculate/input
	•	  $ bin/hdfs dfs -put ../PiCalculation/PiCalculationInput /user/kshe/picalculation/input
	
**8. Prepare the PiCalculation.java code**

	•	  $ cd /hadoop-3.3.4
	•	  $ vi PiCalculation.java 

**9. Compile the java file and create jar file**

	•	$ bin/hadoop com.sun.tools.javac.Main PiCalculation.java
	•	$ jar cf wc.jar PiCalculation*class  
	•	//Error 1: Could not find or load main class com.sun.tools.javac.Main, add following to hadoop-env.sh file:
		o	$ cd etc/hadoop/ 
		o	$ vi hadoop-env.sh
		o	export HADOOP_CLASSPATH=/usr/lib/jvm/java-8-openjdk-amd64/lib/tools.jar

**10. Execute program and view output file**

	•	$ bin/hadoop jar wc.jar PiCalculation /user/kshe/picalculation/input /user/kshe/picalculation/output
	•	//Error 1: input file path does not exist: try executing the following command instead:
		o	$ bin/hadoop jar wc.jar PiCalculation picalculation/input /user/kshe/picalculation/output
	•	$ bin/hdfs dfs -ls /user/kshe/picalculation/output
	•	$ bin/hdfs dfs -cat /user/kshe/picalculation/output/part-r-00000 //check output file

**11. Shutdown hadoop**

	•	$ sbin/stop-dfs.sh //if error occurs, reset passphraseless phase again
