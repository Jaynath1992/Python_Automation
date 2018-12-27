pipeline {
        agent any
        stages {
		stage('Run Test') {
			parallel {
				stage('Build Phase') {
					steps {
						echo 'Build phase completed'
					}
				}
				stage('Testing Phase') {
					steps {
						echo 'Testing phase comepleted'
					}
				}
				stage('Deployment Phase') {
					steps {
						echo 'Deployment completed'
					}
				}
			}
		}
        }    
                
}


