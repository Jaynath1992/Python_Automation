pipeline {
        agent any
        stages {
		stage('Run Test') {
			parallel {
				stage('Build Phase') {
					agent python
					steps {
						echo 'Build phase completed'
					}
				}
				stage('Testing Phase') {
					agent python
					steps {
						echo 'Testing phase comepleted'
					}
				}
				stage('Deployment Phase') {
					agent pyhton
					steps {
						echo 'Deployment completed'
					}
				}
			}
		}
        }    
                
}


