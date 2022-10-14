## DESIGN APPROACH - RANDOM SAMPLING TO ESTIMATE PI: :shipit:


## IMPLEMENTATION STEPS: :shipit:

**Step 1: Generate an input file to the Pi MapReduce program**
	
	Step 1.1: Create a regular Java program which accepts two command line arguments.
	
	R: The radius
	
	N: The number of (x, y) pairs to create
	
	The Java program then randomly generates N pairs of (x, y) and displays them on the standard output.
	
	Step 1.2: Run the program created in Step 1.1 and save the result in a file. The file is the input to Step 2's Pi MapReduce program.

**Step 2: Create a MapReduce program to calculate the numbers of inside darts and outside darts**

**Step 3: Use the file generated in Step 1.2 as the input to execute the MapReduce program created in Step 2**

**Step 4: Calculate Pi in the driver program based on the numbers of inside darts and outside darts.**

## IMPLEMENTATION DETAILS: :shipit:

**1. Create a Ubuntu Virtual Machine on GCP**

**2. Create a VM instance** (note: since the number of pairs generated may be large, I went with 4GB to avoid "java heap error")

**3. Configure the environment**

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

	•	$ bin/hadoop jar wc.jar PiCalculation /user/kshe/picalculation/input /user/lchen/picalculation/output
	•	//Error 1: input file path does not exist: try executing the following command instead:
		o	$ bin/hadoop jar wc.jar PiCalculation picalculation/input /user/lchen/picalculation/output
	•	$ bin/hdfs dfs -ls /user/kshe/picalculation/output
	•	$ bin/hdfs dfs -cat /user/kshe/picalculation/output/part-r-00000 //check output file

**11. Shutdown hadoop**

	•	$ sbin/stop-dfs.sh //if error occurs, reset passphraseless phase again



